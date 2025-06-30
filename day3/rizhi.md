# 实训日志

## 基本信息
- **日期**：2025年6月30日  
- **主要内容**：
  - Python网络爬虫实践
  - 模拟人类访问网站
  - Matplotlib数据可视化基础

## 学习内容

### 1. 网络爬虫实践
- 使用`requests`库获取网页数据
- 解析HTML内容：
  - 使用`BeautifulSoup`提取目标数据
  - XPath选择器应用
- 反爬机制应对：
  - 设置随机User-Agent
  - 添加访问延迟（time.sleep）
  - 使用代理IP池

### 2. 数据可视化基础
- Matplotlib核心组件：
  ```python
  import matplotlib.pyplot as plt
  plt.plot(x,y)
  plt.show()
  
    ```python

  fig, axes = plt.subplots(2, 2, figsize=(10,8))
  axes[0,0].plot(x1, y1)  # 左上子图
  axes[0,1].bar(x2, y2)   # 右上子图
  axes[1,0].scatter(x3, y3) # 左下子图
  axes[1,1].pie(sizes)    # 右下子图