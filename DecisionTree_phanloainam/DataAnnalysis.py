import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("mushrooms.csv")

# Hàm helper để thêm nhãn số trên cột
def add_labels(ax):
    for p in ax.patches:
        height = p.get_height()
        ax.annotate(f'{height}',
                    (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='bottom', fontsize=9, color='black')

# 1. Số lượng mẫu theo class
plt.figure(figsize=(6,4))
ax = sns.countplot(x='class', data=data)
add_labels(ax)  # 👈 thêm số liệu
plt.title('Số lượng mẫu theo class (e = edible, p = poisonous)')
plt.savefig("plot_class_count.png")
plt.close()

# 2. Số lượng mẫu theo một số feature nổi bật
features_to_plot = ['odor', 'cap-color', 'gill-color']
for feature in features_to_plot:
    plt.figure(figsize=(8,4))
    ax = sns.countplot(x=feature, hue='class', data=data)
    add_labels(ax)  # 👈 thêm số liệu
    plt.title(f'Phân phối {feature} theo class')
    plt.legend(title='class')
    plt.xticks(rotation=45)
    plt.savefig(f"plot_{feature}.png")
    plt.close()

# 3. Số lượng giá trị unique của tất cả các feature
unique_counts = data.nunique().sort_values(ascending=False)

plt.figure(figsize=(10,4))
ax = sns.barplot(x=unique_counts.index, y=unique_counts.values)
add_labels(ax)  # 👈 thêm số liệu
plt.title('Số lượng giá trị khác nhau của mỗi feature')
plt.ylabel('Số lượng giá trị unique')
plt.xticks(rotation=45)
plt.savefig("plot_unique_values.png")
plt.close()

# 4. Xuất bảng unique_counts ra file CSV
unique_counts.to_csv("unique_counts.csv", header=["unique_values"])