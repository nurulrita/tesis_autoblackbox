from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

def pendaftaran(driver):
	driver.get ("https://antrian.imigrasi.go.id")
	driver.find_element_by_link_text("Pendaftaran !").click()

	return driver

class PendaftaranFirefox(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "https://antrian.imigrasi.go.id"
		self.verificationErrors = []
		self.accept_next_alert = True

	# def test_Pendaftaran(self):
	# 	driver = self.driver
	# 	driver.get(self.base_url + "/Authentication.jsp")
	# 	driver.find_element_by_link_text("Pendaftaran !").click()

	# def test_PendaftaranEmpty(self):
	# 	driver = pendaftaran(self.driver)

	# 	driver.find_element_by_id("register-btn_save").click()
	# 	assert "(*) Wajib di isi " in driver.page_source

	# def test_PendaftaranUsernameEmpty(self):
	# 	driver = pendaftaran(self.driver)

	# 	driver.find_element_by_name("Username").send_keys("")
	# 	driver.find_element_by_name("Password").send_keys("12345")
	# 	driver.find_element_by_name("NIK").send_keys("1234567891234567")
	# 	driver.find_element_by_name("Telephone").send_keys("081234567890")
	# 	driver.find_element_by_name("Email").send_keys("qwertyayzx@gmail.com")
	# 	driver.find_element_by_name("Alamat").send_keys("Jl. Kenanga")
	# 	driver.find_element_by_id("register-btn_save").click()
	# 	assert "(*) Wajib di isi " in driver.page_source

	# def test_PendaftaranPasswordEmpty(self):
	# 	driver = pendaftaran(self.driver)

	# 	driver.find_element_by_name("Username").send_keys("")
	# 	driver.find_element_by_name("Password").send_keys("")
	# 	driver.find_element_by_name("NIK").send_keys("1234567891234567")
	# 	driver.find_element_by_name("Telephone").send_keys("081234567890")
	# 	driver.find_element_by_name("Email").send_keys("qwertyayzx@gmail.com")
	# 	driver.find_element_by_name("Alamat").send_keys("Jl. Kenanga")
	# 	driver.find_element_by_id("register-btn_save").click()
	# 	assert "(*) Wajib di isi " in driver.page_source

	# def test_PendaftaranNIKEmpty(self):
	# 	driver = pendaftaran(self.driver)

	# 	driver.find_element_by_name("Username").send_keys("")
	# 	driver.find_element_by_name("Password").send_keys("")
	# 	driver.find_element_by_name("NIK").send_keys("")
	# 	driver.find_element_by_name("Telephone").send_keys("081234567890")
	# 	driver.find_element_by_name("Email").send_keys("qwertyayzx@gmail.com")
	# 	driver.find_element_by_name("Alamat").send_keys("Jl. Kenanga")
	# 	driver.find_element_by_id("register-btn_save").click()
	# 	assert "(*) Wajib di isi " in driver.page_source

	# def test_PendaftaranTeleponEmpty(self):
	# 	driver = pendaftaran(self.driver)

	# 	driver.find_element_by_name("Username").send_keys("")
	# 	driver.find_element_by_name("Password").send_keys("")
	# 	driver.find_element_by_name("NIK").send_keys("")
	# 	driver.find_element_by_name("Telephone").send_keys("")
	# 	driver.find_element_by_name("Email").send_keys("qwertyayzx@gmail.com")
	# 	driver.find_element_by_name("Alamat").send_keys("Jl. Kenanga")
	# 	driver.find_element_by_id("register-btn_save").click()
	# 	assert "(*) Wajib di isi " in driver.page_source

	# def test_PendaftaranEmailEmpty(self):
	# 	driver = pendaftaran(self.driver)

	# 	driver.find_element_by_name("Username").send_keys("")
	# 	driver.find_element_by_name("Password").send_keys("")
	# 	driver.find_element_by_name("NIK").send_keys("")
	# 	driver.find_element_by_name("Telephone").send_keys("")
	# 	driver.find_element_by_name("Email").send_keys("")
	# 	driver.find_element_by_name("Alamat").send_keys("Jl. Kenanga")
	# 	driver.find_element_by_id("register-btn_save").click()
	# 	assert "(*) Wajib di isi " in driver.page_source

	# def test_PendaftaranPassKurang4(self):
	# 	driver = pendaftaran(self.driver)

	# 	driver.find_element_by_name("Username").send_keys("abcd")
	# 	driver.find_element_by_name("Password").send_keys("123")
	# 	driver.find_element_by_name("NIK").send_keys("3275050808910002")
	# 	driver.find_element_by_name("Telephone").send_keys("0812345690")
	# 	driver.find_element_by_name("Email").send_keys("bjvs@yahoo.com")
	# 	driver.find_element_by_name("Alamat").send_keys("Jl. Mawar")
	# 	driver.find_element_by_id("register-btn_save").click()
	# 	assert "password minimal 6 digit " in driver.page_source

	# def test_PendaftaranNIKKurang16(self):
	# 	driver = pendaftaran(self.driver)

	# 	driver.find_element_by_name("Username").send_keys("mkng")
	# 	driver.find_element_by_name("Password").send_keys("zxcvbnm")
	# 	driver.find_element_by_name("NIK").send_keys("32750508089")
	# 	driver.find_element_by_name("Telephone").send_keys("08128909876")
	# 	driver.find_element_by_name("Email").send_keys("lkmkl@yahoo.com")
	# 	driver.find_element_by_name("Alamat").send_keys("Jl. Mawar")
	# 	driver.find_element_by_id("register-btn_save").click()
	# 	assert "Error in executeUpdate, NIK user tidak valid. " in driver.page_source

	# def test_PendaftaranNIKLebih16(self):
	# 	driver = pendaftaran(self.driver)

	# 	driver.find_element_by_name("Username").send_keys("mkng")
	# 	driver.find_element_by_name("Password").send_keys("zxcvbnm")
	# 	driver.find_element_by_name("NIK").send_keys("327505080890938492023")
	# 	driver.find_element_by_name("Telephone").send_keys("08128909876")
	# 	driver.find_element_by_name("Email").send_keys("lkmkl@yahoo.com")
	# 	driver.find_element_by_name("Alamat").send_keys("Jl. Mawar")
	# 	driver.find_element_by_id("register-btn_save").click()
	# 	assert "Error in executeUpdate, NIK user tidak valid. " in driver.page_source

	def test_PendaftaranTeleponUsed(self):
		driver = pendaftaran(self.driver)

		driver.find_element_by_name("Username").send_keys("mkng")
		driver.find_element_by_name("Password").send_keys("zxcvbnm")
		driver.find_element_by_name("NIK").send_keys("3275050808910002")
		driver.find_element_by_name("Telephone").send_keys("081234567890")
		driver.find_element_by_name("Email").send_keys("lkmkl@yahoo.com")
		driver.find_element_by_name("Alamat").send_keys("Jl. Mawar")
		driver.find_element_by_id("register-btn_save").click()
		assert "Nomer Telephone Telah Digunakan " in driver.page_source

	# def test_PendaftaranBerhasil(self):
	# 	driver = pendaftaran(self.driver)

	# 	driver.find_element_by_name("Username").send_keys("mtomu")
	# 	driver.find_element_by_name("Password").send_keys("asdfghijkl")
	# 	driver.find_element_by_name("NIK").send_keys("3276064808880001")
	# 	driver.find_element_by_name("Telephone").send_keys("082345671092")
	# 	driver.find_element_by_name("Email").send_keys("mtomu@yahoo.com")
	# 	driver.find_element_by_name("Alamat").send_keys("Jl. Markisa")
	# 	driver.find_element_by_id("register-btn_save").click()
	# 	driver.get("https://antrian.imigrasi.go.id/Index.jsp#Ajax/Home/Index.jsp")

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