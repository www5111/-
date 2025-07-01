import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 加载数据
data = pd.read_csv('train.csv')

# 排除年龄缺失的乘客
data_with_age = data[data['Age'].notna()]

# 按年龄段分组
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70+']
data_with_age['AgeGroup'] = pd.cut(data_with_age['Age'], bins=bins, labels=labels, right=False)

# 计算各年龄段的生还率
survival_by_age = data_with_age.groupby('AgeGroup')['Survived'].agg(['mean', 'count'])
survival_by_age.columns = ['SurvivalRate', 'Count']

# 绘制直方图
plt.figure(figsize=(12, 6))
bars = plt.bar(survival_by_age.index, survival_by_age['SurvivalRate'],
               color='skyblue', edgecolor='black')

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}',
             ha='center', va='bottom')

# 添加标题和标签
plt.title('Survival Rate by Age Group on Titanic', fontsize=16)
plt.xlabel('Age Group', fontsize=14)
plt.ylabel('Survival Rate', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 显示图表
plt.tight_layout()
plt.show()

# 返回各年龄段生还率数据
survival_by_age