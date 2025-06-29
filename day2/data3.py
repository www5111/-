import os
import re


def natural_sort_key(s):
    """
    生成自然排序键（和Windows资源管理器相同的排序方式）
    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]


def batch_rename_images(txt_file, image_folder, image_ext='.jpg'):
    """
    严格按照Windows资源管理器顺序重命名图片

    参数:
        txt_file: 包含新文件名的文本文件路径
        image_folder: 图片文件夹路径
        image_ext: 图片扩展名(如.jpg, .png等)
    """
    # 验证路径
    if not os.path.exists(image_folder):
        print(f"错误：图片文件夹不存在 - {image_folder}")
        return
    if not os.path.exists(txt_file):
        print(f"错误：文本文件不存在 - {txt_file}")
        return

    # 读取新文件名（保留原始顺序）
    with open(txt_file, 'r', encoding='utf-8') as f:
        new_names = [line.strip() for line in f if line.strip()]

    # 获取文件夹中所有图片文件（按Windows资源管理器顺序排序）
    all_images = [f for f in os.listdir(image_folder)
                  if f.lower().endswith(image_ext.lower())]

    # 使用自然排序（和Windows相同的排序方式）
    all_images.sort(key=natural_sort_key)

    # 检查数量是否匹配
    if len(new_names) != len(all_images):
        print(f"错误: 文件名数量({len(new_names)})与图片数量({len(all_images)})不匹配")
        print("请确保:")
        print("1. 文本文件每行一个名称")
        print("2. 文件夹中只有需要重命名的图片")
        return

    # 批量重命名
    success = 0
    for old_name, new_name in zip(all_images, new_names):
        # 构建路径
        old_path = os.path.join(image_folder, old_name)
        new_base = new_name.split('.')[0]  # 移除可能存在的扩展名
        new_path = os.path.join(image_folder, f"{new_base}{image_ext}")

        # 处理文件名冲突
        counter = 1
        while os.path.exists(new_path):
            new_path = os.path.join(image_folder, f"{new_base}_{counter}{image_ext}")
            counter += 1

        # 执行重命名
        try:
            os.rename(old_path, new_path)
            print(f"重命名: {old_name} -> {os.path.basename(new_path)}")
            success += 1
        except Exception as e:
            print(f"重命名失败 {old_name}: {str(e)}")

    print(f"\n完成! 成功重命名 {success}/{len(new_names)} 个文件")


if __name__ == "__main__":
    # 配置参数（修改为您的实际路径）
    text_file = r"C:\Users\武怡聪\OneDrive\桌面\新建文本文档.txt"  # 包含新文件名的文本文件
    image_dir = r"C:\\Users\\武怡聪\\PycharmProjects\\pythonProject6\\day2\\1"  # 图片所在文件夹路径
    extension = ".png"  # 图片扩展名

    # 使用绝对路径更可靠
    script_dir = os.path.dirname(os.path.abspath(__file__))
    text_file = os.path.join(script_dir, text_file)
    image_dir = os.path.join(script_dir, image_dir)

    # 执行批量重命名
    batch_rename_images(text_file, image_dir, extension)