
from selenium import webdriver
from unittest import TestCase

from pages.login.login import Login


class TestLogin(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login(self):
        login = Login(self.driver)
        result = login.login('admin', '1')

        expect = '欢迎您:admin'

        self.assertEqual(expect, result)
