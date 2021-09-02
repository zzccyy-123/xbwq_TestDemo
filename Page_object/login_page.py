'''
    LoginPage类，专门用于实现登录页面对象的文件。
    主体内容包含：
        1.核心的页面元素
            账号、密码、登录按钮
        2.核心的业务流
            用户的登录行为
'''
from selenium.webdriver.common.by import By

from Base.base_page import *
from config import *

from selenium import webdriver


class LoginPage(BasePage):
    # 核心元素
    url = login_url
    company = (By.ID, 'company')
    user = (By.ID, 'account')
    password = (By.ID, 'pass')
    login_button = (By.XPATH, '//button[@type="submit"]')

    # 核心业务流
    def login(self, company, account, password):
        self.visit(self.url)
        self.input_s(self.company, company)
        self.input_s(self.user, account)
        self.input_s(self.password, password)
        self.clike_s(self.login_button)


# 调试代码
if __name__ == '__main__':
    driver = webdriver.Chrome()
    LoginPage(driver).login('cms', 'boss', 'aaaaaa')
