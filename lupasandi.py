from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest, time, re

class LupaSandiFirefox(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_LupaSandi(self):
		driver = self.driver
		driver.get("https://antrian.imigrasi.go.id")
		driver.find_element_by_link_text("Lupa KataSandi ?").click()

	def test_LupaSandi_empty(self):
		driver = self.driver
		driver.get("https://antrian.imigrasi.go.id")
		driver.find_element_by_link_text("Lupa KataSandi ?").click()
		driver.find_element_by_id("btn-search").click()
		wait = WebDriverWait(driver, 30)
		element = wait.until(EC.element_to_be_clickable((By.ID, 'smallbox1')))		
		assert "Akun Anda Tidak Ditemukan" in driver.page_source

	def test_LupaSandi_email_tdkterdaftar(self):
		driver = self.driver
		driver.get("https://antrian.imigrasi.go.id")
		driver.find_element_by_link_text("Lupa KataSandi ?").click()
		driver.find_element_by_id("request").send_keys("kdlsnmcj@gmail.com")
		driver.find_element_by_id("btn-search").click()
		wait = WebDriverWait(driver, 30)
		element = wait.until(EC.element_to_be_clickable((By.ID, 'smallbox1')))		
		assert "Akun Anda Tidak Ditemukan" in driver.page_source

	def test_LupaSandi_email_terdaftar(self):
		driver = self.driver
		driver.get("https://antrian.imigrasi.go.id")
		driver.find_element_by_link_text("Lupa KataSandi ?").click()
		driver.find_element_by_id("request").send_keys("jdmcsusfe@yahoo.com")
		driver.find_element_by_id("btn-search").click()
		wait = WebDriverWait(driver, 30)
		element = wait.until(EC.element_to_be_clickable((By.ID, 'Msg1')))		
		assert " Email telah dikirim silahkan cek e-mail anda untuk melanjutkan proses reset password, Tekan tombol [Yes] untuk kembali ke halaman utama" in driver.page_source

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