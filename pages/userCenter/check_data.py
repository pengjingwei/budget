from selenium.webdriver.common.by import By

from base.base import Base


class CheckData(Base):
    dict_loc = {
        '预算单位(全局)': (By.XPATH, '//*[@id="_easyui_tree_2"]/span[4]'),
        '数据': (By.XPATH, '//*[text()="0000001"]')
    }

    def check(self):
        self.click(self.dict_loc['预算单位(全局)'])

        try:
            self.switch_frame('iframe35glo')
            self.location(self.dict_loc['数据'])
            return True
        except:
            return False
        finally:
            # 关闭当前页面，回到首页，便于后续其他页面操作
            self.close()
            self.switch_window(0)
