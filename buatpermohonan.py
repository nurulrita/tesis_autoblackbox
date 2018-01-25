from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, re, unittest, time

def login(driver):
    driver.get("https://antrian.imigrasi.go.id")
    username = driver.find_element_by_id("Username")
    password = driver.find_element_by_id("Password")
    submit   = driver.find_element_by_id("btn-login")
    username.send_keys("lcfr")
    password.send_keys("1234567890")

    submit.click()
    return driver

class BuatPermohonan(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_buat_permohonan(self):
		driver = login(self.driver) 
		driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")
		wait = WebDriverWait(driver, 30)
		element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))
		driver.find_element_by_class_name ("btn-primary")

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



