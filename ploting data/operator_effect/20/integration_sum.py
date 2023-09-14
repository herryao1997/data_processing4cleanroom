import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import os


def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    x = []
    y = []
    for line in lines:
        data = line.strip().split(' ')
        y.append(float(data[1]))
        x.append(float(data[2]))

    return x, y


def calculate_integral(x, y):
    integral = np.trapz(y, x)
    return integral


def plot_and_save_integral(ax, x, y, label='lateral left'):
    # 绘制数据
    ax.plot(x, y, color='blue', label=label)
    ax.fill_between(x, y, color='lightblue', alpha=0.5)
    # 设置x轴范围和y轴最小值
    ax.set_xlim(0, 300)
    ax.set_ylim(0, None)  # y轴最小值为0
    ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))

    # 设置图表属性
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Surface Mass Fraction integral (m$^2$)')
    ax.grid()
    legend = ax.legend(loc='lower right', fontsize=10, ncol=2)
    legend.get_frame().set_alpha(0.5)  # 设置图例的透明度为0.5


    # 计算曲线的积分
    integral_value = calculate_integral(x, y)

    # 在颜色区域上显示积分值（保留四位有效小数，并显示为数学公式）
    ax.text(0.45, 0.5, f'Integral: ${integral_value:.4f} \, \mathrm{{m^2 \cdot s}}$', color='red', fontsize=12,
            transform=ax.transAxes)


# 定义子图标签
subplot_labels = ['a.', 'b.', 'c.', 'd.', 'e.', 'f.']

horizontal = "cleanroom_ijacr_horizontal"
lateral = "cleanroom_ijacr_lateral"
# define the file name:
save_dir = "integral"

filename_cint = 'operator_center/operator-center-int-rfile.txt'

filename_lint = 'operator_left/operator-center-left-int-rfile.txt'

filename_rint = 'operator_right/operator-center-right-int-rfile.txt'

# 创建一个大图，两行三列的布局
fig, axes = plt.subplots(2, 3, figsize=(16, 8))

# 文件路径列表
file_paths = [
    os.path.join(lateral, filename_lint),
    os.path.join(lateral, filename_rint),
    os.path.join(lateral, filename_cint),
    os.path.join(horizontal, filename_lint),
    os.path.join(horizontal, filename_rint),
    os.path.join(horizontal, filename_cint)
]

# 标签列表
labels = ['lateral left', 'lateral right', 'lateral center', 'horizontal left', 'horizontal right', 'horizontal center']

for i in range(len(file_paths)):
    row = i // 3
    col = i % 3
    x, y = read_data(file_paths[i])
    plot_and_save_integral(axes[row, col], x, y, label=labels[i])

    # 添加子图标签
    axes[row, col].text(0.02, 0.9, subplot_labels[i], transform=axes[row, col].transAxes, fontsize=12, weight='bold')

# 调整子图之间的间距
plt.subplots_adjust(wspace=0.225, hspace=0.5)

# 保存大图
plt.savefig(os.path.join(save_dir, "combined_integral.png"))
plt.savefig(os.path.join(save_dir, "combined_integral.svg"), format="svg")
plt.show()
