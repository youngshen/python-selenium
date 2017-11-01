#coding=utf-8
import unittest

#定义测试文件查找的目录
test_dir=r'C:\Users\Administrator\eclipse-workspace\Terst1\src\test_project'
#定义 discover 方法的参数
discover=unittest.defaultTestLoader.discover(test_dir,pattern ='test*.py',top_level_dir=None)

if __name__ == '__main__':
    runner =unittest.TextTestRunner()
    runner.run(discover)
