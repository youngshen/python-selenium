#coding=utf-8
'''
调用JavaScript
WebDriver提供了 execute_script()方法执行 JavaScript代码。
一般用到操作滚动条的会两个场景：
 注册时的法律条文的阅读，判断用户是否阅读完成的标准是：滚动条是否拉到最下方。
 要操作的页面元素不在视觉范围，无法进行操作，需要拖动滚动条。
用于标识滚动条位置的代码
……
<body onload= "document.body.scrollTop=0 ">
<body onload= "document.body.scrollTop=100000 "> 
……
document.body.scrollTop
网页被卷去的高。scrollTop 设置或获取滚动条与最顶端之间的距离。如果想让滚动条处于顶部，那么
可以设置 scrollTop 的值为 0，如果想让滚动条处于最底端，可以将这个值设置的足够大，大个窗口的高度
即可。scrollTop 的值以像素为单位。

JavaScript 的作用不仅于此，它同样可操作页面上的元素或让，或让这个元素隐藏。学习和使
用 JavaScript 不仅可以让你对前端技术有更深的认识，还可以让你对 web 页面上元素的操作变得游刃有余。
'''
from selenium import webdriver
import time

def cookie1():
    #访问百度
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    #搜索
    driver.find_element_by_id("kw").send_keys("rng")
    driver.find_element_by_id("su").click()
    time.sleep(2)
    #将页面滚动条拖到底部
    js="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    time.sleep(2)
    #将滚动条移动到页面的顶部
    js_="var q=document.documentElement.scrollTop=0"
    driver.execute_script(js_)
    time.sleep(2)
    driver.quit()

if __name__ == '__main__':
    cookie1()
