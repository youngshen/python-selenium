#coding=utf-8
'''
上传文件
普通上传：普通的附件上传都是将本地文件的路径作为一个值放 input 标签中，通过 form 表单提交的时候将这个值提交给服务器。
插件上传：一般是指基于 Flash 与 JavaScript 或 Ajax 等技术所实现的上传功能或插件。
插件上传需要借助AutoIt、因为打开的windows窗口需要这个软件识别与操作、这里不介绍
'''
from selenium import webdriver
import time
import os

def sendFiles():
    '''普通上传'''
    driver = webdriver.Chrome()
    #打开上传功能页面
    file_path = 'file:///' + os.path.abspath('upfile.html')
    driver.get(file_path)
    #定位上传按钮，添加本地文件
    driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')
    driver.quit()

if __name__ == '__main__':
    pass
