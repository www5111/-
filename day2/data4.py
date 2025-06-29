import numpy as np

# 创建3×4的二维数组，元素为1到12的整数
arr = np.arange(1, 13).reshape(3, 4)
print("原始数组:")
print(arr)

# 1. 打印数组的形状、维度和数据类型
print("\n1. 数组属性:")
print("形状(shape):", arr.shape)
print("维度(ndim):", arr.ndim)
print("数据类型(dtype):", arr.dtype)

# 2. 将数组元素乘以2，打印结果
arr_multiplied = arr * 2
print("\n2. 数组乘以2的结果:")
print(arr_multiplied)

# 3. 将数组重塑为4x3的形状，打印新数组
arr_reshaped = arr.reshape(4, 3)
print("\n3. 重塑为4x3的数组:")
print(arr_reshaped)



import numpy as np

# 创建4x4数组
array = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])

print("原始数组:")
print(array)

# 1. 提取第2行所有元素（索引从0开始）
row_2 = array[1, :]
print("\n1. 第2行所有元素:")
print(row_2)

# 2. 提取第3列所有元素
col_3 = array[:, 2]
print("\n2. 第3列所有元素:")
print(col_3)

# 3. 提取子数组（第1、2行和第2、3列）
sub_array = array[0:2, 1:3]  # 行切片0:2表示第1-2行，列切片1:3表示第2-3列
print("\n3. 子数组（第1-2行，第2-3列）:")
print(sub_array)

# 4. 将大于10的元素替换为0
modified_array = array.copy()  # 创建副本避免修改原数组
modified_array[modified_array > 10] = 0
print("\n4. 大于10的元素替换为0后的数组:")
print(modified_array)



import numpy as np

# 创建数组A（3x2）
A = np.arange(1, 7).reshape(3, 2)
print("数组A:\n", A)

# 创建数组B（1x2）
B = np.array([10, 20])
print("\n数组B:\n", B)

# 1. 逐元素相加（广播）
add_result = A + B  # 广播机制自动扩展B到(3,2)
print("\n1. A + B (广播加法):\n", add_result)

# 2. 逐元素相乘（广播）
mul_result = A * B  # 广播机制自动扩展B到(3,2)
print("\n2. A * B (广播乘法):\n", mul_result)

# 3. 计算A的每一行与B的点积
dot_result = np.dot(A, B)  # 或使用 A @ B
print("\n3. A每行与B的点积:\n", dot_result)

# 验证点积计算（可选）
print("\n验证点积计算:")
for i in range(A.shape[0]):
    print(f"第{i+1}行点积: {np.dot(A[i,:], B)}")