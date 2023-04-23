from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Check out the home page
        self.browser.get('http://localhost:8000')

        # Header mentions the to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is invited to enter to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # User types a to-do item into a text box
        inputbox.send_keys('Buy peacock feathers')

        # User hitting enter updates the page and lists updated to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # There is a text box inviting entering a second item User enters second item
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # User hitting enter updates the page and lists updated to-do list
        self.fail('Finish the test!')

        # Unique list url is created with some explanation text

        # User goes to the unique user url


if __name__ == '__main__':
    unittest.main(warnings='ignore')
