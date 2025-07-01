import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('train.csv')

# 计算各乘客等级的总人数和生还人数
survival_by_class = data.groupby('Pclass')['Survived'].agg(['count', 'sum'])

# 计算生还率
survival_by_class['survival_rate'] = survival_by_class['sum'] / survival_by_class['count'] * 100

# 重置索引以便绘图
survival_by_class = survival_by_class.reset_index()

# 绘制直方图
plt.figure(figsize=(10, 6))
bars = plt.bar(survival_by_class['Pclass'], survival_by_class['survival_rate'],
               color=['gold', 'silver', 'brown'], width=0.5)

plt.title('泰坦尼克号乘客等级对生还率的影响', fontsize=15)
plt.xlabel('乘客等级 (1=头等舱, 2=二等舱, 3=三等舱)', fontsize=12)
plt.ylabel('生还率 (%)', fontsize=12)
plt.xticks([1, 2, 3])
plt.ylim(0, 100)

# 在柱子上添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}%',
             ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()