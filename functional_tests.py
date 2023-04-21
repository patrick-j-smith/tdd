from selenium import webdriver
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
        self.fail("Finish the test")

        # User is invited to enter to-do item

        # User types a to-do item into a text box

        # User hitting enter updates the page and lists updated to-do list

        # There is a text box inviting entering a second item User enters second item

        # User hitting enter updates the page and lists updated to-do list

        # Unique list url is created with some explanation text

        # User goes to the unique user url


if __name__ == '__main__':
    unittest.main(warnings='ignore')
