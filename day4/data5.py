import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 加载数据
data = pd.read_csv('train.csv')

# 按年龄分组（分箱）并计算生还率
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80']
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# 按年龄组和性别分组统计生还率
survival_rate = data.groupby(['AgeGroup', 'Sex'])['Survived'].mean().unstack()

# 绘制直方图
ax = survival_rate.plot(kind='bar', figsize=(14, 7), color=['skyblue', 'salmon'])
plt.title('Survival Rate by Age Group and Gender (with Annotations)', fontsize=14)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Survival Rate', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Gender', labels=['Female', 'Male'])
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加生还率标注
for p in ax.patches:
    height = p.get_height()
    if not np.isnan(height):  # 忽略NaN值
        ax.annotate(
            f'{height:.1%}',  # 显示为百分比
            (p.get_x() + p.get_width() / 2, height),
            ha='center', va='bottom',
            xytext=(0, 3),
            textcoords='offset points',
            fontsize=10
        )

plt.tight_layout()  # 调整布局避免文字重叠
plt.show()