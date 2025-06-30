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

import pandas as pd

# 1. 读取数据
df_2015 = pd.read_csv('2015年国内主要城市年度数据.csv')
df_2016 = pd.read_csv('2016年国内主要城市年度数据.csv')
df_2017 = pd.read_csv('2017年国内主要城市年度数据.csv')

# 2. 合并数据
combined_df = pd.concat([df_2015, df_2016, df_2017], ignore_index=True)
combined_df.fillna(0, inplace=True)


# 5. 计算每个城市2015-2017年GDP的年均增长率
def calculate_growth_rate(df):
    # 获取每个城市三年的GDP数据
    city_gdp = df.pivot(index='地区', columns='年份', values='国内生产总值')

    # 计算年均增长率 [(2017GDP/2015GDP)^(1/2)-1]
    city_gdp['年均增长率'] = ((city_gdp[2017] / city_gdp[2015]) ** (1 / 2) - 1) * 100

    # 找出增长率最高和最低的五个城市
    top5 = city_gdp.nlargest(5, '年均增长率')[['年均增长率']]
    bottom5 = city_gdp.nsmallest(5, '年均增长率')[['年均增长率']]

    return city_gdp, top5, bottom5


gdp_growth, top5_cities, bottom5_cities = calculate_growth_rate(combined_df)

print("\n5. GDP年均增长率最高的5个城市:")
print(top5_cities)
print("\nGDP年均增长率最低的5个城市:")
print(bottom5_cities)


# 6. 对医院、卫生院数进行归一化处理（Min-Max标准化），并按年份比较
def normalize_hospital_data(df):
    # 按年份分组
    grouped = df.groupby('年份')

    # 对每个年份的数据进行Min-Max标准化
    normalized_dfs = []
    for year, group in grouped:
        min_val = group['医院、卫生院数'].min()
        max_val = group['医院、卫生院数'].max()
        group['医院、卫生院数_标准化'] = (group['医院、卫生院数'] - min_val) / (max_val - min_val)
        normalized_dfs.append(group)

    return pd.concat(normalized_dfs)


normalized_df = normalize_hospital_data(combined_df)

# 选取几个代表性城市查看医疗资源变化
sample_cities = ['北京', '上海', '广州', '深圳', '成都']
medical_resource_change = normalized_df[normalized_df['地区'].isin(sample_cities)][
    ['地区', '年份', '医院、卫生院数', '医院、卫生院数_标准化']].sort_values(['地区', '年份'])

print("\n6. 部分城市医疗资源标准化结果:")
print(medical_resource_change)

# 7. 提取四个一线城市的数据并保存为新CSV
first_tier_cities = ['北京', '上海', '广州', '深圳']
selected_data = combined_df[combined_df['地区'].isin(first_tier_cities)][
    ['地区', '年份', '国内生产总值', '社会商品零售总额']].sort_values(['地区', '年份'])

# 保存为新的CSV文件
selected_data.to_csv('一线城市GDP和消费数据.csv', index=False, encoding='utf_8_sig')

print("\n7. 四个一线城市数据已保存到: 一线城市GDP和消费数据.csv")
print(selected_data)