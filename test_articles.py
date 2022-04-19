import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class QureAIArticleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("http://demo.realworld.io/")
        time.sleep(3)


    def test_create_new_article(self):

        signin_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign in')]")
        signin_lnk.click()
        time.sleep(3)

        email = self.driver.find_element_by_xpath(".//input[@type='email']")
        password = self.driver.find_element_by_xpath(".//input[@type='password']")
        signin_btn = self.driver.find_element_by_xpath(".//button[@type='submit']")

        email.send_keys('ravi.pal20@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(self.is_element_present(By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(self.click_element(signin_btn))
        time.sleep(3)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]").text
        self.assertEqual("ravipal20", profile_name, "profile username is not matching")

        time.sleep(3)

        article_lnk = self.driver.find_element_by_xpath(".//li/a[@ui-sref='app.editor']")
        article_lnk.click()

        time.sleep(3)

        article_title = self.driver.find_element_by_xpath(".//input[@ng-model='$ctrl.article.title']")
        article_title.send_keys("Hello World 1")

        article_desc = self.driver.find_element_by_xpath(".//input[@ng-model='$ctrl.article.description']")
        article_desc.send_keys("Hello World description")

        article_body = self.driver.find_element_by_xpath(".//textarea[@ng-model='$ctrl.article.body']")
        article_body.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

        article_tag = self.driver.find_element_by_xpath(".//input[@ng-model='$ctrl.article.description']")
        article_tag.send_keys("introduction")

        article_submit = self.driver.find_element_by_xpath(".//button[@type='button']")
        article_submit.click()

        time.sleep(3)


    def test_create_new_article_with_same_name(self):

        signin_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign in')]")
        signin_lnk.click()
        time.sleep(3)

        email = self.driver.find_element_by_xpath(".//input[@type='email']")
        password = self.driver.find_element_by_xpath(".//input[@type='password']")
        signin_btn = self.driver.find_element_by_xpath(".//button[@type='submit']")

        email.send_keys('ravi.pal20@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(self.is_element_present(By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(self.click_element(signin_btn))
        time.sleep(3)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]").text
        self.assertEqual("ravipal20", profile_name, "profile username is not matching")

        time.sleep(3)

        article_lnk = self.driver.find_element_by_xpath(".//li/a[@ui-sref='app.editor']")
        article_lnk.click()

        time.sleep(3)

        article_title = self.driver.find_element_by_xpath(".//input[@ng-model='$ctrl.article.title']")
        article_title.send_keys("Hello World 1")

        article_desc = self.driver.find_element_by_xpath(".//input[@ng-model='$ctrl.article.description']")
        article_desc.send_keys("Hello World description")

        article_body = self.driver.find_element_by_xpath(".//textarea[@ng-model='$ctrl.article.body']")
        article_body.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

        article_tag = self.driver.find_element_by_xpath(".//input[@ng-model='$ctrl.article.description']")
        article_tag.send_keys("introduction")

        article_submit = self.driver.find_element_by_xpath(".//button[@type='button']")
        article_submit.click()

        time.sleep(3)

        article_title_error = self.driver.find_element_by_xpath(".//li[@ng-repeat='error in errors']")
        self.assertTrue(self.is_element_present(By.XPATH, ".//li[@ng-repeat='error in errors']"))

        self.assertEqual("title must be unique", article_title_error.text, "article title is not unique")
        time.sleep(3)


	
    def test_comment_on_article(self):

        comment_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

        signin_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign in')]")
        signin_lnk.click()
        time.sleep(3)

        email = self.driver.find_element_by_xpath(".//input[@type='email']")
        password = self.driver.find_element_by_xpath(".//input[@type='password']")
        signin_btn = self.driver.find_element_by_xpath(".//button[@type='submit']")

        email.send_keys('ravi.pal20@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(self.is_element_present(By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(self.click_element(signin_btn))
        time.sleep(3)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]").text
        self.assertEqual("ravipal20", profile_name, "profile username is not matching")

        time.sleep(3)

        article_lnk = self.driver.find_element_by_xpath(".//li/a[@ui-sref='app.editor']")
        article_lnk.click()

        time.sleep(3)

        article_title = self.driver.find_element_by_xpath(".//input[@ng-model='$ctrl.article.title']")
        article_title.send_keys("Hello World 23")

        article_desc = self.driver.find_element_by_xpath(".//input[@ng-model='$ctrl.article.description']")
        article_desc.send_keys("Hello World 11 description")

        article_body = self.driver.find_element_by_xpath(".//textarea[@ng-model='$ctrl.article.body']")
        article_body.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

        article_tag = self.driver.find_element_by_xpath(".//input[@ng-model='$ctrl.tagField']")
        article_tag.send_keys("welcome")

        article_submit = self.driver.find_element_by_xpath(".//button[@type='button']")
        article_submit.click()

        time.sleep(5)

        comment_submit = self.driver.find_element_by_xpath(".//button[@type='submit']")
        self.assertTrue(self.scroll_to_element(comment_submit), "Element not present")

        comment_txtbox = self.driver.find_element_by_xpath(".//textarea[@ng-model='$ctrl.commentForm.body']")
        comment_txtbox.send_keys(comment_text)

        comment_submit.click()

        time.sleep(3)

        posted_comment = self.driver.find_element_by_xpath(".//comment/div/div[@class='card-block']/p")
        self.assertEqual(comment_text, posted_comment.text, "comment not matching after post")

        time.sleep(3)

    def test_tags_on_article(self):

        signin_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign in')]")
        signin_lnk.click()
        time.sleep(3)

        email = self.driver.find_element_by_xpath(".//input[@type='email']")
        password = self.driver.find_element_by_xpath(".//input[@type='password']")
        signin_btn = self.driver.find_element_by_xpath(".//button[@type='submit']")

        email.send_keys('ravi.pal20@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(self.is_element_present(By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(self.click_element(signin_btn))
        time.sleep(3)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]").text
        self.assertEqual("ravipal20", profile_name, "profile username is not matching")

        time.sleep(3)

        self.assertTrue(self.is_element_present(By.XPATH, ".//div[@class='sidebar']"))

        first_tag = self.driver.find_elements_by_xpath(".//div[@class='sidebar']/div[@class='tag-list']/a")[0]
        first_tag.click()

        time.sleep(3)

        last_feed_list = self.driver.find_elements_by_xpath(".//div[@class='feed-toggle']/ul/li/a")[-1]

        self.assertEqual(first_tag.text, last_feed_list.text, "tag listing is matching")

        article_tags = self.driver.find_elements_by_xpath(".//div[@class='article-preview']/a/ul/li")
        self.assertTrue(self.search_tag(article_tags, last_feed_list.text), "tag not on the article")


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

    def scroll_to_element(self, webelement):
        try: self.driver.execute_script("arguments[0].scrollIntoView();", webelement)
        except NoSuchElementException as e: return False
        return True

    def search_tag(self, list, tag):
        for i in range(len(list)):
            if list[i].text == tag:
                return True
            return False

if __name__ == "__main__":
    unittest.main()