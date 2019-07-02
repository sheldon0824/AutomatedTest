import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os.path
from framework.logger import Logger
from framework.browser_engine import BrowserEngine


# create a logger instance
logger = Logger(logger="BasePage").get_log()


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
        riqi = time.strftime('%Y%m%d%H%M%S', time.localtime((time.time())))
        img_name = file_path + riqi + '.png'
        try:
            self.driver.get_screenshot_as_file(img_name)
            logger.info("Took a screenshot and saved.")
        except NameError as e:
            logger.error("Failed to take screenshot %s" % e)
            self.take_window_img()  # 不是很明白这里为什么要self.take_window_img()

    # 定位元素方法
    def find_elements(self, selector):
        """
        为什么这边是根据>=来切割字符串？
        submit_btn = "id=>su"
        login_link = "xpath=>//*[@id='u1']/a[7]"  # 百度首页 登录链接定位
        因为如果用等号，结果很多xpath表达式中也有=，会造成字符切割不准确，影响定位
        :param selector:
        :return: element
        """
        element = ''  # 先定义了一个无值的变量
        if '=>' not in selector:  # 例子中的selector = ‘id=>kw’
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]  # 例子中的selector = ‘id=>kw’，即id
        selector_value = selector.split('=>')[1]  # 例子中的selector = ‘id=>kw’，即右边的kw

        if selector_by == 'i' or selector_by == 'id':  # 使用id
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Select element \'%s\' successfully, "  
                            # 转义字符为了打印出单引号
                            # 常常 find_element_by_id().text 返回的text是空白的
                            "by %s via value:%s " % (element.text, selector_by, selector_value)
                            )
            except NoSuchElementException as e:
                logger.error("No Such Element Exception:%s" % e)
                self.take_window_img()

        elif selector_by == 'n' or selector_by == 'name':  # 使用name
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'c' or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == 's' or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':  # 使用xpath
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Found the element \'%s\' successfully, "
                            "by %s via value:%s" % (element.text, selector_by, selector_value)
                            )  # 用了2个括号，注意啦~！
            except NoSuchElementException as e:
                logger.error("No Such Element Exception: %s " % e)
                self.take_window_img()
        else:
            raise NameError("Please enter a valid type of targeting element!")  # 输出错误提示
        return element

    # 文本框输入
    def type(self, selector, text):

        el = self.find_elements(selector)  # 例子中的selector = ‘id=>kw’
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type %s into textbox" % text)
        except NameError as e:
            logger.error("Error on type into textbox %s " % e)
            self.take_window_img()

    # 清除文本框
    def clear(self, selector):

        el = self.find_elements(selector)
        try:
            el.clear()
            logger.info("Clear the textbox")
        except NameError as e:
            logger.error("Error when clear the textbox %s " % e)
            self.take_window_img()

    # 点击元素
    def click(self, selector):

        el = self.find_elements(selector)
        try:
            el.click()
            logger.info("Mouse on the element and click")
        except NameError as e:
            logger.error("Error on click the element %s " % e)
            self.take_window_img()

    # 拿到网页标题
    def get_title(self):
        logger.info("Current page's title is:%s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("You have been sleep for %s seconds" % seconds)




