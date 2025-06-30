import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import os


def get_scholar_bibtex(search_query):
    """
    获取Google Scholar文章的BibTeX引用

    参数:
        search_query (str): 要搜索的文章标题或查询字符串

    返回:
        str: BibTeX引用内容，如果失败则返回None
    """
    # 配置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # 最大化窗口
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # 设置日志级别只显示错误
    os.environ['WDM_LOG_LEVEL'] = '0'

    try:
        # 自动下载和管理ChromeDriver
        service = Service(ChromeDriverManager().install())

        # 初始化浏览器
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # 设置隐式等待时间
        driver.implicitly_wait(10)

        # 打开Google Scholar
        print("正在访问Google Scholar...")
        driver.get("https://scholar.google.com")
        time.sleep(2)  # 等待页面加载

        # 切换到中文界面（如果不在中文界面）
        try:
            lang_switch = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "中文"))
            )
            lang_switch.click()
            time.sleep(1)
        except:
            print("已经是中文界面或找不到语言切换选项")

        # 输入搜索词
        print(f"正在搜索: {search_query}")
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.clear()

        # 模拟人类输入速度
        for char in search_query:
            search_box.send_keys(char)
            time.sleep(0.1)  # 减慢输入速度

        time.sleep(1)

        # 提交搜索
        search_box.send_keys(Keys.RETURN)
        print("正在等待搜索结果...")
        time.sleep(3)  # 等待搜索结果

        # 定位到第一篇文章的引用按钮（不点击文章标题）
        try:
            # 找到第一个搜索结果条目
            first_result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.gs_ri"))
            )

            # 在结果条目中找到"引用"按钮
            cite_button = first_result.find_element(By.CSS_SELECTOR, "a.gs_or_cit")
            article_title = first_result.find_element(By.CSS_SELECTOR, "h3.gs_rt").text
            print(f"找到文章: {article_title}")

            # 点击引用按钮
            print("正在点击引用按钮...")
            cite_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"未找到匹配的文章或引用按钮: {str(e)}")
            return None

        # 选择BibTeX格式
        try:
            bibtex_option = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "BibTeX"))
            )
            print("正在选择BibTeX格式...")
            bibtex_option.click()
            time.sleep(2)
        except Exception as e:
            print(f"找不到BibTeX选项: {str(e)}")
            return None

        # 获取BibTeX内容
        try:
            bibtex_content = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "pre"))
            ).text
            print("\n成功获取BibTeX引用:")
            print(bibtex_content)

            # 复制到剪贴板
            try:
                pyperclip.copy(bibtex_content)
                print("\nBibTeX引用已复制到剪贴板")
            except:
                print("\n无法复制到剪贴板，请手动复制")

            return bibtex_content
        except Exception as e:
            print(f"无法获取BibTeX内容: {str(e)}")
            return None

    except Exception as e:
        print(f"发生错误: {str(e)}")
        return None
    finally:
        # 关闭浏览器
        if 'driver' in locals():
            driver.quit()
            print("浏览器已关闭")


def process_multiple_articles(article_list):
    """
    处理多篇文章的BibTeX引用获取

    参数:
        article_list (list): 包含多篇文章标题的列表
    """
    results = {}

    for article in article_list:
        print(f"\n{'=' * 50}")
        print(f"正在处理文章: {article}")
        print(f"{'=' * 50}")

        bibtex = get_scholar_bibtex(article)
        if bibtex:
            results[article] = bibtex
        else:
            results[article] = "未能获取BibTeX引用"

        # 为了避免被Google封禁，添加延迟
        time.sleep(5)

    # 打印所有结果
    print("\n\n所有文章处理完成:")
    print("=" * 60)
    for article, bibtex in results.items():
        print(f"\n文章: {article}")
        print("-" * 60)
        print(bibtex)
        print("=" * 60)

    return results


# 要搜索的文章列表
article_list = [
    "Automatic crater detection and age estimation for mare regions on the lunar surface,",
    "The origin of planetary impactors in the inner solar system,",
    "Deep learning based systems for crater detection: A review,",
    "A preliminary study of classification method on lunar topography and landforms,",
    "The CosmoQuest Moon mappers community science project: The effect of incidence angle on the Lunar surface crater distribution,",
    "Fast r-cnn,",
    "You only look once: Unified, real-time object detection,",
    "Attention is all you need,",
    "End-to-end object detection with transformers,"
]

# 使用示例
if __name__ == "__main__":
    all_results = process_multiple_articles(article_list)