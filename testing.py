import unittest
from selenium import webdriver


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

    # (A2,B1) Empty Email
    # Ram Karri
    # Should display "Please make sure your inputs are not empty!"
    def test_uempty_email(self):
        email = self.driver.find_element_by_id('email')
        password = self.driver.find_element_by_id('password')
        email.send_keys("")
        password.send_keys("Qwerty123!")

        self.driver.find_element_by_id('sign-in-button').click()
        text = self.driver.find_element_by_class_name('jss8')

        self.assertEqual(
            'Please make sure your inputs are not empty!', text.text)

    # (A3,B1) Nonregistered email
    # Ram Karri
    # Should display "You do not seem to have an account. Please register below!"
    def test_vunregistered(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id('email')
        password = self.driver.find_element_by_id('password')
        email.send_keys("ram.karri7@gmail.com")
        password.send_keys("Qwerty123!")

        self.driver.find_element_by_id('sign-in-button').click()
        text = self.driver.find_element_by_class_name('jss8')

        self.assertEqual(
            'You do not seem to have an account. Please register below!', text.text)
    # (A4,B1) Invalid email
    # Ram Karri
    # Should display "You do not seem to have an account. Please register below!"

    def test_winvalid_email(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id('email')
        password = self.driver.find_element_by_id('password')
        email.send_keys("ramkarri7")
        password.send_keys("Qwerty123!")

        self.driver.find_element_by_id('sign-in-button').click()
        text = self.driver.find_element_by_class_name('jss8')

        self.assertEqual(
            'You do not seem to have an account. Please register below!', text.text)

    # (A1,B2) Empty Password
    # Ram Karri
    # Should display "You do not seem to have an account. Please register below!"
    def test_xempty_password(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id('email')
        password = self.driver.find_element_by_id('password')
        email.send_keys("ramkarri7")
        password.send_keys("")

        self.driver.find_element_by_id('sign-in-button').click()
        text = self.driver.find_element_by_class_name('jss8')

        self.assertEqual(
            'Please make sure your inputs are not empty!', text.text)
    # (A1,B3) Wrong Password
    # Ram Karri
    # Should display "You do not seem to have an account. Please register below!"

    def test_ywrong_password(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id('email')
        password = self.driver.find_element_by_id('password')
        email.send_keys("Appolo@gmail.com")
        password.send_keys("Qwerty!")

        self.driver.find_element_by_id('sign-in-button').click()
        text = self.driver.find_element_by_class_name('jss8')

        self.assertEqual(
            'Incorrect password. Please try again or contact us!', text.text)

    # (A1,B1) Wrong Password
    # Ram Karri
    # Should result in None as that element will not be found as page will redirect"
    def test_zbase_case(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id('email')
        password = self.driver.find_element_by_id('password')
        email.send_keys("Appolo@gmail.com")
        password.send_keys("password")

        self.driver.find_element_by_id('sign-in-button').click()
        text = self.driver.find_element_by_class_name('jss8')

        self.assertIsNone(text)

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        return


if __name__ == '__main__':
    unittest.main()
