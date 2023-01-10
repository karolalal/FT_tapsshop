import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_object import main_page, login_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_logo_visible(self):
        self.assertTrue(main_page.taps_logo_visible(self.driver))

if __name__ == '__main__':
    unittest.main()
