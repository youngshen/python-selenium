#coding=utf-8
'''
find_elements_by_id()
find_elements_by_name()
find_elements_by_class_name()
find_elements_by_tag_name()
find_elements_by_link_text()
find_elements_by_partial_link_text()
find_elements_by_xpath()
find_elements_by_css_selector()
定位一组对象的方法与定位单个对象的方法类似，唯一的区别是在单词 element 后面多了一个 s 表示
复数。定位一组对象一般用于以下场景：
批量操作对象，比如将页面上所有的复选框都被勾选。
先获取一组对象，再在这组对象中过滤出需要具体定位的一些对象。比如定位出页面上所有的checkbox，然后选择最后一个。

'''
from selenium import webdriver
import os
from lib2to3.tests.support import driver

def elements():
    '''定位一组元素'''
    dr = webdriver.Chrome()
    file_path = 'file:///' + os.path.abspath('checkbox.html')
    
    dr.get(file_path)
    
    #勾选第二个复选框
    #dr.find_elements_by_css_selector('input[type=checkbox]')。pop(1).click()
    
    #选择页面上所有的tag name为 input的元素
    inputs = dr.find_elements_by_tag_name('input')
    #然后从中过滤出type为checkbox的元素，单击勾选
    for i in inputs:
        if i.get_attribute('type') == 'checkbox':
            i.click()
    dr.quit()
    
if __name__ == '__main__':
    elements()

