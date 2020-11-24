import unittest
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("https://cometshare.com/signin")
        inst.driver.title

    def testOne(self):
        email = self.driver.find_element_by_id('email')
        password = self.driver.find_element_by_id('password')
        email.send_keys("Appolo@gmail.com")
        password.send_keys("passwor")

        self.driver.find_element_by_id('sign-in-button').click()
        text = self.driver.find_element_by_class_name('jss8')

        self.assertEqual(
            'Incorrect password. Please try again or contact us!', text.text)

        self.driver.refresh()

    def test_search_by_name(self):
        email = self.driver.find_element_by_id('email')
        password = self.driver.find_element_by_id('password')
        email.send_keys("Appolo@gmail.com")
        password.send_keys("passwor")

        self.driver.find_element_by_id('sign-in-button').click()
        text = self.driver.find_element_by_class_name('jss8')

        self.assertEqual(
            'Incorrect password. Please try again or contact us!', text.text)
        self.driver.refresh()

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        return


if __name__ == '__main__':
    unittest.main()
