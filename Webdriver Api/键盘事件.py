#coding=utf-8
'''
键盘事件
send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
send_keys(Keys.SPACE) 空格键(Space)
send_keys(Keys.TAB) 制表键(Tab)
send_keys(Keys.ESCAPE) 回退键（Esc）
send_keys(Keys.ENTER) 回车键（Enter）
send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
send_keys(Keys.F1) 键盘 F1
……
send_keys(Keys.F12) 键盘 F12
'''
import time
from selenium import webdriver
#引入Keys模块
from selenium.webdriver.common.keys import Keys

def test1():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    #输入框输入内容
    driver.find_element_by_id("kw").send_keys("seleniumm")
    #删除多输入的一个m
    driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
    #全选输入框内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
    #剪切输入框内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
    #粘贴内容到输入框
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
    #回车代替点击操作
    driver.find_element_by_id("su").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.quit()

if __name__ == '__main__':
    test1()

