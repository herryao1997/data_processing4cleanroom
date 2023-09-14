import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# 创建一个字典来存储不同case的数据
data = {}

cases = ["20% horizontal", "20% lateral", "30% horizontal", "30% lateral", "40% horizontal", "40% lateral"]

# 遍历六个.txt文件
for case in cases:
    case_data = {}

    # 读取文件并提取数据
    with open(case + ".txt", 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                instrument_name, value = parts
                case_data[instrument_name] = float(value)

    # 将提取的数据存储到字典中
    data[case] = case_data

# 计算每个case的总和
case_sums = {case: sum(data[case].values()) for case in cases}

# 创建柱状图，调整图形的大小
fig, ax = plt.subplots(figsize=(8, 6))

# 设置每个柱子的宽度
bar_width = 0.4
index = np.arange(len(cases))

# 提取y数据，即每个case的总和
y = [case_sums[case] for case in cases]

# 绘制柱状图，将最小值的柱子标成红色
min_index = np.argmin(y)
colors = ['red' if i == min_index else 'royalblue' for i in range(len(cases))]

bars = plt.bar(index, y, bar_width, label='Total Value', alpha=0.75, align='center', color=colors)

# 设置x轴标签
plt.xlabel('Cases')
plt.ylabel('Total integral value of contamination')

# 设置x轴刻度标签
plt.xticks(index, cases, rotation=20)

# 减小相邻两个点之间的距离
plt.subplots_adjust(wspace=0.1)  # Adjust the spacing between adjacent bars

# 标记最小的柱子
min_bar = bars[min_index]
min_bar.set_edgecolor('black')  # Add a black border to the red bar

# Add data labels on top of the bars
for i, v in enumerate(y):
    plt.text(i, v, f'{v:.4f}', ha='center', va='bottom', fontsize=10)

blue_patch = Patch(color='royalblue', label='Total value')
red_patch = Patch(color='red', label='Minimum value')
bar_legend = ax.legend(handles=[blue_patch, red_patch], loc='upper left', fontsize=10)
ax.add_artist(bar_legend)

plt.savefig("sum_acc.png", bbox_inches='tight')  # Adjust the bounding box to save with tight layout
plt.show()
