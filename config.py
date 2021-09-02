import time

login_url = 'http://cms.xiaobuwq.com/wq/admin/core/login/index'
index_url = 'http://cms.xiaobuwq.com/wq/admin/core/index/index'

"""测试报告相关配置"""
report_name = '测试报告名称'
report_title = '测试报告标题'
report_describe = '测试报告描述'
report_path = './report/'
report_file = str(int(time.time())) + '.html'
report_user = '谁谁谁'
