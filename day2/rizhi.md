# 实训日志

## 基本信息
- **日期**：2025年6月29日  
- **主要内容**：
  - NumPy图像处理技术实践
  - 文件排序问题分析与解决

## 学习内容

### 1. NumPy图像处理实践
- 使用`numpy.array`将遥感图像转换为矩阵
- 通过数组运算实现图像增强：
  - 对比度拉伸
  - 数据归一化处理
- 结合`matplotlib`进行可视化对比
- 学习收获：
  - 理解了NumPy向量化运算的优势
  - 掌握了基本的图像增强方法

### 2. 文件排序问题
- 发现问题：
  - Windows自然排序（img1, img2,...,img10）
  - Python默认ASCII排序（img1, img10, img2）
- 解决方案：
  ```python
  sorted(files, key=lambda x: int(x[3:-4]))