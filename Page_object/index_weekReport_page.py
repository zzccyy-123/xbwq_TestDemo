'''
    index_weekReport_page页面对象，实现首页中新增周报报的流程
'''
import json
import time

from Base.base_page import BasePage
from config import *
from selenium.webdriver.common.by import By
from selenium import webdriver


class IndexWeekReportPage(BasePage):
    """核心元素"""
    # 页面链接
    url = index_url
    # 工作汇报
    gzhb_button = (By.XPATH, '/html/body/div[1]/div[2]/div/ul/li[13]/a')
    # 周报管理
    zbgl_button = (By.XPATH, '/html/body/div[1]/div[2]/div/ul/li[13]/div/a[2]')
    # 新增日报
    xzzb_button = (By.XPATH, '//a[@data-title="新增周报"]')
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

    """核心流程"""

    def week_report(self, kwargs):
        # 登录（测试用）
        # self.visit('http://cms.xiaobuwq.com/wq/admin/core/login/index')
        # self.input_s((By.ID,'company'),'cms')
        # self.input_s((By.ID,'account'),'boss')
        # self.input_s((By.ID,'pass'),'aaaaaa')
        # self.clike_s((By.XPATH,'//button[@type="submit"]'))
        # time.sleep(2)

        self.visit(self.url)
        # 进入新增日报页面
        self.clike_s(self.gzhb_button)
        self.clike_s(self.zbgl_button)
        self.clike_s(self.xzzb_button)
        # 填写日期
        self.clike_s(self.rq_button)
        self.switch_iframe(self.iframe_element)
        rq1_clike = (By.XPATH,'//td[@onclick="day_Click({});"]'.format(kwargs.get('date1')))
        self.clike_s(rq1_clike)
        self.switch_iframe_parent()
        time.sleep(3)
        # 填写总结
        self.input_s(self.zj_button, kwargs.get('summary'))
        # 填写照片
        self.input_s(self.zp_button, kwargs.get('picPath1'))
        # 填写单行
        self.input_s(self.danh_button, kwargs.get('singleInput'))
        # 填写多行
        self.input_s(self.duoh_button, kwargs.get('MultipleInput'))
        # 填写数字
        self.input_s(self.sz_button, kwargs.get('number'))
        # 填写电话
        self.input_s(self.dh_button, kwargs.get('phoneNumber'))
        # 填写金额
        self.input_s(self.je_button, kwargs.get('money'))
        # 填写单选
        self.clike_s(self.danx_button)
        danx_option = (By.XPATH, '//option[text()="{}"]'.format(kwargs.get('option')))
        self.clike_s(danx_option)
        # 填写多选
        self.clike_s(self.duox_button)
        options = kwargs.get('options').split(',')
        for item in options:
            duox_option = (By.XPATH, '//span[text()="{}"]//..//i'.format(item))
            self.clike_s(duox_option)
        self.clike_s(self.duox_button)
        # 填写日期1
        self.clike_s(self.rq1_button)
        self.switch_iframe(self.iframe_element)
        rq2_clike = (By.XPATH,'//td[@onclick="day_Click({});"]'.format(kwargs.get('date2')))
        self.clike_s(rq2_clike)
        self.switch_iframe_parent()
        # 填写时间
        self.clike_s(self.sj_button)
        self.switch_iframe(self.iframe_element)
        rq3_clike = (By.XPATH,'//td[@onclick="day_Click({});"]'.format(kwargs.get('date3')))
        self.clike_s(rq3_clike)
        self.clike_s(rq3_clike)
        self.switch_iframe_parent()
        # 填写开始时间
        self.clike_s(self.kssj_button)
        self.switch_iframe(self.iframe_element)
        rq4_clike = (By.XPATH,'//td[@onclick="day_Click({});"]'.format(kwargs.get('startTime')))
        self.clike_s(rq4_clike)
        self.clike_s(rq4_clike)
        self.switch_iframe_parent()
        # 填写结束时间
        self.clike_s(self.jssj_button)
        self.switch_iframe(self.iframe_element)
        rq5_clike = (By.XPATH, '//td[@onclick="day_Click({});"]'.format(kwargs.get('endTime')))
        self.clike_s(rq5_clike)
        self.clike_s(rq5_clike)
        self.switch_iframe_parent()
        # 填写照片1
        self.input_s(self.zp1_button, kwargs.get('picPath2'))
        # 填写图文
        self.input_s(self.tw_button, kwargs.get('picPath3'))
        # 填写备注
        self.input_s(self.bz_button, kwargs.get('remarks'))
        # 此处不sleep会出事
        time.sleep(1)
        # 提交
        self.clike_s(self.tj_button)


if __name__ == '__main__':
    with open('../Test_data/data_weekReport.json', 'r', encoding='utf-8') as fp:
        kwargs = json.load(fp)
    driver = webdriver.Chrome()
    IndexWeekReportPage(driver).week_report(**kwargs)

