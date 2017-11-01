#coding=utf-8
'''
maximize_window() 全屏设置
set_window_size(480, 800) 参数数字为像素点
driver.forward() 页面前进
driver.back() 页面后退
clear() 清除文本，如果是一个文件输入框
send_keys(*value) 在元素上模拟按键输入
click() 单击元素
'''
from selenium import webdriver
import time

def setSize():
    #设置浏览器大小
    driver = webdriver.Chrome()
    
    #参数数字为像素点
    print "设置浏览器宽 480、高 800 显示"
    driver.set_window_size(480, 800)
    
    #全屏设置
    #driver.maximize_window()
    
    driver.get("http://www.baidu.com")
    
    time.sleep(2)
    driver.quit()

def forwardAndback():
    ''' 
    driver.forward() 页面前进
    driver.back() 页面后退
    '''
    driver = webdriver.Chrome()
    #访问百度首页
    first_url= 'http://www.baidu.com'
    print "now access %s" %(first_url)
    driver.get(first_url)
    time.sleep(1)
    #访问新闻页面
    second_url='http://news.baidu.com'
    print "now access %s" %(second_url)
    driver.get(second_url)
    time.sleep(1)
    
    #返回（后退）到百度首页
    print "back to %s "%(first_url)
    driver.back()
    time.sleep(1)
    #前进到新闻页
    print "forward to %s"%(second_url)
    driver.forward()
    time.sleep(1)
    
    driver.quit()

if __name__ == '__main__':
    pass
