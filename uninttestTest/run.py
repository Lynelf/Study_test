import unittest
from utils.HTMLTestRunner import HTMLTestRunner
import time

# 1.收集所有的测试用例
testcases = unittest.defaultTestLoader.discover('cases','test_*.py')

# 2.把测试用例装载到测试套件
testsuite = unittest.TestSuite()
testsuite.addTests(testcases)

# 3.执行测试套件，并生成测试报告
now = time.strftime("%Y-%m-%d %H_%M_%S")  # 报告生成时间
title = "测试报告"
descr = "网页报告的描述"
filename = 'reports/' + now + ' report.html'
with open(filename, "wb") as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(testsuite)