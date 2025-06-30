import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import datetime

# 1. 生成随机销售数据（30天）
np.random.seed(42)  # 设置随机种子保证可重复性
start_date = datetime.datetime(2023, 1, 1)
dates = [start_date + datetime.timedelta(days=x) for x in range(30)]
sales = np.random.randint(50, 200, size=30).cumsum()  # 生成累加随机销售数据

# 添加一些随机波动
for i in range(5, 30, 5):
    sales[i] = sales[i] * np.random.uniform(0.7, 1.3)

# 2. 创建DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Sales': sales
})

# 3. 绘制折线图
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Sales'],
         marker='o',
         linestyle='-',
         color='royalblue',
         linewidth=2,
         markersize=8,
         markerfacecolor='red')

# 4. 美化图表
plt.title('2023年1月销售趋势', fontsize=16, pad=20)
plt.xlabel('日期', fontsize=12)
plt.ylabel('销售额 (万元)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# 设置日期格式
date_format = DateFormatter("%m-%d")
plt.gca().xaxis.set_major_formatter(date_format)

# 旋转日期标签
plt.xticks(rotation=45)

# 添加数据标签
for x, y in zip(df['Date'], df['Sales']):
    plt.text(x, y+50, f'{y:.0f}',
             ha='center',
             va='bottom',
             fontsize=9)

# 调整边距
plt.tight_layout()

# 5. 显示图表
plt.show()

# 6. 可选：保存图表
# plt.savefig('sales_trend.png', dpi=300, bbox_inches='tight')