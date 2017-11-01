#coding=utf-8
'''
警告框处理
text 返回 alert/confirm/prompt 中的文字信息。
accept 点击确认按钮。
dismiss 点击取消按钮，如果有的话。
send_keys 输入值，这个 alert\confirm 没有对话框就不能用了，不然会报错。

在 WebDriver 中处理 JavaScript 所生成的 alert、confirm 以及 prompt 是很简单的。具体做法是使用
switch_to_alert()方法定位到 alert/confirm/prompt。然后使用 text/accept/dismiss/send_keys 按需进行操做。
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def alert1():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.baidu.com')
    #鼠标悬停相“设置”链接
    link = driver.find_element_by_link_text(u'设置')
    ActionChains(driver).move_to_element(link).perform()
    #打开搜索设置
    driver.find_element_by_class_name('setpref').click()
    time.sleep(2)
    print('等待设置')
    #保存设置
    driver.find_element_by_xpath("//*[@id='gxszButton']/a[1]").click()
    print('设置保存完毕')
    time.sleep(2)
    #接收弹窗
    driver.switch_to_alert().accept()
    print('弹窗处理完成')
    time.sleep(1)
    driver.quit()

if __name__ == '__main__':
    alert1()
