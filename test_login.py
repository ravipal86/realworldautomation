import time
import unittest
from utils import Utils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class QureAISignInTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("http://demo.realworld.io/")
        time.sleep(3)


    def test_signin_fail(self):

        signin_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign in')]")
        signin_lnk.click()
        time.sleep(3)

        email = self.driver.find_element_by_xpath(".//input[@type='email']")
        password = self.driver.find_element_by_xpath(".//input[@type='password']")
        signin_btn = self.driver.find_element_by_xpath(".//button[@type='submit']")

        email.send_keys('ravi.pal@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(Utils.is_element_present(self ,By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(Utils.click_element(self, signin_btn))
        time.sleep(3)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]").text
        self.assertNotEqual("ravipal17", profile_name, "profile username is not matching")

        time.sleep(3)

	
    def test_signin_pass(self):

        signin_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign in')]")
        signin_lnk.click()
        time.sleep(3)

        email = self.driver.find_element_by_xpath(".//input[@type='email']")
        password = self.driver.find_element_by_xpath(".//input[@type='password']")
        signin_btn = self.driver.find_element_by_xpath(".//button[@type='submit']")

        email.send_keys('ravi.pal20@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(Utils.is_element_present(self ,By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(Utils.click_element(self, signin_btn))
        time.sleep(3)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]").text
        self.assertEqual("ravipal20", profile_name, "profile username is not matching")

        time.sleep(3)


    def test_signout_pass(self):

        signin_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign in')]")
        signin_lnk.click()
        time.sleep(3)

        email = self.driver.find_element_by_xpath(".//input[@type='email']")
        password = self.driver.find_element_by_xpath(".//input[@type='password']")
        signin_btn = self.driver.find_element_by_xpath(".//button[@type='submit']")

        email.send_keys('ravi.pal20@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(Utils.is_element_present(self ,By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(Utils.click_element(self, signin_btn))
        time.sleep(3)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]").text
        self.assertEqual("ravipal20", profile_name, "profile username is not matching")

        time.sleep(3)

        profile_settings = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.settings')]")
        profile_settings.click()

        time.sleep(3)

        logout_btn = self.driver.find_element_by_xpath(".//button[contains(text(),'Or click here to logout.')]")
        self.assertTrue(Utils.scroll_to_element(self, logout_btn), "Element not present")
        logout_btn.click()

        time.sleep(3)

        self.assertTrue(Utils.is_element_present(self ,By.XPATH, ".//a[contains(text(),'Sign in')]"))

        time.sleep(3)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()