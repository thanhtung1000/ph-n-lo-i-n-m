import pickle
import tkinter as tk
from tkinter import ttk, messagebox

# ------------------------
# Load model
# ------------------------
with open("mushroom_model.pkl", "rb") as f:
    tree = pickle.load(f)

def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    feature = next(iter(tree))
    value = sample.get(feature, None)
    if value in tree[feature]:
        return predict(tree[feature][value], sample)
    else:
        return "Không xác định"

# ------------------------
# Danh sách giá trị (dịch song ngữ)
# ------------------------
odor_values = {
    "a": "a - hạnh nhân (almond)",
    "l": "l - hồi (anise)",
    "c": "c - creosote (nhựa gỗ)",
    "y": "y - cá (fishy)",
    "f": "f - hôi (foul)",
    "m": "m - mốc (musty)",
    "n": "n - không mùi (none)",
    "p": "p - cay (pungent)",
    "s": "s - cay nồng (spicy)"
}

cap_color_values = {
    "n": "n - nâu (brown)",
    "b": "b - be (buff)",
    "c": "c - quế (cinnamon)",
    "g": "g - xám (gray)",
    "r": "r - xanh lục (green)",
    "p": "p - hồng (pink)",
    "u": "u - tím (purple)",
    "e": "e - đỏ (red)",
    "w": "w - trắng (white)",
    "y": "y - vàng (yellow)"
}

gill_color_values = {
    "k": "k - đen (black)",
    "n": "n - nâu (brown)",
    "b": "b - be (buff)",
    "h": "h - chocolate",
    "g": "g - xám (gray)",
    "r": "r - xanh lục (green)",
    "o": "o - cam (orange)",
    "p": "p - hồng (pink)",
    "u": "u - tím (purple)",
    "e": "e - đỏ (red)",
    "w": "w - trắng (white)",
    "y": "y - vàng (yellow)"
}

# ------------------------
# GUI
# ------------------------
root = tk.Tk()
root.title("🍄 Mushroom Prediction")
root.geometry("400x400")
root.resizable(False, False)

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

title = ttk.Label(frame, text="DỰ ĐOÁN NẤM ĂN ĐƯỢC HAY KHÔNG", font=("Arial", 14, "bold"))
title.pack(pady=10)

# Odor
ttk.Label(frame, text="Mùi (odor):").pack(anchor="w")
odor_cb = ttk.Combobox(frame, values=list(odor_values.values()), state="readonly")
odor_cb.pack(fill="x", pady=5)

# Cap color
ttk.Label(frame, text="Màu mũ nấm (cap-color):").pack(anchor="w")
cap_cb = ttk.Combobox(frame, values=list(cap_color_values.values()), state="readonly")
cap_cb.pack(fill="x", pady=5)

# Gill color
ttk.Label(frame, text="Màu phiến nấm (gill-color):").pack(anchor="w")
gill_cb = ttk.Combobox(frame, values=list(gill_color_values.values()), state="readonly")
gill_cb.pack(fill="x", pady=5)

# Hàm xử lý
def on_predict():
    if not odor_cb.get() or not cap_cb.get() or not gill_cb.get():
        messagebox.showwarning("⚠️ Lỗi", "Vui lòng chọn đầy đủ thông tin!")
        return

    sample = {
        "odor": odor_cb.get().split(" - ")[0],
        "cap-color": cap_cb.get().split(" - ")[0],
        "gill-color": gill_cb.get().split(" - ")[0],
    }

    prediction = predict(tree, sample)

    if prediction == "e":
        result = "🍄 Nấm ăn được (Edible)"
    elif prediction == "p":
        result = "☠️ Nấm độc (Poisonous)"
    else:
        result = "⚠️ Không xác định được"

    messagebox.showinfo("Kết quả dự đoán", result)

# Button
ttk.Button(frame, text="🔮 Dự đoán", command=on_predict).pack(pady=15)

root.mainloop()