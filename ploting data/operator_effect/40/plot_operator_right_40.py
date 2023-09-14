import os.path

import matplotlib.pyplot as plt
import numpy as np


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


horizontal = "cleanroom_ijacr_horizontal"
lateral = "cleanroom_ijacr_lateral"
#define the file name:


filename_c1 = 'operator_center/operator-center-average-rfile.txt'
filename_c2 = 'operator_center/operator-center-max-rfile.txt'
filename_cint = 'operator_center/operator-center-int-rfile.txt'

filename_l1 = 'operator_left/operator-center-left-average-rfile.txt'
filename_l2 = 'operator_left/operator-center-left-max-rfile.txt'
filename_lint = 'operator_left/operator-center-left-int-rfile.txt'

filename_r1 = 'operator_right/operator-center-right-average-rfile.txt'
filename_r2 = 'operator_right/operator-center-right-max-rfile.txt'
filename_rint = 'operator_right/operator-center-right-int-rfile.txt'

# 读取文件1的数据
x1, y1 = read_data(os.path.join(horizontal, filename_r1))
# 读取文件2的数据
x2, y2 = read_data(os.path.join(lateral, filename_r1))

# 读取文件3的数据
x3, y3 = read_data(os.path.join(horizontal, filename_r2))
# 读取文件4的数据
x4, y4 = read_data(os.path.join(lateral, filename_r2))
# # 读取文件5的数据
# x5, y5 = read_data(file5)
# # 读取文件6的数据
# x6, y6 = read_data(file6)
# # 读取文件7的数据
# x7, y7 = read_data(file7)
# # 读取文件6的数据
# x8, y8 = read_data(file8)



# 创建图表对象
fig, ax = plt.subplots()


# 绘制第一个文件的数据
ax.plot(x1, y1, color='blue', label='horizontal average')
#
# 绘制第二个文件的数据
ax.plot(x2, y2, color='red', label='lateral average')

# # 绘制第三个文件的数据
# ax.plot(x3, y3, '--', color='blue', label='horizontal maximum')
# #
# # 绘制第四个文件的数据
# ax.plot(x4, y4, '--', color='red', label='lateral maximum')
# #
# # 绘制第五个文件的数据
# ax.plot(x5, y5, '-*', color='blue', label='center_average_velocity_1.5')
# #
# # 绘制第六个文件的数据
# ax.plot(x6, y6, '-*', color='red', label='side_average_velocity_1.5')
#
# # 绘制第七个文件的数据
# ax.plot(x7, y7, '-^', color='blue', label='center_average_velocity_1.67')
# #
# # 绘制第八个文件的数据
# ax.plot(x8, y8, '-^', color='red', label='side_average_velocity_1.67')



# # 绘制第一个文件的数据
# ax.plot(x1, y1, color='blue', label='center_maximum_velocity_0.5')
# #
# # 绘制第二个文件的数据
# ax.plot(x2, y2, color='red', label='side_maximum_velocity_0.5')
#
# # 绘制第三个文件的数据
# ax.plot(x3, y3, '--', color='blue', label='center_maximum_velocity_1.0')
# #
# # 绘制第四个文件的数据
# ax.plot(x4, y4, '--', color='red', label='side_maximum_velocity_1.0')
#
# # 绘制第五个文件的数据
# ax.plot(x5, y5, '-*', color='blue', label='center_maximum_velocity_1.5')
# #
# # 绘制第六个文件的数据
# ax.plot(x6, y6, '-*', color='red', label='side_maximum_velocity_1.5')
#
# # 绘制第七个文件的数据
# ax.plot(x7, y7, '-^', color='blue', label='center_maximum_velocity_1.67')
# #
# # 绘制第八个文件的数据
# ax.plot(x8, y8, '-^', color='red', label='side_maximum_velocity_1.67')



# 设置图表属性
ax.set_xlabel('Time (s)')
ax.set_ylabel('Mass Fraction')
ax.grid()

# 添加图例
ax.legend(loc='best', ncol=2, fontsize=9)
plt.savefig("40_right_operator_average.png")
# 显示图表
plt.show()

