import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. 读取并合并数据
df_2015 = pd.read_csv('2015年国内主要城市年度数据.csv')
df_2016 = pd.read_csv('2016年国内主要城市年度数据.csv')
df_2017 = pd.read_csv('2017年国内主要城市年度数据.csv')

# 合并数据并填充缺失值
combined_df = pd.concat([df_2015, df_2016, df_2017], ignore_index=True)
combined_df.fillna(0, inplace=True)

# 2. 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 3. 绘制2015-2017年GDP直方图
plt.figure(figsize=(18, 8))

# 获取每个城市三年的GDP数据
gdp_pivot = combined_df.pivot(index='地区', columns='年份', values='国内生产总值')

# 只显示GDP最高的15个城市（避免过于拥挤）
top_cities = gdp_pivot[2017].nlargest(15).index
gdp_pivot = gdp_pivot.loc[top_cities]

# 绘制并列柱状图
bar_width = 0.25
x = np.arange(len(top_cities))

plt.bar(x - bar_width, gdp_pivot[2015], width=bar_width, label='2015年', color='#1f77b4')
plt.bar(x, gdp_pivot[2016], width=bar_width, label='2016年', color='#ff7f0e')
plt.bar(x + bar_width, gdp_pivot[2017], width=bar_width, label='2017年', color='#2ca02c')

# 添加标签和标题
plt.title('2015-2017年主要城市GDP对比（TOP15）', fontsize=16)
plt.xlabel('城市', fontsize=12)
plt.ylabel('国内生产总值（亿元）', fontsize=12)
plt.xticks(x, top_cities, rotation=45)
plt.legend()

# 添加数值标签
for i in x:
    for year, offset in zip([2015, 2016, 2017], [-bar_width, 0, bar_width]):
        value = gdp_pivot[year].iloc[i]
        plt.text(i + offset, value + 500, f'{value:.0f}',
                 ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()

# 4. 绘制2015年GDP饼图
plt.figure(figsize=(12, 12))

# 获取2015年GDP数据并按降序排序
gdp_2015 = df_2015[['地区', '国内生产总值']].sort_values('国内生产总值', ascending=False)

# 只显示前10名，其余合并为"其他"
top10 = gdp_2015.head(10)
others = pd.DataFrame({
    '地区': ['其他'],
    '国内生产总值': [gdp_2015['国内生产总值'][10:].sum()]
})
pie_data = pd.concat([top10, others])

# 绘制饼图
colors = plt.cm.tab20c(np.linspace(0, 1, len(pie_data)))
plt.pie(pie_data['国内生产总值'],
        labels=pie_data['地区'],
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        textprops={'fontsize': 10})

plt.title('2015年各城市GDP占比（TOP10）', fontsize=16)
plt.tight_layout()
plt.show()