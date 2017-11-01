#coding=utf-8
'''
获取验证信息
text 获取用户文本
title 用于获得当前页面的标题。
current_url 用户获得当页面的 URL
'''
from selenium import webdriver
import time

def signInQqMail():
    '''登录qq邮箱'''
    driver = webdriver.Chrome()
    driver.get("https://mail.qq.com/")
    print('Before login================')
    #打印当前页面 title
    title = driver.title
    print(title)
    #打印当前页面 URL
    now_url = driver.current_url
    print(now_url)
    driver.switch_to_frame("login_frame")
    driver.find_element_by_xpath('//*[@id="u"]').clear()
    driver.find_element_by_xpath('//*[@id="u"]').send_keys("xxxxxxx")
    driver.find_element_by_xpath('//*[@id="p"]').clear()
    driver.find_element_by_xpath('//*[@id="p"]').send_keys("xxxxxxx")
    driver.find_element_by_id("login_button").click()
    print('After login================')
    #打印当前页面 title
    title = driver.title
    print(title)
    #打印当前页面 URL
    now_url = driver.current_url
    print(now_url)
    now_handle = driver.current_window_handle
    print(now_handle)
    time.sleep(3)
    user_name = driver.find_element_by_id("useralias").text
    print(user_name)
    driver.quit()

if __name__ == '__main__':
    signInQqMail()

