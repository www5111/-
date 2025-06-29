def is_palindrome(num):
    """判断一个数是否为回文数"""
    num_str = str(num)
    return num_str == num_str[::-1]

# 测试
print(is_palindrome(121))  # True
print(is_palindrome(123))  # False
print(is_palindrome(1221))  # True


def calculate_average(*args):
    """计算任意数量参数的平均值"""
    if not args:
        return 0
    return sum(args) / len(args)

# 测试
print(calculate_average(1, 2, 3))  # 2.0
print(calculate_average(10, 20, 30, 40))  # 25.0
print(calculate_average())  # 0

def find_longest_string(*strings):
    """返回任意多个字符串中最长的一个"""
    if not strings:
        return None
    return max(strings, key=len)

# 测试
print(find_longest_string("apple", "banana", "orange"))  # banana
print(find_longest_string("hello", "world"))  # hello
print(find_longest_string())  # None

# main.py
from rectangle import area, perimeter

# 使用模块中的函数
print("矩形面积:", area(5, 3))  # 15
print("矩形周长:", perimeter(5, 3))  # 16