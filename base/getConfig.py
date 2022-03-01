import os
from configparser import ConfigParser


class GetConfig:

    def __init__(self):
        self.url = ''

    def get_url(self):
        config = ConfigParser()
        file = os.path.abspath("..") + "\\base\\baseconfig.ini"
        config.read(file)
        self.url = config.get("url", "TEST_URL")
        return self.url
