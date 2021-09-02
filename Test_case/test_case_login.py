import unittest
from Page_object.login_page import *
from selenium.webdriver import ChromeOptions
from Page_object.index_dayReport_page import *
from ddt import ddt, file_data


# 测试用例的设计
@ddt
class TestCaseLogin(unittest.TestCase):
    # 前置条件
    def setUp(self):
        # 设置无窗口运行
        self.opt = ChromeOptions()
        self.opt.headless = True
        self.driver = webdriver.Chrome(options=self.opt)

    # 后置条件
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    @file_data('../Test_data/data_login.yml')
    def test_login(self, company, account, password):
        LoginPage(self.driver).login(company, account, password)
        time.sleep(1)
        self.assertEqual(self.driver.current_url, index_url, msg='未成功跳转到首页')


if __name__ == '__main__':
    unittest.main()
