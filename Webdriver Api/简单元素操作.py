#coding=utf-8
'''
简单元素操作
clear() 清除文本，如果是一个文件输入框
send_keys(*value) 在元素上模拟按键输入
click() 单击元素

WebElement接口常用方法
submit() 用于提交表单，这里特别用于没提交按钮的情况
size 返回元素的尺寸。
text 获取元素的文本。
get_attribute(name) 获得属性值。
is_displayed() 设置该元素是否用户可见。
'''
from selenium import webdriver
import time

def signInQqMail():
    '''登录qq邮箱'''
    driver = webdriver.Chrome()
    driver.get("https://mail.qq.com/")
    driver.switch_to_frame("login_frame")
    driver.find_element_by_xpath('//*[@id="u"]').clear()
    driver.find_element_by_xpath('//*[@id="u"]').send_keys("xxxxxxxxxx")
    driver.find_element_by_xpath('//*[@id="p"]').clear()
    driver.find_element_by_xpath('//*[@id="p"]').send_keys("xxxxxxxxx")
    driver.find_element_by_id("login_button").click()
    now_url = driver.current_url
    print(now_url)
    now_handle = driver.current_window_handle
    print(now_handle)
    time.sleep(3)
    driver.quit()

def submit1():
    driver = webdriver.Chrome()
    driver.get("http://www.youdao.com")
    driver.find_element_by_id('translateContent').send_keys('hello')
    #提交输入框的内容
    driver.find_element_by_id('translateContent').submit()
    time.sleep(2)
    driver.quit()
    
def apiAlwaysInUse():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    #获得输入框的尺寸
    size=driver.find_element_by_id('kw').size
    print(size)
    #返回百度页面底部备案信息
    text=driver.find_element_by_id("cp").text
    print(text)
    #返回元素的属性值，可以是 id、name、type 或元素拥有的其它任意属性
    attribute=driver.find_element_by_id("kw").get_attribute('type')
    print(attribute)
    #返回元素的结果是否可见，返回结果为 True 或 False
    result=driver.find_element_by_id("kw").is_displayed()
    print result
    time.sleep(2)
    driver.quit()

if __name__ == '__main__':
    pass
