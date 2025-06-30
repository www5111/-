import requests
from bs4 import BeautifulSoup


def scrape_douban_top10():
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # 目标URL
    url = 'https://movie.douban.com/top250'

    try:
        # 发送HTTP请求
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找所有电影标题
        movie_items = soup.find_all('div', class_='hd')[:10]  # 只取前10个

        # 提取电影名称
        movies = []
        for item in movie_items:
            title = item.a.span.text.strip()
            movies.append(title)

        # 打印结果
        print("豆瓣电影Top10:")
        for i, movie in enumerate(movies, 1):
            print(f"{i}. {movie}")

        return movies

    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None


# 执行爬取
scrape_douban_top10()