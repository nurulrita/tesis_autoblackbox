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

class DaftarPermohonan(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_daftar_permohonan(self):
		driver = login(self.driver)
		driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")
		driver.find_element_by_css_selector("a[title=\"Daftar Pemohonan\"]").click()

	# def test_daftar_permohonan_kodeAntrian(self):
	# 	driver = login(self.driver)
	# 	driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")
	# 	driver.find_element_by_css_selector("a[title=\"Daftar Pemohonan\"]").click()

	# 	driver.find_element_by_xpath ("readbarcode({"MU_ALAMAT":null,"StartHour":1300,"MP_NAME":null,"MP_NAME_IN":null,"MT_TANGGAL":null,"MQ_CREATED_DATE":"Jan 18, 2018 12:27:14 PM","IS_ACTIVE":true,"MO_CLASS":null,"NO_ANTRIAN":"null-082H9I","ProvinceName":"Bangka Belitung Islands","MQ_UID":1000667543,"STATUS":0,"ServiceDate":"Jan 26, 2018","ProvinceId":3,"data_qr":"F9vVhsO5beLpYzmuaVAUcuG7m5FYDEalqH1b6daoZ70uwpuh6rGaDbk0z5Gjsr1jbxRS/llYldHN/7uag9KxvpPIc8cHrEL6GDvcPSWgNnK3zCTDeGssLF+4Y94CO/lHkNZ6de//il2Azjg5k5hoVHn1zyqkZQp5Wx1FP//ttsRvsIjDMfq9ocu2noKlB3vb7FIDAu42cfpN8eNAaX7nivhz0lluyZ4a85AvO6q8BLFmQzSyKxiHGKjL1x332xBSrqmo0bHl4KijOQQkS7mJjXiRQj3nKKs8YaQOHQpp+lQ6kn7inwi6NPCLQLhQvujKZg4AXmeug1jNvLXj3F+xFa1prsZWb/T0q3qCF1aZ+RrhQAnXX3FqYnmTz/SmwrXAzzhu6Q/2Jdcafj8a5iJMCJhAVuW9vQBW7RD3IM6K9Hw=","EndHour":1400,"MQ_TDID":49965,"MU_EMAIL":null,"MO_ADDRESS":"JL. Jendral Sudirman Km. 6, 5, 33413, Pangkal Lalang, Tj. Pandan, Kabupaten Belitung, Kepulauan Bangka Belitung 33413","KET_PENGANTRI":"","MO_NAME":null,"NAMA_PENGANTRI":"Andra","OfficeId":12,"MU_USERNAME":null,"NIK_PENGANTRI":"3276060912900001","MT_MULAI":null,"MQ_ID":659482,"MT_SELESAI":null,"UserId":null,"OfficeName":"Kantor Imigrasi Tanjung Pandan"})").click()

	# def test_daftar_permohonan_batalkan(self):
	# 	driver = login(self.driver)
	# 	driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")
	# 	driver.find_element_by_css_selector("a[title=\"Daftar Pemohonan\"]").click()

	# 	driver.find_element_by_id("btn-hapus_null-082H9I").click()
	# 	driver.execute_script("window.alert('Pemohon Hanya diperbolehkan membatalkan Antrian ');")
	# 	alert = driver.switch_to_alert()
	# 	alert.accept()
	# 	driver.find_element_by_id("bot1-Msg1").click()
	# 	driver.get ("https://antrian.imigrasi.go.id/Index.jsp#Ajax/User/Daftar_Permohonan.jsp")


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