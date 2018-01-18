from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options

import os, re, unittest, time 

class LoginFirefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://antrian.imigrasi.go.id"
        self.verificationErrors = []
        self.accept_next_alert = True

    # def test_login_empty(self):
    # 	driver = self.driver
    # 	driver.get(self.base_url + "/Authentication.jsp")
    # 	driver.find_element_by_id("btn-login").click()
    # 	assert "Masukkan Nama Akun Anda" and "Masukkan Password Anda" in driver.page_source     

    # def test_login_akunWrong(self):
    # 	driver = self.driver
    #     driver.get(self.base_url + "/Authentication.jsp")
    # 	username = driver.find_element_by_id("Username")
    #     password = driver.find_element_by_id("Password")
    #     submit   = driver.find_element_by_id("btn-login")
    #     username.send_keys("kmjl")
    #     password.send_keys("")
    #     submit.click()
    #     assert "Masukkan Password Anda" in driver.page_source        

    # def test_login_passWrong(self):
    # 	driver = self.driver
    #     driver.get(self.base_url + "/Authentication.jsp")
    #     username = driver.find_element_by_id("Username")
    #     password = driver.find_element_by_id("Password")
    #     submit   = driver.find_element_by_id("btn-login")
    #     username.send_keys("lcfr")
    #     password.send_keys("zxcvbnm")
    #     submit.click()
    #     driver.execute_script("window.alert('Invalid username or password');")
    #     alert = driver.switch_to_alert()
    #     alert.accept()         

    def test_login_true(self):
    	driver = self.driver
        driver.get(self.base_url + "/Authentication.jsp")
        username = driver.find_element_by_id("Username")
        password = driver.find_element_by_id("Password")
        submit   = driver.find_element_by_id("btn-login")
        username.send_keys("lcfr")
        password.send_keys("1234567890")

        submit.click()
        driver.get ("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")

    def is_element_present(self, how, what):
        try: 
        	self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: 
        	self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()