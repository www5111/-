x = 10
y = "10"
z = True

print(f"x的类型是: {type(x)}")  # <class 'int'>
print(f"y的类型是: {type(y)}")  # <class 'str'>
print(f"z的类型是: {type(z)}")  # <class 'bool'>


# 接收用户输入的半径
radius = float(input("请输入圆的半径: "))

# 计算圆的面积
area = 3.14 * radius ** 2

# 输出结果
print(f"半径为 {radius} 的圆的面积是: {area}")


# 将字符串"3.14"转换为浮点数
float_num = float("3.14")
print(f"转换为浮点数: {float_num}, 类型: {type(float_num)}")  # 3.14 <class 'float'>

# 将浮点数转换为整数
int_num = int(float_num)
print(f"转换为整数: {int_num}, 类型: {type(int_num)}")  # 3 <class 'int'>

# 观察差异
print("差异说明: 转换为浮点数保留了小数部分，转换为整数时丢弃了小数部分")

