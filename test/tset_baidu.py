"""
@Author: zn
@Data:  11:26 上午
@Desc:
"""
import configparser
import os
import unittest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@allure.feature('test baidu web')
class TestDemo(unittest.TestCase):
    # 读取配置,chromedirver 路径放在配置文件里面。因为每个电脑位置不一样
    def get_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['HOME'], 'run.ini'))
        return config

    def setUp(self) -> None:
        #设置前后台运行
        config = self.get_config()
        try:
            using_headless = config.get('driver', 'using_headless')
        except KeyError:
            using_headless = None
            print('未配置，有界面方式运行')

        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('无界面运行')
            chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                       chrome_options=chrome_options)

    def tearDown(self) -> None:
        pass

    def test_baidu(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('今日头条')
        self.driver.find_element_by_xpath('//*[@id="su"]').click()
        assert '百度' in self.driver.title




