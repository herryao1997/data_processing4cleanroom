import matplotlib.pyplot as plt
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


def plot_and_save_integral(x, y, save_dir, label='lateral left'):
    # 创建图表对象
    fig, ax = plt.subplots()

    # 绘制数据
    ax.plot(x, y, color='blue', label=label)
    ax.fill_between(x, y, color='lightblue', alpha=0.5)
    # 设置x轴范围和y轴最小值
    ax.set_xlim(0, 300)
    ax.set_ylim(0, None)  # y轴最小值为0

    # 设置图表属性
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Surface Mass Fraction integral (m$^2$)')
    ax.grid()
    ax.legend()

    # 计算曲线的积分
    integral_value = calculate_integral(x, y)

    # 在颜色区域上显示积分值（保留四位有效小数，并显示为数学公式）
    ax.text(0.5, 0.5, f'Integral: ${integral_value:.4f} \, \mathrm{{m^2 \cdot s}}$', color='red', fontsize=12, transform=ax.transAxes)

    # 保存图表
    filename = f"{label.replace(' ', '_').lower()}_integral.png"
    plt.savefig(os.path.join(save_dir, filename))

    # 显示图表
    plt.show()


horizontal = "cleanroom_ijacr_horizontal"
lateral = "cleanroom_ijacr_lateral"
#define the file name:
save_dir = "integral"

filename_cint = 'operator_center/operator-center-int-rfile.txt'

filename_lint = 'operator_left/operator-center-left-int-rfile.txt'

filename_rint = 'operator_right/operator-center-right-int-rfile.txt'

#//lateral
x1, y1 = read_data(os.path.join(lateral, filename_lint))
# 读取文件2的数据
x2, y2 = read_data(os.path.join(lateral, filename_rint))
# 读取文件3的数据
x3, y3 = read_data(os.path.join(lateral, filename_cint))

#//horizontal
# # 读取文件4的数据
x4, y4 = read_data(os.path.join(horizontal, filename_lint))
# # 读取文件5的数据
x5, y5 = read_data(os.path.join(horizontal, filename_rint))
# # 读取文件6的数据
x6, y6 = read_data(os.path.join(horizontal, filename_cint))


# 假设 x1, y1 是你的数据，calculate_integral 是计算积分的函数，save_dir 是保存图表的目录
plot_and_save_integral(x1, y1, save_dir, label='lateral left')
plot_and_save_integral(x2, y2, save_dir, label='lateral right')
plot_and_save_integral(x3, y3, save_dir, label='lateral center')
plot_and_save_integral(x4, y4, save_dir, label='horizontal left')
plot_and_save_integral(x5, y5, save_dir, label='horizontal right')
plot_and_save_integral(x6, y6, save_dir, label='horizontal center')