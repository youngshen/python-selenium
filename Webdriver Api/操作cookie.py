#coding=utf-8
'''
操作 cookie
get_cookies() 获得所有 cookie 信息
get_cookie(name) 返回有特定 name 值有 cookie 信息
add_cookie(cookie_dict) 添加 cookie，必须有 name 和 value 值
delete_cookie(name) 删除特定(部分)的 cookie 信息
delete_all_cookies() 删除所有 cookie 信息
'''
from selenium import webdriver
import time

def cookie1():
    driver = webdriver.Chrome()
    driver.get("http://www.youdao.com")
    time.sleep(1)
    # 获得 cookie 信息
    cookie = driver.get_cookies()
    #将获得 cookie 的信息打印
    print(cookie)
    driver.quit()

if __name__ == '__main__':
    cookie1()
