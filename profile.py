from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest, time, re

def login(driver):
    driver.get("https://antrian.imigrasi.go.id")
    username = driver.find_element_by_id("Username")
    password = driver.find_element_by_id("Password")
    submit   = driver.find_element_by_id("btn-login")
    username.send_keys("lcfr")
    password.send_keys("1234567890")

    submit.click()
    return driver

class ProfileFireFox(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30) 
		self.verificationErrors = []
		self.accept_next_alert = True

	# def test_profile(self):
	# 	driver = login(self.driver) 
	# 	driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")

	# 	driver.find_element_by_css_selector("a[title=\"Profile\"]").click()

	# def test_profile_NoChange(self):
	# 	driver = login(self.driver) 
	# 	driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")

	# 	driver.find_element_by_css_selector("a[title=\"Profile\"]").click()
	# 	driver.find_element_by_name('button-save').click()
	# 	wait = WebDriverWait(driver, 30)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'Msg1')))		
	# 	assert "Anda yakin ingin merubah data profil anda ?" in driver.page_source
	# 	driver.find_element_by_id('bot2-Msg1').click()
	# 	wait = WebDriverWait(driver, 30)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'smallbox1')))		
	# 	assert "Akun Anda Telah, Dirubah" in driver.page_source
	# 	driver.get ("https://antrian.imigrasi.go.id/Index.jsp#Ajax/User/Profile.jsp")

	# def test_profile_UsernameChange(self):
	# 	driver = login(self.driver) 
	# 	driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")

	# 	driver.find_element_by_css_selector("a[title=\"Profile\"]").click()
	# 	driver.find_element_by_name("Username").clear()
	# 	driver.find_element_by_name("Username").send_keys("prism")
	# 	driver.find_element_by_name('button-save').click()
	# 	wait = WebDriverWait(driver, 30)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'Msg1')))		
	# 	assert "Anda yakin ingin merubah data profil anda ?" in driver.page_source
	# 	driver.find_element_by_id('bot2-Msg1').click()
	# 	wait = WebDriverWait(driver, 30)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'smallbox1')))	
	# 	assert "Akun Anda Telah, Dirubah" in driver.page_source
	# 	driver.get ("https://antrian.imigrasi.go.id/Index.jsp#Ajax/User/Profile.jsp")

	# def test_profile_NIKkomChange(self):
	# 	driver = login(self.driver)
	# 	driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")

	# 	driver.find_element_by_css_selector("a[title=\"Profile\"]").click()
	# 	driver.find_element_by_name("Nik").clear()
	# 	driver.find_element_by_name("Nik").send_keys("37s8dkcdske0p101")
	# 	driver.find_element_by_name('button-save').click()
	# 	wait = WebDriverWait(driver, 30)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'Msg1')))		
	# 	assert "Anda yakin ingin merubah data profil anda ?" in driver.page_source
	# 	driver.find_element_by_id('bot2-Msg1').click()
	# 	wait = WebDriverWait(driver, 30)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'smallbox1')))	
	# 	assert "NIK User Tidak Valid" in driver.page_source
	# 	driver.get ("https://antrian.imigrasi.go.id/Index.jsp#Ajax/User/Profile.jsp")

	# def test_profile_NIKkurang16(self):
	# 	driver = login(self.driver)
	# 	driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")

	# 	driver.find_element_by_css_selector("a[title=\"Profile\"]").click()
	# 	driver.find_element_by_name("Nik").clear()
	# 	driver.find_element_by_name("Nik").send_keys("327606091")
	# 	driver.find_element_by_name('button-save').click()
	# 	wait = WebDriverWait(driver, 30)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'Msg1')))		
	# 	assert "Anda yakin ingin merubah data profil anda ?" in driver.page_source
	# 	driver.find_element_by_id('bot2-Msg1').click()
	# 	wait = WebDriverWait(driver, 30)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'smallbox1')))	
	# 	assert "NIK User Tidak Valid" in driver.page_source
	# 	driver.get ("https://antrian.imigrasi.go.id/Index.jsp#Ajax/User/Profile.jsp")

	# def test_profile_NIKlebih16(self):
	# 	driver = login(self.driver)
	# 	driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")

	# 	driver.find_element_by_css_selector("a[title=\"Profile\"]").click()
	# 	driver.find_element_by_name("Nik").clear()
	# 	driver.find_element_by_name("Nik").send_keys("3276060912900010908")
	# 	driver.find_element_by_name('button-save').click()
	# 	wait = WebDriverWait(driver, 30)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'Msg1')))		
	# 	assert "Anda yakin ingin merubah data profil anda ?" in driver.page_source
	# 	driver.find_element_by_id('bot2-Msg1').click()
	# 	wait = WebDriverWait(driver, 30)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'smallbox1')))	
	# 	assert "NIK User Tidak Valid" in driver.page_source
	# 	driver.get ("https://antrian.imigrasi.go.id/Index.jsp#Ajax/User/Profile.jsp")

	def test_profile_TeleponKombinasi(self):
		driver = login(self.driver)
		driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")

		driver.find_element_by_css_selector("a[title=\"Profile\"]").click()
		driver.find_element_by_name("Telephone").clear()
		driver.find_element_by_name("Telephone").send_keys("08123451bcde")
		driver.find_element_by_name('button-save').click()
		wait = WebDriverWait(driver, 30)
		element = wait.until(EC.element_to_be_clickable((By.ID, 'Msg1')))		
		assert "Anda yakin ingin merubah data profil anda ?" in driver.page_source
		driver.find_element_by_id('bot2-Msg1').click()
		wait = WebDriverWait(driver, 30)
		element = wait.until(EC.element_to_be_clickable((By.ID, 'smallbox1')))	
		assert "Nomer Telephone Tidak Valid" in driver.page_source
		driver.get ("https://antrian.imigrasi.go.id/Index.jsp#Ajax/User/Profile.jsp")


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


