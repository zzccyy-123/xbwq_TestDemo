'''
    BasePage类是POM中的基类，主要用于提供常用的函数，为页面对象类进行服务。
    Selenium常用函数：
        元素定位
        输入
        点击
        访问url
        等待
        关闭
'''
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):

    # 构造函数
    def __init__(self, driver):
        self.driver = driver
        # 必须全屏，否则会出现部分元素无法交互的问题
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # 访问url
    def visit(self, url):
        self.driver.get(url)

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_s(self, loc, txt):
        try:
            self.driver.find_element(*loc)
        except NoSuchElementException:
            return False
        if txt:
            self.locator(loc).send_keys(txt)
        else:
            pass

    # 点击
    def clike_s(self, loc):
        try:
            self.driver.find_element(*loc)
        except NoSuchElementException:
            return False
        self.locator(loc).click()

    # 关闭
    # 切换iframe
    def switch_iframe(self, loc):
        self.driver.switch_to.frame(self.locator(loc))

    # 切换回上级iframe
    def switch_iframe_parent(self):
        self.driver.switch_to.parent_frame()

    # 获取文本信息
    def get_message(self, loc):
        try:
            self.driver.find_element(*loc)
        except NoSuchElementException:
            return False
        return self.locator(loc).text

    # 日期格式处理
    @staticmethod
    def date_format(date):
        year = str(date.split(',')[0])
        month = date.split(',')[1]
        if int(month) < 10:
            month = '0' + month
        day = date.split(',')[2]
        if int(day) < 10:
            day = '0' + day
        new_date = year + '-' + str(month) + '-' + str(day)
        return new_date
