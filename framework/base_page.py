import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os.path
from framework.logger import Logger

# create a logger instance
logger = Logger(logger="BasePage").get_log()


driver = webdriver.Chrome()

class BasePage(object):
    """
    定义一个页面基类，封装一些常用的页面基本操作方法到这个类
    让所有页面都继承这个页面
    """

    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()
        logger.info("Quit the browser")

    def forward_browser(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    def back_browser(self):
        self.driver.back()
        logger.info("Click Back button on current page.")

    # 隐式等待 implicitly
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("implicitly wait for %d second(s)", seconds)

    # 关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing the window and quiting the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser as %s" % e)

    def take_window_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        riqi = time.strftime('%Y%m%d%H%M', time.localtime((time.time())))
        img_name = file_path + riqi + '.png'
        try:
            self.driver.get_screenshot_as_file(img_name)
            logger.info("Took a screenshot and saved.")
        except NameError as e:
            logger.error("Failed to take screenshot %s" % e)
            self.take_window_img()  # 不是很明白这里为什么要self.take_window_img()

    # 定位元素方法




