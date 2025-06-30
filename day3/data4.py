import pandas as pd

# 1. 读取三个CSV文件
df_2015 = pd.read_csv('2015年国内主要城市年度数据.csv')
df_2016 = pd.read_csv('2016年国内主要城市年度数据.csv')
df_2017 = pd.read_csv('2017年国内主要城市年度数据.csv')

# 2. 合并数据，纵向连接
combined_df = pd.concat([df_2015, df_2016, df_2017], ignore_index=True)

# 3. 处理缺省值，填充为0
combined_df.fillna(0, inplace=True)

# 4. 按照年份来聚合并求每年的国内生产总值
gdp_by_year = combined_df.groupby('年份')['国内生产总值'].sum()

# 打印结果
print("合并后的数据前5行：")
print(combined_df.head())
print("\n每年的国内生产总值：")
print(gdp_by_year)