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

horizontal = "cleanroom_ijacr_horizontal"
lateral = "cleanroom_ijacr_lateral"
#define the file name:

filename_cint = 'operator_center/operator-center-int-rfile.txt'

filename_lint = 'operator_left/operator-center-left-int-rfile.txt'

filename_rint = 'operator_right/operator-center-right-int-rfile.txt'

x1, y1 = read_data(os.path.join(horizontal, filename_cint))
# 读取文件2的数据
# x2, y2 = read_data(os.path.join(lateral, filename_rint))

# # 读取文件3的数据
# x3, y3 = read_data(os.path.join(horizontal, filename_r2))
# # 读取文件4的数据
# x4, y4 = read_data(os.path.join(lateral, filename_r2))

# 创建图表对象
fig, ax = plt.subplots()

# 绘制第一个文件的数据
ax.plot(x1, y1, color='blue', label='horizontal center')
# ax.plot(x1, y1, color='blue', label='side_maximum_velocity_1.0')

# 添加阴影标记
ax.fill_between(x1, y1, color='lightblue', alpha=0.5)

# 设置图表属性
ax.set_xlabel('Time (s)')
ax.set_ylabel('Surface Mass Fraction integral')

ax.grid()

# 添加图例
ax.legend()

# 计算曲线的积分
integral_value = calculate_integral(x1, y1)

# 在颜色区域上显示积分值
# ax.text(0.5, 0.5, f'Integral: {integral_value} m^2*s', color='red', fontsize=12, transform=ax.transAxes)
# ax.text(0.5, 0.5, f'Integral: {integral_value:.4f} m^2*s', color='red', fontsize=12, transform=ax.transAxes)
# 在颜色区域上显示积分值（保留四位有效小数，并显示为数学公式）
ax.text(0.5, 0.5, f'Integral: ${integral_value:.4f} \, \mathrm{{m^2 \cdot s}}$', color='red', fontsize=12, transform=ax.transAxes)


plt.savefig("horizontal_center_integral.png")
# plt.savefig("sidewall_integral.png")
# 显示图表
plt.show()
