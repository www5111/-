import pandas as pd

# 1. 读取CSV文件并转换为DataFrame
df = pd.read_csv('drinks.csv')

# 2. 问题1：哪个大陆平均消耗的啤酒更多？
beer_by_continent = df.groupby('continent')['beer_servings'].mean()
max_beer_continent = beer_by_continent.idxmax()
print(f"\n1. 平均啤酒消耗最多的大陆是: {max_beer_continent}")
print(beer_by_continent.sort_values(ascending=False))

# 3. 问题2：每个大陆红酒消耗的描述性统计值
wine_stats = df.groupby('continent')['wine_servings'].describe()
print("\n2. 每个大陆红酒消耗的描述性统计值:")
print(wine_stats)

# 4. 问题3：每个大陆每种酒类别的消耗平均值
avg_consumption = df.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']].mean()
print("\n3. 每个大陆每种酒类别的消耗平均值:")
print(avg_consumption)

# 5. 问题4：每个大陆每种酒类别的消耗中位数
median_consumption = df.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']].median()
print("\n4. 每个大陆每种酒类别的消耗中位数:")
print(median_consumption)