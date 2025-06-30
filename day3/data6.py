import os
import requests
from lxml import etree
from urllib.parse import urljoin
import time


def scrape_bian_pics_to_desktop():
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://pic.netbian.com/'
    }

    # 目标URL
    base_url = 'https://pic.netbian.com/'

    # 获取桌面路径并创建保存目录
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    save_dir = os.path.join(desktop_path, '彼岸桌面图片')

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"已创建保存目录: {save_dir}")

    try:
        # 发送HTTP请求
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功

        # 使用lxml解析HTML
        html = etree.HTML(response.content.decode('gbk'))  # 该网站使用gbk编码

        # 修正后的XPath选择器 - 获取所有图片链接
        pic_links = html.xpath('//div[@class="slist"]//li/a/@href')

        if not pic_links:
            print("未找到图片链接，请检查XPath选择器或网站结构是否变化")
            return

        # 遍历图片链接并下载
        for i, link in enumerate(pic_links[:10], 1):  # 只下载前10张
            try:
                # 构建完整图片详情页URL
                detail_url = urljoin(base_url, link)

                # 访问图片详情页获取大图
                detail_resp = requests.get(detail_url, headers=headers)
                detail_resp.encoding = 'gbk'
                detail_html = etree.HTML(detail_resp.text)

                # 获取大图URL
                img_src = detail_html.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
                img_url = urljoin(base_url, img_src)

                # 获取图片名称
                img_name = detail_html.xpath('//div[@class="photo-hd"]/h1/text()')[0].strip() + '.jpg'

                # 清理文件名
                img_name = "".join(c for c in img_name if c.isalnum() or c in (' ', '.', '_')).rstrip()

                # 下载图片
                print(f"正在下载第 {i} 张: {img_name}")
                img_data = requests.get(img_url, headers=headers).content

                # 保存图片到桌面
                save_path = os.path.join(save_dir, img_name)
                with open(save_path, 'wb') as f:
                    f.write(img_data)
                    print(f"已保存到: {save_path}")

                # 添加延迟，避免请求过于频繁
                time.sleep(1)

            except Exception as e:
                print(f"下载第 {i} 张图片时出错: {e}")
                continue

        print(f"\n所有图片已下载完成！保存位置: {save_dir}")

    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
    except Exception as e:
        print(f"发生错误: {e}")


scrape_bian_pics_to_desktop()