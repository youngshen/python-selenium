#coding=utf-8
from selenium import webdriver
import unittest, time
import HTMLTestRunner #引入 HTMLTestRunner 包

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
    
    def test_baidu_search(self):
        #百度搜索用例
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw123").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":

    #测试套件
    testunit=unittest.TestSuite()
    #添加测试用例到测试套件中
    testunit.addTest(Baidu("test_baidu_search"))
    #定义个报告存放路径
    filename = r'C:\Users\Administrator\Desktop\result.html'
    fp = file(filename, 'wb')
    #定义测试报告
    runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'自动化测试报告',
    description=u'用例执行情况：')
    #运行测试用例
    runner.run(testunit)
    #关闭报告文件
    fp.close()
