#coding=utf-8
'''
鼠标事件
ActionChains类提供的鼠标操作的常用方法：
perform() 执行所有ActionChains中存储的行为
context_click() 右击
double_click() 双击
drag_and_drop() 拖动
move_to_element() 鼠标悬停
'''
from selenium import webdriver
import time
#引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains

def test1():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")

    #定位到要右击的元素
    right_click = driver.find_element_by_id('su')
    #对定位到的元素执行右键操作
    ActionChains(driver).context_click(right_click).perform()
    
    #鼠标悬停操作
    #定位元素的源位置
    element = driver.find_element_by_name("xxx")
    #定位元素要移动到的目标位置
    target = driver.find_element_by_name("xxx")
    #执行元素的拖放操作
    ActionChains(driver).drag_and_drop(element, target).perform()
    
    
    time.sleep(1)
    driver.quit()

if __name__ == '__main__':
    test1()
