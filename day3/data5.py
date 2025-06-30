import pandas as pd
import numpy as np

# 1. 创建包含指定数据的DataFrame并保存为CSV
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Score': [85, 92, 78, np.nan, 88],
    'Grade': ['A', 'A', 'B', 'B', 'A']
}

df = pd.DataFrame(data)
df.to_csv('students.csv', index=False)  # 不包含索引列
print("1. 原始CSV文件已创建: students.csv")
print(df)

# 2. 读取CSV文件并打印前3行
df_read = pd.read_csv('students.csv')
print("\n2. 读取CSV文件的前3行:")
print(df_read.head(3))

# 3. 处理缺失值
# 计算Score列的平均值（忽略NaN）
score_mean = df_read['Score'].mean()

# 填充缺失值
df_cleaned = df_read.copy()
df_cleaned['Score'].fillna(score_mean, inplace=True)  # 用平均分填充Score
df_cleaned['Name'].fillna('Unknown', inplace=True)    # 用'Unknown'填充Name

print("\n3. 处理缺失值后的DataFrame:")
print(df_cleaned)

# 4. 保存处理后的DataFrame为新CSV文件
df_cleaned.to_csv('students_cleaned.csv', index=False)
print("\n4. 处理后的数据已保存为: students_cleaned.csv")