# import HtmlTestRunner
import HTMLTestRunner
import os
import time
import unittest
# import testsuites
# from testsuites.test_baidu_search import BaiduSearch
# from testsuites.test_get_page_title import GetPageTitle

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath(".")) + '/test_report/'

# 设置时间
time_now = time.strftime("%Y-%m-%d_%H-%M-%S ", time.localtime(time.time()))

# 设置报告名称
# HtmlFile = time_now + 'Html Report.html'
HtmlFile = report_path + time_now + 'HtmlReport.html'
fp = open(HtmlFile, "wb")  # 通过open()方法以二进制写模式('wb')打开当前目录下的html,如果没有则自行创建（先创建打开，再写入）

# suite = unittest.TestSuite()  # 指定某个类的某个方法
# suite.addTest(BaiduSearch('test_baidu_search'))
# suite.addTest(BaiduSearch('test_search_2'))
# suite.addTest(GetPageTitle('test_get_page_title'))
# suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))  # 指定某个类下的所有方法

# 指定某个文件目录下的所有方法：
suite = unittest.TestLoader().discover("testsuites")

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp, title="Sheldon Report", description="测试结果：", verbosity=2
    )

    # runner = HtmlTestRunner.HTMLTestRunner(
    #     output="../test_report/", report_title="Sheldon Report", report_name=time_now,
    #     add_timestamp=False)
    runner.run(suite)
    fp.close()
