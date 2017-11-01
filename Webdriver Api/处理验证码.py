#coding=utf-8
'''
验证码处理
常见处理方式：
1 去掉验验证码（正式环境有安全风险）
2 设置万能码
3 Python-tesseract 是光学字符识别 Tesseract OCR 引擎的 Python 封装类。
能够读取任何常规的图片文件(JPG, GIF ,PNG , TIFF 等)。
不过，目前市面上的验证码形式繁多，目前任何一种验证码识别技术，识别率都不是100% 。
4 记录 cookie
通过向浏览器中添加 cookie 可以绕过登录的验证码，这是比较有意思的一种解决方案。比如我们在
第一次登录某网站可以勾选“记住密码”的选项，当下次再访问该网站时自动就处于登录状态了。这样其
实也绕过验证码问题。那么这个“记住密码”的功能其实就记在了浏览器的 cookie 中。前面已经学了通过
WebDriver 来操作浏览器的 Cookie，可以通过 add_cookie()方法将用户名密码写入浏览器 cookie ，再次访
问网站时服务器直接读取浏览器 Cookie 登录。
'''
import random

def dealWithIdentify():
    '''万能码方式'''
    #生成一个 1000 到 9999 之间的随机整数
    verify = random.randint(1000,9999)
    print(u"生成的随机数:%d " %verify)
    number = input(u"请输入随机数:")
    print number
    if number == verify:
        print(u"登录成功!!")
    elif number == 132741:
        print(u"登录成功!!")
    else:
        print(u"验证码输入有误！")
        
if __name__ == '__main__':
    dealWithIdentify()
