#coding=utf-8
'''
switch_to_frame() 默认可以直接取表单的 id 或 name 属性进行切换。
如果 iframe 没有可用的 id 和 name 可以通过下面的方式进行定位
先通过 xpth 定位到 iframe
xf = driver.find_element_by_xpath('//*[@class="if"]')
再将定位对象传给 switch_to_frame()方法
driver.switch_to_frame(xf)

switch_to_default_content() 返回到上一层表单
'''
from selenium import webdriver
import time
import os

def frame1():
    '''表单操作'''
    #打开准备的有frame表单的网页
    dr = webdriver.Chrome()
    file_path = 'file:///' + os.path.abspath('frame.html')
    dr.get(file_path)
    #切换到iframe（id="if"）
    dr.switch_to_frame("if")
    #下面就可以正常操作元素
    dr.find_element_by_id("kw").send_keys("selenium")
    dr.find_element_by_id("su").click()
    time.sleep(2)
    dr.quit()

if __name__ == '__main__':
    frame1()
