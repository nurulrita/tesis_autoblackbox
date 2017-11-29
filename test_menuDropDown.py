import time
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def login(driver):
    driver.get("http://bepy.pythonanywhere.com/accounts/login/")
    username = driver.find_element_by_id("id_username")
    password = driver.find_element_by_id("id_password")
    submit   = driver.find_element_by_class_name("btn-primary")
    username.send_keys("anindita")
    password.send_keys("1234")
    submit.click()
    return driver


class BepyMenuDropDownFireFox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()

    def test_ProfileSaya(self):
        driver = login(self.driver)        

        #Test Profile Saya
        driver.get("http://bepy.pythonanywhere.com/learning/dashboard/")
        self.assertIn("Profil (anindita)..", driver.page_source)

        #Test Bantuan
        driver.get("http://bepy.pythonanywhere.com/learning/bantuan/")
        self.assertIn("BANTUAN", driver.page_source)

        #Test Tentang
        driver.get("http://bepy.pythonanywhere.com/learning/about/")
        self.assertIn("Tentang Be-Py", driver.page_source)

        #Test Keluar
        # driver.find_element_by_link_text("Keluar").click()
        # driver.get("http://bepy.pythonanywhere.com/learning/")


    def tearDown(self):
        self.driver.close()

class BepyMenuDropDownChrome(unittest.TestCase):

    def setUp(self):
        chromedriver = "/home/nuthanu/tesis/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()

    def test_ProfileSaya(self):
        driver = login(self.driver)        

        #Test Profile Saya
        driver.get("http://bepy.pythonanywhere.com/learning/dashboard/")
        self.assertIn("Profil (anindita)..", driver.page_source)

        #Test Bantuan
        driver.get("http://bepy.pythonanywhere.com/learning/bantuan/")
        self.assertIn("BANTUAN", driver.page_source)

        #Test Tentang
        driver.get("http://bepy.pythonanywhere.com/learning/about/")
        self.assertIn("Tentang Be-Py", driver.page_source)

        #Test Keluar
        # driver.find_element_by_link_text("Keluar").click()
        # driver.get("http://bepy.pythonanywhere.com/learning/")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

