# AutoPatchPro
个人pytest+selenium+yaml自动化测试项目

项目结构

```
AutoPatchPro/
│
├── tests/                    # 测试用例目录
│   ├── test_login.py          # 示例测试文件
│   ├── test_search.py         # 其他测试文件
│   └── __init__.py            # 使其成为一个包
│
├── pages/                    # 页面对象模式 (POM) 的页面类
│   ├── login_page.py          # 登录页面类
|   ├── dashboard_page.py       # 仪表盘页面的对象类
│   ├── search_page.py         # 搜索页面类
│   └── __init__.py            # 使其成为一个包
│
├── config/                   # 配置文件目录
│   └── config.yaml            # 主配置文件（例如URL，用户名，密码等）
│
├── data/                     # 测试数据目录
│   └── test_data.yaml         # 测试数据
│
├── utils/                    # 公共方法和工具函数
│   ├── webdriver_manager.py   # 浏览器驱动的管理
│   ├── logger.py              # 日志工具
│   └── __init__.py            # 使其成为一个包
│
├── fixtures/                 # pytest fixtures 目录
│   ├── browser.py             # 浏览器的fixture
│   └── __init__.py            # 使其成为一个包
│
├── reports/                  # 测试报告存放目录
│   └── pytest_report.html     # pytest生成的测试报告
│
├── logs/                     # 日志文件目录
│   └── test_run.log           # 测试运行日志
│
├── drivers/                  # 浏览器驱动目录
│   └── chromedriver           # Chrome浏览器驱动
│
├── conftest.py               # pytest的全局配置和钩子
├── pytest.ini                # pytest的配置文件
├── requirements.txt          # 项目依赖的包列表
└── README.md                 # 项目说明文件

```

/page/login_page.py示例

```py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # 页面元素定位
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'loginButton')

    # 页面上的操作方法
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

```

如果你的项目比较复杂，你可以创建一些辅助类或模块来分担页面的部分功能，例如创建 `BasePage` 基类，所有其他页面类继承它以共享常用功能。

**示例 `base_page.py`**：

```py
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        self.driver.get(url)
```

然后每个具体页面类可以继承 `BasePage`，简化代码：

```py
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'loginButton')
```
