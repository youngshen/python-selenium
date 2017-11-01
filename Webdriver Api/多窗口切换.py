#coding=utf-8
'''
current_window_handle 获得当前窗口句柄
window_handles 返回的所有窗口的句柄到当前会话
switch_to_window() 用于切换到相应的窗口、与上一节的switch_to_frame()类似、后者用于不同表单之间切换
'''
from selenium import webdriver
import time

def windowsSwitch():
    dr = webdriver.Chrome()
    dr.implicitly_wait(10)
    dr.get("http://www.baidu.com")
    #获得百度搜索窗口句柄
    search_windows = dr.current_window_handle
    dr.find_element_by_link_text(u'登录').click()
    dr.find_element_by_link_text(u'立即注册').click()
    
    #获取当前所有打开窗口的句柄
    all_handles = dr.window_handles
    #进入注册窗口
    for handle in all_handles:
        if handle != search_windows:
            dr.switch_to_window(handle)
            print('now register window!')
            dr.find_element_by_name("account").send_keys()
            dr.find_element_by_name('password').send_keys()
    #......
    #进入搜索窗口
    for handle in all_handles:
        if handle ==search_windows:
            dr.switch_to_window(handle)
            print('now search window!')
            dr.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
            dr.find_element_by_id("kw").send_keys("selenium")
            dr.find_element_by_id("su").click()
    time.sleep(5)
    dr.quit()   
    
if __name__ == '__main__':
    windowsSwitch()
