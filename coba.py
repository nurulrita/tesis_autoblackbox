from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BuatPermohonanButon(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://antrian.imigrasi.go.id/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_buat_permohonan_buton(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("Username").clear()
        driver.find_element_by_id("Username").send_keys("lcfr")
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("1234567890")
        driver.find_element_by_id("btn-login").click()
        driver.find_element_by_xpath("//*[@id='list-kanim']/tr[10]/td[3]/button").click()
    
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