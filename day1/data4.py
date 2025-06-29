#联系1
s1 = "Python is a powerful programming language"
s2 = "Let's learn together"

# (1) 提取单词"language"
words = s1.split()
last_word = words[-1]
print("(1) 最后一个单词:", last_word)  # 输出: language

# (2) 连接字符串并重复输出3次
combined = s1 + " " + s2
print("(2) 连接后的字符串重复3次:")
print((combined + "\n") * 3)  # 使用\n换行更美观

# (3) 输出所有以p或P开头的单词
p_words = [word for word in words if word.lower().startswith('p')]
print("(3) 以p或P开头的单词:", p_words)  # 输出: ['Python', 'powerful', 'programming']


#联系2
ss = "Hello, World! This is a test string. "

# (1) 去除前后空格
trimmed = ss.strip()
print("(1) 去除前后空格:", trimmed)

# (2) 转换为大写
upper_case = trimmed.upper()
print("(2) 转换为大写:", upper_case)

# (3) 查找"test"的起始下标
test_index = trimmed.find("test")
print("(3) 'test'的起始下标:", test_index)  # 输出: 21

# (4) 将"test"替换为"practice"
replaced = trimmed.replace("test", "practice")
print("(4) 替换后的字符串:", replaced)

# (5) 分割并用"-"连接
split_list = trimmed.split()
joined = "-".join(split_list)
print("(5) 分割后用-连接:", joined)