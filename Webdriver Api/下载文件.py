#coding=utf-8
'''
下载文件
为了让 FireFox 让浏览器能实现文件的载，我们需要通过 FirefoxProfile() 对其参数做一个设置。
browser.download.folderList
设置成 0 代表下载到浏览器默认下载路径；设置成 2 则可以保存到指定目录。
browser.download.manager.showWhenStarting
是否显示开始，Ture 为显示，Flase 为不显示。
browser.download.dir
用于指定你所下载文件的目录。os.getcwd() 该函数不需要传递参数，用于返回当前的目录。
browser.helperApps.neverAsk.saveToDisk
指定要下载页面的 Content-type 值，“application/octet-stream”为文件的类型。HTTP Content-type 常
用对照表：http://tool.oschina.net/commons
这些参数的设置可以通过在 Firefox 浏览器地址栏输入：about:config 进行设置

将所有设置信息在调用 webdriver 的 Firefox()方法时作为参数传递给浏览器。下面 FireFox 浏览器在下
载时就根据这些设置信息将文件下载的当前脚本的目录下。
那么对于上面的方法只适用于 Firefox 浏览器，对于其它浏览器浏览设置方法会有所不同。
比较通用的方法的还是借助 AutoIt 来操作 Windows 控件进行下载
'''
from selenium import webdriver
import os
def downloadFiles():
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList",2)
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    fp.set_preference("browser.download.dir", os.getcwd())
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
    "application/octet-stream") #下载文件的类型
    driver = webdriver.Firefox(firefox_profile=fp)
    driver.get("http://pypi.Python.org/pypi/selenium")
    driver.find_element_by_partial_link_text("selenium-2").click()

if __name__ == '__main__':
    pass
