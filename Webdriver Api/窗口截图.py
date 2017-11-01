#coding=utf-8
'''
窗口截图
get_screenshot_as_file() 截取当前窗口。
'''
from selenium import webdriver
import time

def screenShot():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    try:
        driver.find_element_by_id('kw_error').send_key('selenium')
        driver.find_element_by_id('su').click()
    except :
        driver.get_screenshot_as_file("D:\\baidu_error.jpg")
        print('已截图')
        driver.quit()

if __name__ == '__main__':
screenShot()
