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

class PlaceTest(LiveServerTestCase):
    #doesn't work and I'm not sure why

    fixtures = ['test_places']

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_add_note_page(self):
        self.browser.get(self.live_server_url)
        visited = self.browser.find_element_by_id('places_visited_link')
        visited.click()

        wait_for_place_three = self.browser.find_element_by_id('place-3')
        wait_for_place_three.click()

        wait_for_date = self.browser.find_element_by_name('visited_date')
        wait_for_date.clear()   # this place already has a date visited and there's already text in the date input. 
        wait_for_date.send_keys('2015-04-03 00:00:00')  # if there's already text, this will be appended to it.
        wait_for_note = self.browser.find_element_by_name('note')
        wait_for_note.send_keys('a more unique string of text')   # it's possible 'text' is already in the page, common word in HTML pages
        save = self.browser.find_element_by_id('place_save_form_button')
        save.click()

        assert 'a more unique string of text' in self.browser.page_source
