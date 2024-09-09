import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    """
    初始化Chrome浏览器驱动driver
    @param: None
    @return: driver
    """

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")  # 启用隐私模式

    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()  # 最大化浏览器窗口
    yield driver  # 每次调用都先关闭driver并返回一个新的driver实例

    # 测试结束后，关闭浏览器
    driver.quit()
