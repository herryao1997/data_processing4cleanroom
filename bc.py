import sympy as sp

# 创建符号变量
x = sp.symbols('x')

# 定义方程
equation = 0.092 * (28.97 * (1 - x) - 36.46 * x) - 36.46 * x
# 解方程
solution = sp.solve(equation, x)
# 将质量分数转换为PPM
ppm = [s * 10**6 for s in solution]
print(type(solution))
print("解为 x_ppm =", ppm)

