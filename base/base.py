# 封装操作浏览器的基本方法

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Base:
    # 初始化创建浏览器驱动
    def __init__(self, driver):
        self.driver = driver

    # 打开指定url页面
    def open(self, url):
        return self.driver.get(url)

    # 关闭当前窗口
    def close(self):
        return self.driver.close()

    # 关闭浏览器
    def quit(self):
        return self.driver.quit()

    # 最大化浏览器窗口
    def max_window(self):
        self.driver.maximize_window()

    # 设置隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 定位元素
    def location(self, loc):
        self.highlightElement(loc)
        return self.driver.find_element(*loc)

    def highlightElement(self, loc):
        ele = self.driver.find_element(*loc)  # 定位元素
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", ele,
                                   "background: green; border: 2px solid red;")  # 元素的背景色和边框设置成绿色和红色

    # 点击目标元素
    def click(self, loc):
        try:
            self.highlightElement(loc)
            self.driver.find_element(*loc).click()
        except:
            loc.click()

    # 向目标元素输入内容
    def input(self, loc, text):
        try:
            self.highlightElement(loc)
            return self.driver.find_element(*loc).send_keys(text)
        except:
            return loc.send_keys(text)

    # 清空输入框
    def clear(self, loc):
        try:
            self.driver.find_element(*loc).clear()
        except:
            loc.clear()

    # 获取元素文本
    def get_text(self, loc):
        try:
            self.highlightElement(loc)
            return self.driver.find_element(*loc).text
        except:
            return loc.text

    # 获取页面标题
    def title(self):
        return self.driver.title

    # 跳转窗口页面
    def switch_window(self, index=-1):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    # 跳入页面iframe框
    def switch_frame(self, name):
        self.driver.switch_to.frame(name)

    # 跳出iframe框
    def quit_frame(self):
        self.driver.switch_to.default_content()

    # 多层frame切换到上级frame
    def parent_frame(self):
        self.driver.switch_to.parent_frame()

    # 定位存在滚动条导致元素不可见的元素
    def scroll_loc(self, loc):
        el = self.driver.find_element(*loc)
        return self.driver.execute_script("arguments[0].scrollIntoView(false);", el)

    # 直接点击滚动条导致元素不可见的元素
    def scroll_click(self, loc):
        el = self.driver.find_element(*loc)
        self.driver.execute_script("arguments[0].click();", el)

    # 通过内容选择下拉列表中的选项
    def selector_text(self, loc, text):
        select = self.driver.find_element(*loc)
        el = Select(select)
        return el.select_by_visible_text(text)

    # 通过value值选择下拉列表中的选项
    def selector_value(self, loc, value):
        select = self.driver.find_element(*loc)
        el = Select(select)
        return el.select_by_value(value)

    # 通过下标选择下拉列表中的选项
    def selector_index(self, loc, index):
        select = self.driver.find_element(*loc)
        el = Select(select)
        return el.select_by_index(index)

    # 点击弹窗中的确定
    def alert_accept(self):
        return self.driver.switch_to.alert.accept()

    # 点击弹窗的取消
    def alert_dismiss(self):
        return self.driver.switch_to.alert.dismiss()

    # 向弹窗中输入值
    def alert_input(self, text):
        return self.driver.switch_to.alert.send_keys(text)

    # 获取弹窗中的文本信息
    def alert_text(self):
        return self.driver.switch_to.alert.text

    # 执行js代码修改元素的属性
    def execute_script(self, script):
        self.driver.execute_script(script)

    # 创建鼠标事件
    def mouse_action(self):
        ac = ActionChains(self.driver)
        return ac

    # 模拟鼠标悬停在元素上
    def mouse_over(self, loc):
        el = self.location(loc)
        self.mouse_action().move_to_element(el).perform()

    # 模拟鼠标左键点击元素并保持
    def mouse_click_hold(self):
        self.mouse_action().click_and_hold().perform()

    # 模拟移动鼠标点击的元素
    def mouse_move(self, loc, x, y):
        el = self.location(*loc)
        self.mouse_action().move_to_element_with_offset(el, x, y).perform()

    # 模拟鼠标右键点击
    def mouse_click(self, loc):
        el = self.location(loc)
        self.mouse_action().context_click(el).perform()

    # 模拟鼠标双击
    def mouse_double_click(self, loc):
        el = self.location(loc)
        self.mouse_action().double_click(el).perform()

    # 模拟鼠标拖动元素
    def mouse_drag(self, source, target):
        source = self.location(source)
        target = self.location(target)
        self.mouse_action().drag_and_drop(source, target).perform()

    # 模拟将鼠标移动到目标位置
    def mouse_drag_move(self, loc, x, y):
        el = self.location(loc)
        self.mouse_action().drag_and_drop_by_offset(el, x, y).perform()

    # 定位元素
    def locate(self, name, value):
        return self.driver.find_element(name, value)

    # 断言文本信息：可以捕获异常进行处理，也可以不捕获，因为报错就相当于断言失败。
    def assert_text(self, loc, expect):
        try:
            reality = self.driver.find_element(*loc).text
            assert expect == reality, '断言失败，实际结果为：{}'.format(reality)
            return True
        except Exception as e:
            print('断言失败信息：' + str(e))
            return False
