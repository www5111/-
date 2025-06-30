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
        print("\n未能获取BibTeX引用")