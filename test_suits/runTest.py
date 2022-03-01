
import time
import unittest

from HTMLTestRunner import HTMLTestRunner

tests = unittest.defaultTestLoader.discover(r'../test_cases', pattern="test*.py")

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
filename = r"../report/Report{}.html".format(now)
file = open(file=filename, mode='w+', encoding='utf-8')

runner = HTMLTestRunner.HTMLTestRunner(
    title='财政预算一体化',
    description='财政预算一体化数据界面显示测试',
    stream=file,
    verbosity=1
)

runner.run(tests)
file.close()
