# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ProfileUsernameChange2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://antrian.imigrasi.go.id/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_5_profile_username_change2(self):
        driver = self.driver
        driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")
        driver.find_element_by_id("Username").clear()
        driver.find_element_by_id("Username").send_keys("lcfr")
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("1234567890")
        driver.find_element_by_id("btn-login").click()
        driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")
        driver.find_element_by_css_selector("a[title=\"Profile\"]").click()
        driver.find_element_by_name("Username").clear()
        driver.find_element_by_name("Username").send_keys("prism")
        driver.find_element_by_name('button-save').click()
        driver.execute_script("window.alert('Anda yakin ingin merubah data profil anda ?');")
        alert = driver.switch_to_alert()
        alert.accept()
        driver.find_element_by_id("bot2-Msg1").click()
        driver.get ("https://antrian.imigrasi.go.id/Index.jsp#Ajax/User/Profile.jsp")
        
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
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