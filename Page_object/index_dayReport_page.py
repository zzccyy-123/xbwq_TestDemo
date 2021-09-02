'''
    index_page页面对象，实现首页中新增日报的流程
'''
import time, json

from Base.base_page import BasePage
from config import *
from selenium.webdriver.common.by import By
from selenium import webdriver


class IndexDayReportPage(BasePage):
    """核心元素"""
    # 页面链接
    url = index_url
    # 工作汇报
    gzhb_button = (By.XPATH, '/html/body/div[1]/div[2]/div/ul/li[13]/a')
    # 日报管理
    rbgl_button = (By.XPATH, '/html/body/div[1]/div[2]/div/ul/li[13]/div/a[1]')
    # 新增日报
    xzrb_button = (By.XPATH, '//a[@data-title="新增日报"]')
    # 日期
    rq_button = (By.XPATH, '//input[@placeholder="日期"]')
    # 总结
    zj_button = (By.XPATH, '//textarea[contains(@id,"summary")]')
    # 照片
    zp_button = (By.XPATH, '//span[@id="s_pics_input_selpic"]//input')
    # 单行
    danh_button = (By.XPATH, '//input[@placeholder="单行"]')
    # 多行
    duoh_button = (By.XPATH, '//textarea[@data-label="多行"]')
    # 数字
    sz_button = (By.XPATH, '//input[@placeholder="数字"]')
    # 电话
    dh_button = (By.XPATH, '//input[@placeholder="电话"]')
    # 金额
    je_button = (By.XPATH, '//input[@placeholder="金额"]')

    # 单选
    danx_button = (By.XPATH, '//select[@data-label="单选"]')

    # 多选
    duox_button = (By.XPATH, '//span[text()="多选："]//..//..//div')

    # 日期1
    rq1_button = (By.XPATH, '//input[@placeholder="日期1"]')
    # 时间
    sj_button = (By.XPATH, '//input[@placeholder="时间"]')
    # 开始时间
    kssj_button = (By.XPATH, '//input[@placeholder="时间起止开始"]')
    # 结束时间
    jssj_button = (By.XPATH, '//input[@placeholder="时间起止结束"]')
    # 照片1
    zp1_button = (By.XPATH, '//div[contains(@class,"only_pic_input_class")][2]//div//div//div//div[2]//input')
    # 图文
    tw_button = (By.XPATH, '//div[contains(@class,"only_pic_input_class")][3]//div//div//div//div[2]//input')
    # 备注
    bz_button = (By.XPATH, '//textarea[contains(@name,"text")]')
    # 提交
    tj_button = (By.XPATH, '//button[text()="确定"]')
    # iframe
    iframe_element = (By.XPATH, '//iframe')
    # 错误信息
    error_msg = (By.XPATH, '//div[@class="tip_widget_text"]')
    # 确认删除
    final_delete = (By.XPATH, '//button[text()="确定"]')
    # 关闭按钮
    close_button = (By.XPATH, '//div[text()="×"]')
    # 总数
    totle_num = (By.XPATH, '//div[@class="summary"]')

    """核心流程"""

    def initialize(self):
        # 登录（测试用）
        # self.visit('http://cms.xiaobuwq.com/wq/admin/core/login/index')
        # self.input_s((By.ID, 'company'), 'cms')
        # self.input_s((By.ID, 'account'), 'boss')
        # self.input_s((By.ID, 'pass'), 'aaaaaa')
        # self.clike_s((By.XPATH, '//button[@type="submit"]'))
        # time.sleep(1)

        self.visit(self.url)
        # 进入日报管理页
        self.clike_s(self.gzhb_button)
        self.clike_s(self.rbgl_button)

    # 上报
    def day_report(self, kwargs):
        # 进入日报管理页
        self.initialize()
        # 进入新增日报页面
        self.clike_s(self.xzrb_button)
        # 填写日期
        self.clike_s(self.rq_button)
        self.switch_iframe(self.iframe_element)
        rq1_clike = (By.XPATH, '//td[@onclick="day_Click({});"]'.format(kwargs.get('date1')))
        self.clike_s(rq1_clike)
        self.switch_iframe_parent()
        time.sleep(1)
        # 填写总结
        if kwargs.get('summary'):
            self.input_s(self.zj_button, kwargs.get('summary'))
        # 填写照片
        if kwargs.get('picPath1'):
            self.input_s(self.zp_button, kwargs.get('picPath1'))
        # 填写单行
        if kwargs.get('singleInput'):
            self.input_s(self.danh_button, kwargs.get('singleInput'))
        # 填写多行
        if kwargs.get('MultipleInput'):
            self.input_s(self.duoh_button, kwargs.get('MultipleInput'))
        #
        if kwargs.get('number'):
            self.input_s(self.sz_button, kwargs.get('number'))
        # 填写电话
        if kwargs.get('phoneNumber'):
            self.input_s(self.dh_button, kwargs.get('phoneNumber'))
        # 填写金额
        if kwargs.get('money'):
            self.input_s(self.je_button, kwargs.get('money'))
        # 填写单选
        if kwargs.get('option'):
            self.clike_s(self.danx_button)
            danx_option = (By.XPATH, '//option[text()="{}"]'.format(kwargs.get('option')))
            self.clike_s(danx_option)
        # 填写多选
        if kwargs.get('options'):
            if self.clike_s(self.duox_button) is not False:
                options = kwargs.get('options').split(',')
                for item in options:
                    duox_option = (By.XPATH, '//span[text()="{}"]//..//i'.format(item))
                    self.clike_s(duox_option)
                self.clike_s(self.duox_button)
        # 填写日期1
        if kwargs.get('date2'):
            self.clike_s(self.rq1_button)
            self.switch_iframe(self.iframe_element)
            rq2_clike = (By.XPATH, '//td[@onclick="day_Click({});"]'.format(kwargs.get('date2')))
            self.clike_s(rq2_clike)
            self.switch_iframe_parent()
        # 填写时间
        if kwargs.get('date3'):
            self.clike_s(self.sj_button)
            self.switch_iframe(self.iframe_element)
            rq3_clike = (By.XPATH, '//td[@onclick="day_Click({});"]'.format(kwargs.get('date3')))
            self.clike_s(rq3_clike)
            # 当传入时间与默认时间（当日）一致时，则不需要再次点击
            # self.clike_s(rq3_clike)
            self.switch_iframe_parent()
        # 填写开始时间
        if kwargs.get('startTime'):
            self.clike_s(self.kssj_button)
            self.switch_iframe(self.iframe_element)
            rq4_clike = (By.XPATH, '//td[@onclick="day_Click({});"]'.format(kwargs.get('startTime')))
            self.clike_s(rq4_clike)
            # 当开始时间与默认时间（当天）一致时，则不需要再次点击
            # self.clike_s(rq4_clike)
            self.switch_iframe_parent()
        # 填写结束时间
        if kwargs.get('endTime'):
            self.clike_s(self.jssj_button)
            self.switch_iframe(self.iframe_element)
            rq5_clike = (By.XPATH, '//td[@onclick="day_Click({});"]'.format(kwargs.get('endTime')))
            self.clike_s(rq5_clike)
            # 当结束时间与开始时间一致时，则不需要再次点击
            # self.clike_s(rq5_clike)
            self.switch_iframe_parent()
        # 填写照片1
        if kwargs.get('picPath2'):
            self.input_s(self.zp1_button, kwargs.get('picPath2'))
        # 填写图文
        if kwargs.get('picPath3'):
            self.input_s(self.tw_button, kwargs.get('picPath3'))
        # 填写备注
        if kwargs.get('remarks'):
            self.input_s(self.bz_button, kwargs.get('remarks'))
        # 此处不sleep会出事
        time.sleep(1)
        # 提交
        self.clike_s(self.tj_button)
        time.sleep(1)
        # 如果已有此记录，则删除后重新上报
        # if self.get_message(self.error_msg) == '该日期的工作上报记录已经存在了！':
        #     self.clike_s(self.close_button)
        #     time.sleep(1)
        #     new_date = self.date_format(kwargs.get('date1'))
        #     self.day_delete(new_date)
        #     self.day_report(kwargs)
        return self.get_message(self.error_msg)

    # 删除
    def day_delete(self, kwargs):
        # 进入日报管理页
        self.initialize()
        new_date = self.date_format(kwargs.get('date1'))
        self.clike_s(
            (By.XPATH,
             '//td[contains(text(),"{}")]/../td[@class="table_op_td"]/a[@data-content="确认删除？"]'.format(new_date)))
        time.sleep(1)
        self.clike_s(self.final_delete)

    # 获取总条数
    def get_totlenum(self):
        # 进入日报管理页
        self.initialize()
        num = self.get_message(self.totle_num)
        num = num.replace('共', '')
        num = num.replace('条', '')
        num = num.replace(' ', '')
        return int(num)


if __name__ == '__main__':
    # kwargs = {
    #     'summary': '我是总结啊',
    #     'date1': '2021,8,21',
    #     'picPath1': 'C:\\Users\\Administrator\\Desktop\\2.jpg',
    #     'singleInput': '单行输入',
    #     'MultipleInput': '多行输入',
    #     'number': '56',
    #     'phoneNumber': '13112345678',
    #     'money': '',
    #     'option': '',
    #     'options': '多选1，多选2',
    #     'date2': '2021,8,21',
    #     'date3': '2021,8,22',
    #     'startTime': '2021,8,8',
    #     'endTime': '2021,8,12',
    #     'picPath2': 'C:\\Users\\Administrator\\Desktop\\3.jpg',
    #     'picPath3': 'C:\\Users\\Administrator\\Desktop\\4.jpg',
    #     'remarks': 'selenium测试'
    # }
    with open('../Test_data/data_dayReport.json', 'r', encoding='utf-8') as fp:
        kwargs = json.load(fp)
    driver = webdriver.Chrome()
    testnum = IndexDayReportPage(driver).get_totlenum()
    print(type(testnum))
    print(testnum)
