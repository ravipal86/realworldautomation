import time
import unittest
from utils import Utils
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

        self.assertTrue(Utils.is_element_present(self, By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(Utils.click_element(self, signin_btn))
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

        self.assertTrue(Utils.is_element_present(self, By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(Utils.click_element(self, signin_btn))
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
        self.assertTrue(Utils.is_element_present(self, By.XPATH, ".//li[@ng-repeat='error in errors']"))

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

        self.assertTrue(Utils.is_element_present(self, By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(Utils.click_element(self, signin_btn))
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
        self.assertTrue(Utils.scroll_to_element(self, comment_submit), "Element not present")

        comment_txtbox = self.driver.find_element_by_xpath(".//textarea[@ng-model='$ctrl.commentForm.body']")
        comment_txtbox.send_keys(comment_text)

        comment_submit.click()

        time.sleep(3)

        posted_comment = self.driver.find_element_by_xpath(".//comment/div/div[@class='card-block']/p")
        self.assertEqual(comment_text, posted_comment.text, "comment not matching after post")

        time.sleep(3)


    def test_tags_on_article(self):

        signin_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign in')]")
        self.assertTrue(Utils.click_element(self, signin_lnk))
        time.sleep(3)

        email = self.driver.find_element_by_xpath(".//input[@type='email']")
        password = self.driver.find_element_by_xpath(".//input[@type='password']")
        signin_btn = self.driver.find_element_by_xpath(".//button[@type='submit']")

        email.send_keys('ravi.pal20@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(Utils.is_element_present(self, By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(Utils.click_element(self, signin_btn))
        time.sleep(3)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]").text
        self.assertEqual("ravipal20", profile_name, "profile username is not matching")

        time.sleep(3)

        self.assertTrue(Utils.is_element_present(self, By.XPATH, ".//div[@class='sidebar']"))

        first_tag = self.driver.find_elements_by_xpath(".//div[@class='sidebar']/div[@class='tag-list']/a")[0]
        first_tag.click()

        time.sleep(3)

        last_feed_list = self.driver.find_elements_by_xpath(".//div[@class='feed-toggle']/ul/li/a")[-1]

        self.assertEqual(first_tag.text, last_feed_list.text, "tag listing is matching")

        article_tags = self.driver.find_elements_by_xpath(".//div[@class='article-preview']/a/ul/li")
        self.assertTrue(Utils.search_tag(self, article_tags, last_feed_list.text), "tag not on the article")


    def test_fav_count_on_article(self):

        signin_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign in')]")
        self.assertTrue(Utils.click_element(self, signin_lnk))
        time.sleep(3)

        email = self.driver.find_element_by_xpath(".//input[@type='email']")
        password = self.driver.find_element_by_xpath(".//input[@type='password']")
        signin_btn = self.driver.find_element_by_xpath(".//button[@type='submit']")

        email.send_keys('ravi.pal20@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(Utils.is_element_present(self, By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(Utils.click_element(self, signin_btn))
        time.sleep(3)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]").text
        self.assertEqual("ravipal20", profile_name, "profile username is not matching")

        time.sleep(3)

        global_feeds = self.driver.find_element_by_xpath(".//a[contains(text(),'Global Feed')]")
        global_feeds.click()

        time.sleep(3)

        first_article_on_feed = self.driver.find_elements_by_xpath(".//article-preview")[1]
        fav_count_before = first_article_on_feed.find_element_by_xpath(".//ng-transclude//ng-transclude/span").text

        fav_icon_btn = first_article_on_feed.find_element_by_xpath(".//ng-transclude//button")
        fav_icon_btn.click()

        time.sleep(3)

        fav_count_after = first_article_on_feed.find_element_by_xpath(".//ng-transclude//ng-transclude/span").text

        self.assertEqual(int(fav_count_before) + 1, int(fav_count_after), "fav article count did not increased")


    def test_follow_author_of_article(self):

        signin_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign in')]")
        self.assertTrue(Utils.click_element(self, signin_lnk))
        time.sleep(3)

        email = self.driver.find_element_by_xpath(".//input[@type='email']")
        password = self.driver.find_element_by_xpath(".//input[@type='password']")
        signin_btn = self.driver.find_element_by_xpath(".//button[@type='submit']")

        email.send_keys('ravi.pal12@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(Utils.is_element_present(self, By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(Utils.click_element(self, signin_btn))
        time.sleep(3)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]").text
        self.assertEqual("ravipal12", profile_name, "profile username is not matching")

        time.sleep(3)

        global_feeds = self.driver.find_element_by_xpath(".//a[contains(text(),'Global Feed')]")
        global_feeds.click()

        time.sleep(3)

        global_feeds = self.driver.find_element_by_xpath(".//a[contains(text(),'Global Feed')]")
        global_feeds.click()

        time.sleep(3)

        last_article_on_feed = self.driver.find_elements_by_xpath(".//article-preview")[-1]
        self.assertTrue(Utils.scroll_to_element(self, last_article_on_feed), "Element not present")

        author_name = last_article_on_feed.find_element_by_xpath("//div[@class='info']/a[contains(@class,'author')]")
        author_name.click()

        time.sleep(3)

        follow_btn = self.driver.find_element_by_xpath(".//follow-btn/button")
        follow_btn.click()

        time.sleep(3)

    def test_edit_article(self):

        new_article_body_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius."

        signin_lnk = self.driver.find_element_by_xpath(".//a[contains(text(),'Sign in')]")
        self.assertTrue(Utils.click_element(self, signin_lnk))
        time.sleep(3)

        email = self.driver.find_element_by_xpath(".//input[@type='email']")
        password = self.driver.find_element_by_xpath(".//input[@type='password']")
        signin_btn = self.driver.find_element_by_xpath(".//button[@type='submit']")

        email.send_keys('ravi.pal19@gmail.com')
        password.send_keys('password@123')

        self.assertTrue(Utils.is_element_present(self, By.XPATH, ".//button[@type='submit']"))

        self.assertTrue(Utils.click_element(self, signin_btn))
        time.sleep(5)


        profile_name = self.driver.find_element_by_xpath(".//a[contains(@ui-sref,'app.profile.main')]")
        self.assertEqual("ravipal19", profile_name.text, "profile username is not matching")

        time.sleep(3)

        profile_name.click()

        time.sleep(3)

        first_article_on_feed = self.driver.find_element_by_xpath(".//article-preview")
        read_more = first_article_on_feed.find_element_by_xpath(".//span[contains(text(),'Read more')]")
        read_more.click()

        time.sleep(3)

        article_prev_text = self.driver.find_element_by_xpath(".//div[@ng-bind-html='::$ctrl.article.body']").text

        edit_article_btn = self.driver.find_elements_by_xpath(".//article-actions//ng-transclude/span/a[@ui-sref='app.editor({ slug: $ctrl.article.slug })']")[0]
        edit_article_btn.click()

        time.sleep(3)

        article_body = self.driver.find_element_by_xpath(".//textarea[@ng-model='$ctrl.article.body']")
        article_body.send_keys(new_article_body_text)

        article_submit = self.driver.find_element_by_xpath(".//button[@type='button']")
        article_submit.click()

        time.sleep(3)

        article_update_text = self.driver.find_element_by_xpath(".//div[@ng-bind-html='::$ctrl.article.body']").text

        self.assertTrue(article_update_text, new_article_body_text)

        time.sleep(3)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()