#coding=utf-8
'''
显式等待
显式等待使 WebdDriver 等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）
WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
driver - WebDriver 的驱动程序（Ie， Firefox，Chrome 等）
timeout - 最长超时时间，默认以秒为单位
poll_frequency - 休眠时间的间隔（步长）时间，默认为 0.5 秒
ignored_exceptions - 超时后的异常信息，默认情况下抛 NoSuchElementException 异常。
until()
WebDriverWait()一般由 until()（或 until_not()）方法配合使用，下面是 until()和 until_not()方法的说明。
until(method, message=’ ’)
调用该方法提供的驱动程序作为一个参数，直到返回值为 Ture。
until_not(method, message=’ ’)
调用该方法提供的驱动程序作为一个参数，直到返回值为 False。
Expected Conditions
调用 presence_of_element_located()判断元素是否存在。
expected_conditions 类提供一些预期条件的实现。
title_is 用于判断标题是否 xx。
title_contains 用于判断标题是否包含 xx 信息。
presence_of_element_located 元素是否存在。
visibility_of_element_located 元素是否可见。
visibility_of 是否可见
presence_of_all_elements_located 判断一组元素的是否存在
text_to_be_present_in_element 判断元素是否有 xx 文本信息
text_to_be_present_in_element_value 判断元素值是否有 xx 文本信息
frame_to_be_available_and_switch_to_it 表单是否可用，并切换到该表单。
invisibility_of_element_located 判断元素是否隐藏
element_to_be_clickable 判断元素是否点击，它处于可见和启动状态
staleness_of 等到一个元素不再是依附于 DOM。
element_to_be_selected 被选中的元素。
element_located_to_be_selected 一个期望的元素位于被选中。
element_selection_state_to_be 一个期望检查如果给定的元素被选中。
element_located_selection_state_to_be 期望找到一个元素并检查是否选择状态
alert_is_present 预期一个警告信息
除了 expected_conditions 所提供的预期方法，我们也可以使用前面学过的 is_displayed()方法来判断元
素是否可见。

隐式等待
隐式等待是通过一定的时长等待页面所元素加载完成。哪果超出了设置的时长元素还没有被加载测抛
NoSuchElementException 异常。WebDriver 提供了 implicitly_wait()方法来实现隐式等待，默认设置为 0。
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait1():
        
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
    #显式等待、等待5、每间隔0.5秒确认一次
    element = WebDriverWait(driver,5,0.5).until(
        EC.presence_of_element_located((By.ID,"kw"))
        )
    element.send_keys('selenium')
    
    #隐式等待、等待10秒                    
    #driver.implicitly_wait(10)
    time.sleep(2)
    driver.quit()

if __name__ == '__main__':
    pass
