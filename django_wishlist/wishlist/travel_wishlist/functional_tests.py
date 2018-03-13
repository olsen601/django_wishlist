import selenium
from selenium import webdriver

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_shown_on_home_page(self):
        self.browser.get(self.live_server_url)
        assert 'Wishlist' in self.browser.title

class FunctionalityTests(LiveServerTestCase):

    fixtures = ['test_places']

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_add_new_place(self):
        self.browser.get(self.live_server_url)
        input_name = self.browser.find_element_by_id('id_name')
        input_name.send_keys('Denver')
        add_button = self.browser.find_element_by_id('add-new-place')
        add_button.click()

        wait_for_denver = self.browser.find_element_by_id('place-name-5')

        assert 'Tokyo' in self.browser.page_source
        assert 'New York' in self.browser.page_source

        assert 'Denver' in self.browser.page_source
