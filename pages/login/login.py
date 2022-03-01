from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base
from base.getConfig import GetConfig


class Login(Base):
    # 从配置文件中读取url
    config = GetConfig()
    url = config.get_url()

    dict_loc = {
        '用户名': (By.ID, 'username'),
        '密码': (By.ID, 'password'),
        '年度': (By.ID, 'busiyear'),
        '区划': (By.XPATH, '//*[@id="_easyui_textbox_input2"]/../span/a'),
        '登录': (By.ID, 'subimg')
    }

    def login(self, username, password, year='2022年', dvision=''):
        self.open(self.url)
        self.max_window()
        self.wait(10)

        self.input(self.dict_loc['用户名'], username)
        self.input(self.dict_loc['密码'], password)
        self.selector_text(self.dict_loc['年度'], year)
        if dvision != '':
            self.click(self.dict_loc['区划'])
            loc = (By.XPATH, '//*[text()="{0}"]'.format(dvision))
            self.scroll_click(loc)

        self.click(self.dict_loc['登录'])
        sleep(3)
        expect = (By.XPATH, '//*[text()="欢迎您:{0}"]'.format(username))

        return self.get_text(expect)
