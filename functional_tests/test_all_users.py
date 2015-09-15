#coding: utf-8
from selenium.webdriver.firefox import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase
from django.utils.translation import activate

class HomeNewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.WebDriver()
        self.browser.implicitly_wait(5)
        activate('en')

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self,namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("TaskBuster", self.browser.title)

    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"), "rgba(0, 0, 0, 1)")

    def test_home_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Page Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Page Not Found", self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
