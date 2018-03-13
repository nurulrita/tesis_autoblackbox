from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import os, re, unittest, time

def login(driver):
    driver.get("https://antrian.imigrasi.go.id")
    username = driver.find_element_by_id("Username")
    password = driver.find_element_by_id("Password")
    submit   = driver.find_element_by_id("btn-login")
    username.send_keys("lcfr")
    password.send_keys("1234567890")

    submit.click()
    driver.implicitly_wait(30)
    return driver

class BuatPermohonan(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.verificationErrors = []
		self.accept_next_alert = True

	# def test_buat_permohonan(self):
	# 	driver = login(self.driver) 
	# 	EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
		
	# 	driver.find_element_by_css_selector('#list-kanim > tr:nth-child(1) > td:nth-child(3) > button').click()

	# def test_buat_permohonan_formKosong(self):
	# 	driver = login(self.driver)
	# 	EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))

	# 	driver.find_element_by_css_selector('#list-kanim > tr:nth-child(1) > td:nth-child(3) > button').click()
	# 	driver.find_element_by_css_selector('#btn-lanjut').click()
	# 	driver.find_element_by_css_selector('#btn-lanjut').click()
	# 	driver.find_element_by_css_selector('#btn-lanjut').click()
	# 	driver.find_element_by_id('jumlah_pemohon-error').click()
	# 	assert "(*) Wajib di isi " in driver.page_source

	# def test_buat_permohonan_formIsi(self):
	# 	driver = login(self.driver)
	# 	EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))

	# 	driver.find_element_by_css_selector('#list-kanim > tr:nth-child(1) > td:nth-child(3) > button').click()
	# 	driver.find_element_by_xpath("//form[@id='daftar_jumlah_antrian-form']/fieldset/section/label[2]/i").click()
	# 	time.sleep(2)
	# 	driver.find_element_by_css_selector("#availableDate").click()
	# 	day_from = driver.find_element_by_xpath("//a[contains(text(),'14')]").click()
	# 	time.sleep(5)
		
	# 	driver.find_elements_by_css_selector('#jamkerja > label:nth-child(1)')[0].click()
	# 	select = Select(driver.find_element_by_id('jumlah_pemohon'))
	# 	select.select_by_value('1')
	# 	driver.find_element_by_id("btn-lanjut").click()

	# def test_buat_permohonan_formRegisWizardKosong(self):
	# 	driver = login(self.driver)
	# 	EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))

	# 	driver.find_element_by_css_selector('#list-kanim > tr:nth-child(1) > td:nth-child(3) > button').click()
	# 	driver.find_element_by_xpath("//form[@id='daftar_jumlah_antrian-form']/fieldset/section/label[2]/i").click()
	# 	time.sleep(2)
	# 	driver.find_element_by_css_selector("#availableDate").click()
	# 	day_from = driver.find_element_by_xpath("//a[contains(text(),'14')]").click()
	# 	time.sleep(5)
		
	# 	driver.find_elements_by_css_selector('#jamkerja > label:nth-child(1)')[0].click()
	# 	select = Select(driver.find_element_by_id('jumlah_pemohon'))
	# 	select.select_by_value('1')
	# 	driver.find_element_by_id("btn-lanjut").click()
	# 	driver.find_element_by_id("NAMA_PENGANTRI_1").send_keys("")
	# 	driver.find_element_by_id("NIK_PENGANTRI_1").send_keys("")
	# 	select = Select(driver.find_element_by_id('KET_PENGANTRI_1'))
	# 	select.select_by_value('pribadi')
	# 	driver.find_element_by_id("next-btn").click()

	# def test_buat_permohonan_formRegisWizardNamaKosong(self):
	# 	driver = login(self.driver)
	# 	EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))

	# 	driver.find_element_by_css_selector('#list-kanim > tr:nth-child(1) > td:nth-child(3) > button').click()
	# 	driver.find_element_by_xpath("//form[@id='daftar_jumlah_antrian-form']/fieldset/section/label[2]/i").click()
	# 	time.sleep(2)
	# 	driver.find_element_by_css_selector("#availableDate").click()
	# 	day_from = driver.find_element_by_xpath("//a[contains(text(),'14')]").click()
	# 	time.sleep(5)
		
	# 	driver.find_elements_by_css_selector('#jamkerja > label:nth-child(1)')[0].click()
	# 	select = Select(driver.find_element_by_id('jumlah_pemohon'))
	# 	select.select_by_value('1')
	# 	driver.find_element_by_id("btn-lanjut").click()
	# 	driver.find_element_by_id("NAMA_PENGANTRI_1").send_keys("")
	# 	driver.find_element_by_id("NIK_PENGANTRI_1").send_keys("3276060912900001")
	# 	select = Select(driver.find_element_by_id('KET_PENGANTRI_1'))
	# 	select.select_by_value('pribadi')
	# 	driver.find_element_by_id("next-btn").click()

	# def test_buat_permohonan_formRegisWizardNIKKurang16(self):
	# 	driver = login(self.driver)
	# 	EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))

	# 	driver.find_element_by_css_selector('#list-kanim > tr:nth-child(1) > td:nth-child(3) > button').click()
	# 	driver.find_element_by_xpath("//form[@id='daftar_jumlah_antrian-form']/fieldset/section/label[2]/i").click()
	# 	time.sleep(2)
	# 	driver.find_element_by_css_selector("#availableDate").click()
	# 	day_from = driver.find_element_by_xpath("//a[contains(text(),'14')]").click()
	# 	time.sleep(5)
		
	# 	driver.find_elements_by_css_selector('#jamkerja > label:nth-child(1)')[0].click()
	# 	select = Select(driver.find_element_by_id('jumlah_pemohon'))
	# 	select.select_by_value('1')
	# 	driver.find_element_by_id("btn-lanjut").click()
	# 	driver.find_element_by_id("NAMA_PENGANTRI_1").send_keys("Resa")
	# 	driver.find_element_by_id("NIK_PENGANTRI_1").send_keys("327606")
	# 	select = Select(driver.find_element_by_id('KET_PENGANTRI_1'))
	# 	select.select_by_value('pribadi')
	# 	driver.find_element_by_id("next-btn").click()

	# 	wait = WebDriverWait(driver, 15)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'smallbox1')))
	# 	assert "NIK Wajib 16 Digit" in driver.page_source

	# def test_buat_permohonan_formRegisWizardNIKLebih16(self):
	# 	driver = login(self.driver)
	# 	EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))

	# 	driver.find_element_by_css_selector('#list-kanim > tr:nth-child(1) > td:nth-child(3) > button').click()
	# 	driver.find_element_by_xpath("//form[@id='daftar_jumlah_antrian-form']/fieldset/section/label[2]/i").click()
	# 	time.sleep(2)
	# 	driver.find_element_by_css_selector("#availableDate").click()
	# 	day_from = driver.find_element_by_xpath("//a[contains(text(),'14')]").click()
	# 	time.sleep(5)
		
	# 	driver.find_elements_by_css_selector('#jamkerja > label:nth-child(1)')[0].click()
	# 	select = Select(driver.find_element_by_id('jumlah_pemohon'))
	# 	select.select_by_value('1')
	# 	driver.find_element_by_id("btn-lanjut").click()
	# 	driver.find_element_by_id("NAMA_PENGANTRI_1").send_keys("Resa")
	# 	driver.find_element_by_id("NIK_PENGANTRI_1").send_keys("327606091290000112345")
	# 	select = Select(driver.find_element_by_id('KET_PENGANTRI_1'))
	# 	select.select_by_value('pribadi')
	# 	driver.find_element_by_id("next-btn").click()

	# 	wait = WebDriverWait(driver, 15)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'smallbox1')))
	# 	assert "NIK Wajib 16 Digit" in driver.page_source

	# *********** Kombinasi tidak bisa, kolom nik tidak bisa dimasukkan huruf ************
	# def test_buat_permohonan_formRegisWizardNIKKombinasi(self):
	# 	driver = login(self.driver)
	# 	EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))

	# 	driver.find_element_by_css_selector('#list-kanim > tr:nth-child(1) > td:nth-child(3) > button').click()
	# 	driver.find_element_by_xpath("//form[@id='daftar_jumlah_antrian-form']/fieldset/section/label[2]/i").click()
	# 	time.sleep(2)
	# 	driver.find_element_by_css_selector("#availableDate").click()
	# 	day_from = driver.find_element_by_xpath("//a[contains(text(),'14')]").click()
	# 	time.sleep(5)
		
	# 	driver.find_elements_by_css_selector('#jamkerja > label:nth-child(1)')[0].click()
	# 	select = Select(driver.find_element_by_id('jumlah_pemohon'))
	# 	select.select_by_value('1')
	# 	driver.find_element_by_id("btn-lanjut").click()
	# 	driver.find_element_by_id("NAMA_PENGANTRI_1").send_keys("Resa")
	# 	driver.find_element_by_id("NIK_PENGANTRI_1").send_keys("32760609129abcf1")
	# 	select = Select(driver.find_element_by_id('KET_PENGANTRI_1'))
	# 	select.select_by_value('pribadi')
	# 	driver.find_element_by_id("next-btn").click()

	# 	wait = WebDriverWait(driver, 15)
	# 	element = wait.until(EC.element_to_be_clickable((By.ID, 'smallbox1')))
	# 	assert "NIK Tidak Valid" in driver.page_source
	# **************************************************************************************


	def test_buat_permohonan_formIsiSukses(self):
		driver = login(self.driver)
		EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))

		driver.find_element_by_css_selector('#list-kanim > tr:nth-child(1) > td:nth-child(3) > button').click()
		driver.find_element_by_xpath("//form[@id='daftar_jumlah_antrian-form']/fieldset/section/label[2]/i").click()
		time.sleep(2)
		driver.find_element_by_css_selector("#availableDate").click()
		day_from = driver.find_element_by_xpath("//a[contains(text(),'14')]").click()
		time.sleep(5)
		
		driver.find_elements_by_css_selector('#jamkerja > label:nth-child(1)')[0].click()
		select = Select(driver.find_element_by_id('jumlah_pemohon'))
		select.select_by_value('1')
		driver.find_element_by_id("btn-lanjut").click()


		driver.find_element_by_id("NAMA_PENGANTRI_1").send_keys("Resa")
		driver.find_element_by_id("NIK_PENGANTRI_1").send_keys("3276061012910001")
		select = Select(driver.find_element_by_id('KET_PENGANTRI_1'))
		select.select_by_value('pribadi')
		driver.find_element_by_id("next-btn").click()
		driver.find_element_by_id("next-btn").click()
		wait = WebDriverWait(driver, 15)
		element = wait.until(EC.element_to_be_clickable((By.ID, 'smallbox1')))
		assert "Permohonan Berhasil Dikirim, Cek Daftar Permohonan" in driver.page_source

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



