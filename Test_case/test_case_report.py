import unittest
from Page_object.login_page import *
from Page_object.index_dayReport_page import *
from Page_object.index_weekReport_page import *
from Page_object.index_monReport_page import *
from selenium import webdriver
from ddt import ddt

# 测试用例的设计
"""讲道理这里应该不会用到ddt装饰，但是不用ddt装饰的话，tearDownClass中的driver会标记警告。虽然对代码执行无任何影响。"""


@ddt
class TestCaseReport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(login_url)
        LoginPage(cls.driver).login(company='cms', account='boss', password='aaaaaa')
        time.sleep(1)
        global day_testdata, week_testdata, mon_testdata
        # 不知道这里为什么只认绝对路径？？？明明在同级文件下用相对路径也是可以的啊！！！！！！
        day_testdata = cls.open_datafile(
            'C:\\Users\\Administrator\\Desktop\\unittestWq\\Test_data\\data_dayReport.json')
        week_testdata = cls.open_datafile(
            'C:\\Users\\Administrator\\Desktop\\unittestWq\\Test_data\\data_weekReport.json')
        mon_testdata = cls.open_datafile(
            'C:\\Users\\Administrator\\Desktop\\unittestWq\\Test_data\\data_monReport.json')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @staticmethod
    def open_datafile(path):
        with open(path, 'r', encoding='utf-8') as f:
            kwargs = json.load(f)
        return kwargs

    def test_dayReport_1(self):
        """完整数据(非日期重复)"""
        # 获取上报前的总条数
        initial_num = IndexDayReportPage(self.driver).get_totlenum()
        # 执行上报操作
        IndexDayReportPage(self.driver).day_report(day_testdata.get('data1'))
        # 获取上报后的总条数
        result_num = IndexDayReportPage(self.driver).get_totlenum()
        # 计算差值
        real_message = result_num - initial_num
        expect_message = 1
        self.assertEqual(real_message, expect_message, msg='上报失败')

    def test_dayReport_2(self):
        """验证日期非(必)填"""
        real_message = IndexDayReportPage(self.driver).day_report(day_testdata.get('data2'))
        expect_message = '日期 不能为空'
        self.assertEqual(real_message, expect_message, msg='报错信息有误')

    def test_dayReport_3(self):
        """验证本日总结非(必)填"""
        real_message = IndexDayReportPage(self.driver).day_report(day_testdata.get('data3'))
        expect_message = '本日总结 不能为空'
        self.assertEqual(real_message, expect_message, msg='报错信息有误')

    def test_dayReport_4(self):
        """验证电话格式"""
        real_message = IndexDayReportPage(self.driver).day_report(day_testdata.get('data4'))
        expect_message = '电话 格式错误'
        self.assertEqual(real_message, expect_message, msg='报错信息有误')

    def test_dayReport_5(self):
        """验证上报日期"""
        real_message = IndexDayReportPage(self.driver).day_report(day_testdata.get('data5'))
        expect_message = '不允许上报还未到的日期！'
        self.assertEqual(real_message, expect_message, msg='报错信息有误')

    def test_dayReport_6(self):
        """上报重复数据"""
        real_message = IndexDayReportPage(self.driver).day_report(day_testdata.get('data5'))
        expect_message = '该日期的工作上报记录已经存在了！'
        self.assertEqual(real_message, expect_message, msg='报错信息有误')


    def test_weekReport(self):
        real_message = IndexWeekReportPage(self.driver).week_report(week_testdata)
        # 缺少断言

    def test_monReport(self):
        real_message = IndexMonReportPage(self.driver).mon_report(mon_testdata)
        # 缺少断言


if __name__ == '__main__':
    unittest.main()
