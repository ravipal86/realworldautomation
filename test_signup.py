import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class QureAISignUpTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("http://demo.realworld.io/")
        time.sleep(3)


    def test_signup_fail(self):

        signup_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign up')]")
        signup_lnk.click()
        time.sleep(3)

        username = self.driver.find_element_by_xpath(".//input[@type='text']");
        email = self.driver.find_element_by_xpath(".//input[@type='email']");
        password = self.driver.find_element_by_xpath(".//input[@type='password']");
        signup_btn = self.driver.find_element_by_xpath(".//button[@type='submit']");

        username.send_keys('ravipal')
        email.send_keys('ravi.pal@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(self.is_element_present(By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(self.click_element(signup_btn))
        time.sleep(3)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]")
        self.assertEqual("ravipal16", profile_name.text, "profile username is not matching")

        time.sleep(3)

	
    def test_signup_pass(self):

        signup_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign up')]")
        signup_lnk.click()
        time.sleep(3)

        username = self.driver.find_element_by_xpath(".//input[@type='text']")
        email = self.driver.find_element_by_xpath(".//input[@type='email']")
        password = self.driver.find_element_by_xpath(".//input[@type='password']")
        signup_btn = self.driver.find_element_by_xpath(".//button[@type='submit']")

        username.send_keys('ravipal20')
        email.send_keys('ravi.pal20@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(self.is_element_present(By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(self.click_element(signup_btn))
        time.sleep(3)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]")
        print(profile_name.text)
        self.assertEqual("ravipal20", profile_name.text, "profile username is not matching")

        time.sleep(3)


    def tearDown(self):
        self.driver.close()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def click_element(self, webelement):
        try: webelement.click()
        except NoSuchElementException as e: return False
        return True

if __name__ == "__main__":
    unittest.main()



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://www.python.org")
# print(driver.title)
# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
# driver.close()