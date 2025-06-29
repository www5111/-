# 使用列表推导式生成1-100的整数列表
numbers = [x for x in range(1, 101)]

# 输出其中的所有偶数
even_numbers = [num for num in numbers if num % 2 == 0]
print("1-100之间的所有偶数:")
print(even_numbers)

def remove_duplicates(lst):
    """删除列表中的重复元素并保持顺序不变"""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# 示例列表
example_list = [3, 5, 2, 3, 8, 5, 9, 2]

# 删除重复元素
unique_list = remove_duplicates(example_list)
print("原始列表:", example_list)
print("删除重复元素后的列表:", unique_list)


keys = ["a", "b", "c"]
values = [1, 2, 3]

# 将两个列表合并为字典
merged_dict = dict(zip(keys, values))
print("合并后的字典:")
print(merged_dict)


# 定义学生信息元组
student_info = ("张三", 20, 89.5)

# 解包元组
name, age, score = student_info

# 输出各字段
print("学生信息:")
print(f"姓名: {name}")
print(f"年龄: {age}")
print(f"成绩: {score}")