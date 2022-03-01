from selenium.webdriver.common.by import By

from base.base import Base


class Home(Base):

    def enter(self, element):

        el = (By.XPATH, '//*[text()="{0}"]/..'.format(element))
        self.click(el)

        self.switch_window()
