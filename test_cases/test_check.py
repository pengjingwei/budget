from unittest import TestCase

from selenium import webdriver

from pages.login.home import Home
from pages.login.login import Login
from pages.userCenter.check_data import CheckData


class TestCheck(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_check(self):
        Login(self.driver).login('admin', 1)
        enter = Home(self.driver)
        enter.enter('用户授权管理')
        result = CheckData(self.driver).check()
        expect = True
        self.assertEqual(expect, result)
