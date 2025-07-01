import numpy as np
import matplotlib.pyplot as plt

# 1. 准备数据
countries = ['挪威', '德国', '中国', '美国', '瑞典']
gold_medal = np.array([16, 12, 9, 8, 8])
silver_medal = np.array([8, 10, 4, 10, 5])
bronze_medal = np.array([13, 5, 2, 7, 5])

# 2. 设置图形和坐标轴
plt.figure(figsize=(10, 6))
x = np.arange(len(countries))  # 国家位置的x坐标

# 3. 绘制并列柱状图
bar_width = 0.25  # 柱子的宽度
plt.bar(x - bar_width, gold_medal, width=bar_width,
        color='gold', edgecolor='black', label='金牌')
plt.bar(x, silver_medal, width=bar_width,
        color='silver', edgecolor='black', label='银牌')
plt.bar(x + bar_width, bronze_medal, width=bar_width,
        color='#CD7F32', edgecolor='black', label='铜牌')  # 青铜色

# 4. 添加文本标签
def add_labels(x_pos, data, offset=0):
    for i in range(len(data)):
        plt.text(x_pos[i] + offset, data[i] + 0.2, str(data[i]),
                ha='center', va='bottom', fontsize=10)

add_labels(x, gold_medal, -bar_width)
add_labels(x, silver_medal, 0)
add_labels(x, bronze_medal, bar_width)

# 5. 美化图表
plt.title('2022年冬奥会奖牌榜', fontsize=16, pad=20)
plt.xlabel('国家', fontsize=12)
plt.ylabel('奖牌数量', fontsize=12)
plt.xticks(x, countries, fontsize=11)
plt.yticks(np.arange(0, 18, 2))  # 设置y轴刻度

# 添加图例和网格
plt.legend(loc='upper right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 调整布局
plt.tight_layout()

# 6. 显示图表
plt.show()

# 7. 可选：保存图表
# plt.savefig('olympic_medals.png', dpi=300, bbox_inches='tight')