import time
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def login(driver):
    driver.get("http://bepy.pythonanywhere.com/accounts/login/")
    username = driver.find_element_by_id("id_username")
    password = driver.find_element_by_id("id_password")
    submit   = driver.find_element_by_class_name("btn-primary")
    username.send_keys("anindita")
    password.send_keys("1234")
    submit.click()
    return driver

class BepyLearningFireFox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()

    def test_login_empty(self):
        driver = login(self.driver)               

        driver.get("http://bepy.pythonanywhere.com/learning/")
        submit   = driver.find_element_by_class_name("btn-primary")       
        submit.click()
        self.assertIn("BAB YANG DIPELAJARI", driver.page_source)

    def tearDown(self):
        self.driver.close()


class BepyLearningChrome(unittest.TestCase):

    def setUp(self):
        chromedriver = "/home/nuthanu/tesis/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()

    def test_login_empty(self):
        driver = login(self.driver)               

        driver.get("http://bepy.pythonanywhere.com/learning/")
        submit   = driver.find_element_by_class_name("btn-primary")       
        submit.click()
        self.assertIn("BAB YANG DIPELAJARI", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()