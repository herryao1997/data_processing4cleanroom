import matplotlib.pyplot as plt
import numpy as np

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

# 创建柱状图，调整图形的大小
fig, ax = plt.subplots(figsize=(12, 6))

# 提取横坐标和纵坐标数据
x = list(data[cases[0]].keys())

# 设置每个柱子的宽度
bar_width = 0.15
index = np.arange(len(x))

# 循环绘制每个case的柱子
for i, case in enumerate(cases):
    y = [data[case][instrument] for instrument in x]

    # 使用不同的偏移量来避免重叠
    offset = i * bar_width
    ax.bar(index + offset, y, bar_width, label=case)

# 添加标签和标题
ax.set_xlabel('Instruments')
ax.set_ylabel('Mass fraction of Hcl on instrument')
# ax.set_title('Bar Chart for Different Cases')

# 设置x轴标签
ax.set_xticks(index + bar_width * (len(cases) - 1) / 2)
ax.set_xticklabels(x, ha='center')  # 在x轴每个元素的中间显示标签

# 设置坐标轴为对数刻度
# ax.set_yscale('log')

# 显示图例
ax.legend()

# 调整底部边距
plt.subplots_adjust(bottom=0.2)

plt.savefig("facet weighted average mass fraction of Hcl on instruments.png", dpi=300)
plt.savefig("facet weighted average mass fraction of Hcl on instruments.svg", format="svg")
# 显示柱状图
plt.show()
