# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#首先要引入unittest框架包。

class BaiduTest(unittest.TestCase):
    '''Baidu 类继承 unittest.TestCase 类，从 TestCase 类继承是告诉 unittest 模块的方式，这是一个测试案例。'''
    
    def setUp(self):
        '''
        setUp用于设置初始化工作，在每一个测试用例前先被执行，它与 
        tearDown 方法相呼应，后者在每一个测试用例执行后被执行。这里的初始化工作定义了浏览器启动和基础 URL 地址。
        implicitly_wait()在前面章节已经学过，它用于设置整个页面元素的隐性等待，30 秒。接下来定义空的
        verificationErrors 数组，脚本运行时的错误信息将被打印到这个数组中。定义 
        accept_next_alert 变量，表示是否继续接受下一个警告，初始化状态为 Ture。
        '''
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_baidu(self):
        '''测试脚本'''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium ide")
        driver.find_element_by_id("su").click()
        
    def is_element_present(self, how, what):
        '''
        is_element_present方法用来查找页面元素是否存在，通过 
        find_element()来接收元素的定位方法（how）和定位值（what），如果定位到元素返回 
        Ture,否则出现异常并返回 Flase。try...except....为
        Python的异常处理。
        '''
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True
    
    def is_alert_present(self):
        '''
        is_alert_present()方法用来处理弹出的警告框，用 WebDriver 所提供的 
        switch_to_alert()方法来捕捉警告框。如果捕捉到警告框返回 Ture，否则异常，返回 Flase。
        '''
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException, e:
            return False
        return True
    
    def close_alert_and_get_its_text(self):
        '''
        close_alert_and_get_its_text()关闭警告并且获得警告信息。首先通过 
        switch_to_alert()获得警告，通过.text 获得警告框信息。接着通过 if 语句判断 
        accept_next_alert 的状态，在 setUp()已经初始化状态为 Ture，如果为 Ture，通过 
        accept()接受警告。否则 dismiss()忽略此警告。
        '''
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
            
    def tearDown(self):
        '''
        tearDown 方法在每个测试方法执行后调用，这个方法用于完成测试用例执行后的清理工作，如退出浏览器、关闭驱动，恢复用例执行状态等。在 
        setUp()方法中定义了 verificationErrors 为空数组，这里通过 
        assertEqual()比较其是否为空，如果为空说明用例执行的过程过程中没有出现异常，否则将抛出 AssertionError 异常。
        '''
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    '''整个测试过程集成在 unitest.main()模块中，其默认执行以 test 开头的方法。'''
    unittest.main()
