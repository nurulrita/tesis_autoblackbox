from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

def login(driver):
	driver.get("https://antrian.imigrasi.go.id/")
	username = driver.find_element_by_id("Username")
	password = driver.find_element_by_id("Password")
	submit   = driver.find_element_by_id("btn-login")
	username.send_keys("lcfr")
	password.send_keys("1234567890")
	submit.click()
	return driver

class Syarat_ProsedurFireFox(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.verificationErrors = []
		self.accept_next_alert = True
		self.driver.set_window_size(1920, 1080)
		self.driver.maximize_window()

	# def test_syaratProsedur(self):
	# 	driver = login(self.driver) 
	# 	driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Terms/syarat.jsp")

	# 	driver.find_element_by_css_selector("a[title=\"Syarat & Prosedur\"] > span.menu-item-parent").click()
	# 	assert "Persyaratan Dan Prosedur" in driver.page_source

	# def test_syaratProsedur_Persyaratan(self):
	# 	driver = login(self.driver) 
	# 	driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Terms/syarat.jsp")

	# 	driver.find_element_by_css_selector("a[title=\"Syarat & Prosedur\"] > span.menu-item-parent").click()

	# 	driver.find_element_by_link_text("Persyaratan").click()
	# 	assert "Persyaratan" in driver.page_source

	def test_syaratProsedur_Persyaratan(self):
		driver = login(self.driver) 
		driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Terms/syarat.jsp")

		driver.find_element_by_css_selector("a[title=\"Syarat & Prosedur\"] > span.menu-item-parent").click()

		driver.find_element_by_link_text("Panduan").click()
		assert "Panduan" in driver.page_source


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