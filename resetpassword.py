from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options

import os, re, unittest, time

class ResetPasswordFirefox(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.verificationErrors = []
		self.accept_next_alert = True

	def reset_password_empty(self):
		driver = self.driver
		driver.get("https://antrian.imigrasi.go.id/Layanan/Resetpass.jsp?") 
		driver.find_element_by_id("btn-reset").click()
		assert "Masukkan Password Baru Anda" and "Konfirmasi Password Anda" in driver.page_source

	def reset_password_KonfirmPassEmpty(self):
		driver = self.driver
		driver.get("https://antrian.imigrasi.go.id/Layanan/Resetpass.jsp?1000667543")
		driver.find_element_by_name("inpPassword").send_keys("mtomu")
		driver.find_element_by_name("cnfPassword").send_keys("")
		driver.find_element_by_id("btn-reset").click()
		assert "Konfirmasi Password Anda" in driver.page_source
	
	# def reset_password_KonfirmPassTdkSama(self):
	# 	driver = self.driver
	# 	driver.get("https://antrian.imigrasi.go.id/Layanan/Resetpass.jsp?1000667543")
	# 	driver.find_element_by_name("inpPassword").send_keys("mtomu")
	# 	driver.find_element_by_name("cnfPassword").send_keys("")
	# 	driver.find_element_by_id("btn-reset").click()
	# 	assert "Password Tidak sama" in driver.page_source
	
	# def reset_password_Berhasil(self):
	# 	driver = self.driver
	# 	driver.get("https://antrian.imigrasi.go.id/Layanan/Resetpass.jsp?1000667543")
	# 	driver.find_element_by_name("inpPassword").send_keys("mtomu")
	# 	driver.find_element_by_name("cnfPassword").send_keys("")
	# 	driver.find_element_by_id("btn-reset").click()
	# 	driver.execute_script("window.alert('Password anda telah berhasil dirubah, Tekan tombol [Yes] Untuk Login');")
	# 	alert = driver.switch_to_alert()
	# 	alert.accept()
	# 	driver.find_element_by_id('bot2-Msg1').click()

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

# Password anda telah berhasil dirubah, Tekan tombol [Yes] Untuk Login
# https://antrian.imigrasi.go.id/Layanan/