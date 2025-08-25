import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

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
# Danh sách giá trị
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

@app.route('/')
def home():
    return render_template('index.html', odor_values=odor_values, cap_color_values=cap_color_values, gill_color_values=gill_color_values)

@app.route('/predict', methods=['POST'])
def predict_web():
    sample = {
        "odor": request.form['odor'],
        "cap-color": request.form['cap-color'],
        "gill-color": request.form['gill-color'],
    }

    prediction = predict(tree, sample)

    if prediction == "e":
        result = "🍄 Nấm ăn được (Edible)"
    elif prediction == "p":
        result = "☠️ Nấm độc (Poisonous)"
    else:
        result = "⚠️ Không xác định được"
        
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
