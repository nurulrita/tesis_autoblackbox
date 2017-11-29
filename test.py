import time
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class BepyLoginFireFox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()

    def test_login_empty(self):
        #Username and Password empty
        driver = self.driver
        driver.get("http://bepy.pythonanywhere.com/accounts/login/")
        username = driver.find_element_by_id("id_username")
        password = driver.find_element_by_id("id_password")
        submit   = driver.find_element_by_class_name("btn-primary")
        #self.assertIn("Be-Py", driver.title)
        # elem = driver.find_element_by_name("q")        
        submit.click()
        self.assertIn("<li>This field is required.</li>", driver.page_source)
        # assert "No results found." not in driver.page_source

    def test_login_wrong(self):
        #username and password, wrong
        driver = self.driver
        driver.get("http://bepy.pythonanywhere.com/accounts/login/")
        username = driver.find_element_by_id("id_username")
        password = driver.find_element_by_id("id_password")
        submit   = driver.find_element_by_class_name("btn-primary")
        username.send_keys("aa")
        password.send_keys("bb")

        submit.click()         
        self.assertIn("Please enter a correct username and password.", driver.page_source)

    def test_login_pass_wrong(self):
        #username and password, wrong
        driver = self.driver
        driver.get("http://bepy.pythonanywhere.com/accounts/login/")
        username = driver.find_element_by_id("id_username")
        password = driver.find_element_by_id("id_password")
        submit   = driver.find_element_by_class_name("btn-primary")
        username.send_keys("anindita")
        password.send_keys("abcd")

        submit.click()         
        self.assertIn("Please enter a correct username and password.", driver.page_source)    

    def test_login_true(self):
        #username and password true
        driver = self.driver
        driver.get("http://bepy.pythonanywhere.com/accounts/login/")
        username = driver.find_element_by_id("id_username")
        password = driver.find_element_by_id("id_password")
        submit   = driver.find_element_by_class_name("btn-primary")
        username.send_keys("anindita")
        password.send_keys("1234")

        submit.click()         
        self.assertIn("Selamat Datang.. anindita", driver.page_source)

    def tearDown(self):
        self.driver.close()


class BepyLoginChrome(unittest.TestCase):

    def setUp(self):

        chromedriver = "/home/nuthanu/tesis/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()


    def test_login_empty(self):
        #Username and Password empty
        driver = self.driver
        driver.get("http://bepy.pythonanywhere.com/accounts/login/")
        username = driver.find_element_by_id("id_username")
        password = driver.find_element_by_id("id_password")
        submit   = driver.find_element_by_class_name("btn-primary")
        #self.assertIn("Be-Py", driver.title)
        # elem = driver.find_element_by_name("q")        
        submit.click()
        self.assertIn("<li>This field is required.</li>", driver.page_source)
        # assert "No results found." not in driver.page_source

    def test_login_wrong(self):
        #username and password, wrong
        driver = self.driver
        driver.get("http://bepy.pythonanywhere.com/accounts/login/")
        username = driver.find_element_by_id("id_username")
        password = driver.find_element_by_id("id_password")
        submit   = driver.find_element_by_class_name("btn-primary")
        username.send_keys("aa")
        password.send_keys("bb")

        submit.click()         
        self.assertIn("Please enter a correct username and password.", driver.page_source)

    def test_login_pass_wrong(self):
        #username and password, wrong
        driver = self.driver
        driver.get("http://bepy.pythonanywhere.com/accounts/login/")
        username = driver.find_element_by_id("id_username")
        password = driver.find_element_by_id("id_password")
        submit   = driver.find_element_by_class_name("btn-primary")
        username.send_keys("anindita")
        password.send_keys("abcd")

        submit.click()         
        self.assertIn("Please enter a correct username and password.", driver.page_source)    

    def test_login_true(self):
        #username and password true
        driver = self.driver
        driver.get("http://bepy.pythonanywhere.com/accounts/login/")
        username = driver.find_element_by_id("id_username")
        password = driver.find_element_by_id("id_password")
        submit   = driver.find_element_by_class_name("btn-primary")
        username.send_keys("anindita")
        password.send_keys("1234")

        submit.click()         
        self.assertIn("Selamat Datang.. anindita", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()