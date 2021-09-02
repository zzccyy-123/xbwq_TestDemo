import os

from Test_case.test_case_report import *
from Test_case.test_case_login import *
import HTMLTestReportCN

# 创建一个测试套件 == list
suite = unittest.TestSuite()

# 选择性添加测试用例（子元素）到测试套件（集合）

# 很坑，使用ddt后，测试用例名后会生成一个编号，故测试用例名发生了改变
# suite.addTest(TestCaseLogin('test_login_00001'))
# 批量运行第一种方法：
# suite.addTest(TestCaseReport('test_2_weekReport'))
# suite.addTest(TestCaseReport('test_3_monReport'))
# 批量运行第二种方法：
# case = [TestCaseReport('test_dayReport_1'), TestCaseReport('test_dayReport_2'), TestCaseReport('test_dayReport_3'),
#         TestCaseReport('test_dayReport_4')]
# suite.addTests(case)
# 批量运行第三种方法：
# test_dir = './Test_case/'
# suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_case_*.py')
# 批量运行第四种方法：
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCaseReport))
# suite.addTest(unittest.TestLoader().loadTestsFromName('Test_case.test_case_report'))

# 实例
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCaseLogin))
case = [TestCaseReport('test_dayReport_1'), TestCaseReport('test_dayReport_2'), TestCaseReport('test_dayReport_3'),
        TestCaseReport('test_dayReport_4')]
suite.addTests(case)

if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
with open(report_path + report_file, 'wb') as report:
    runner = HTMLTestReportCN.HTMLTestRunner(stream=report, title=report_title, description=report_describe,
                                             tester=report_user)
    runner.run(suite)
