import unittest
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class tests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://cometshare.com/signup")
        self.driver.title


    # (A4,B2,C1,D1,E1,F1)
    # Anurag Vathalurin
    # Should display "Please enter a valid email."
    def test_a_invalid_email(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("asv9mn")
        name.send_keys("Taco Bell")
        address.send_keys("291 McCormick Rd")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Qwertyyy1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a valid email.', text.text)

        self.driver.refresh()

    # (A2,B2,C1,D1,E1,F1)
    # Anurag Vathalurin
    # Should display "One or more fields are missing!"
    def test_b_empty_email(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("")
        name.send_keys("Taco Bell")
        address.send_keys("291 McCormick Rd")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Qwertyyy1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('One or more fields are missing!', text.text)

        self.driver.refresh()

    # (A3,B2,C1,D1,E1,F1)
    # Ram Karri
    # Should display "Email is already registered."
    def test_c_taken_email(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("ramkarri7@gmail.com")
        name.send_keys("Taco Bell")
        address.send_keys("291 McCormick Rd")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Qwertyyy1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Email is already registered.', text.text)

        self.driver.refresh()

 # (A1,B2,C3,D1,E1,F1)
    # Ram Karri
    # Should display "One or more fields are missing!"
    def test_f_empty_address(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("asv9mn@virginia.edu")
        name.send_keys("Taco Bell")
        address.send_keys("")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Qwertyyy1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('One or more fields are missing!', text.text)

        self.driver.refresh()

    # (A1,B2,C2,D1,E1,F1)
    # Ram Karri
    # (FAILS) Should display "Address is invalid."; however, application doesn't test to see if address is valid, thus creating an account
    #A different email is used to here to show that a new account would be created for each individual user since our base case (which is run before this test) uses the original email to successfully create a new account
    def test_z_invalid_address(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("9beeka.beeka.75l@bb7665.com")
        name.send_keys("Taco Bell")
        address.send_keys("123456789")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Qwertyyy1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Address is invalid', text.text)

        self.driver.refresh()

    # (A1,B2,C4,D1,E1,F1)
    # Ram Karri
    # Should display "This store seems to already exist."
    # A new email is used to prevent the "Taken Email" error from showing up again: this will specifically show the "Taken Address" error
    def test_y_taken_address(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("emehd_itov@civoo.com")
        name.send_keys("Taco Bell")
        address.send_keys("8608 Aldeburgh dr")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Qwertyyy1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('This store seems to already exist.', text.text)

        self.driver.refresh()

    # (A1,B2,C1,D3,E1,F1)
    # Ram Karri
    # Should display "One or more fields are missing!"
    def test_g_empty_zipcode(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("asv9mn@virginia.edu")
        name.send_keys("Taco Bell")
        address.send_keys("291 McCormick Rd")
        zipcode.send_keys("")
        city.send_keys("Charlottesville")
        password.send_keys("Qwertyyy1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('One or more fields are missing!', text.text)

        self.driver.refresh()

    # (A1,B2,C1,D2,E1,F1)
    # Ram Karri
    # Should display "Please enter a valid zip code!"
    def test_h_invalid_zipcode(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("asv9mn@virginia.edu")
        name.send_keys("Taco Bell")
        address.send_keys("291 McCormick Rd")
        zipcode.send_keys("12345678910111213141516")
        city.send_keys("Charlottesville")
        password.send_keys("Qwertyyy1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a valid zip code!', text.text)

        self.driver.refresh()

    # (A1,B2,C1,D1,E3,F1)
    # Ram Karri
    # (FAILS) Should display "Please enter a valid email."; however, the application doesn't test to see if the inputted city exists/is valid thus creating the account
    #A different email and address are used here to show that a new account would be created for each individual user since our base case (which is run before this test) uses the original email and address to successfully create a new account
    def test_x_invalid_city(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("hhicham.blend1q@caeboyleg.ga")
        name.send_keys("Taco Bell")
        address.send_keys("450 Whitehead Rd")
        zipcode.send_keys("22903")
        city.send_keys("Ch4r1otte5vi11e")
        password.send_keys("Qwertyyy1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a valid city!', text.text)

        self.driver.refresh()

    # (A1,B2,C1,D1,E2,F1)
    # Ram Karri
    # Should display "One or more fields are missing!"
    def test_i_empty_city(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("asv9mn@virginia.edu")
        name.send_keys("Taco Bell")
        address.send_keys("291 McCormick Rd")
        zipcode.send_keys("22903")
        city.send_keys("")
        password.send_keys("Qwertyyy1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('One or more fields are missing!', text.text)

        self.driver.refresh()

    # (A1,B2,C1,D1,E1,F3)
    # Ram Karri
    # Should display "Please enter a stronger password."
    def test_j_password_less_than_8(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("asv9mn@virginia.edu")
        name.send_keys("Taco Bell")
        address.send_keys("291 McCormick Rd")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Qwty1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a stronger password.', text.text)

        self.driver.refresh()

    # (A1,B2,C1,D1,E1,F6)
    # Ram Karri
    # Should display "Please enter a stronger password."
    def test_k_password_no_uppercase_letter(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("asv9mn@virginia.edu")
        name.send_keys("Taco Bell")
        address.send_keys("291 McCormick Rd")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("qwertyyy1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a stronger password.', text.text)

        self.driver.refresh()

    # (A1,B2,C1,D1,E1,F5)
    # Ram Karri
    # Should display "Please enter a stronger password."
    def test_l_password_no_number(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("asv9mn@virginia.edu")
        name.send_keys("Taco Bell")
        address.send_keys("291 McCormick Rd")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Qwertyyy?")
        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a stronger password.', text.text)

        self.driver.refresh()

    # (A1,B2,C1,D1,E1,F4)
    # Ram Karri
    # Should display "Please enter a stronger password."
    def test_m_password_no_special_char(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("asv9mn@virginia.edu")
        name.send_keys("Taco Bell")
        address.send_keys("291 McCormick Rd")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Qwertyyy1")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a stronger password.', text.text)

        self.driver.refresh()

    # (A1,B2,C1,D1,E1,F2)
    # Ram Karri
    # Should display "One or more fields are missing!"
    def test_n_empty_password(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("asv9mn@virginia.edu")
        name.send_keys("Taco Bell")
        address.send_keys("291 McCormick Rd")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('One or more fields are missing!', text.text)

        self.driver.refresh()

    # (A1,B2,C1,D1,E1,F1)
    # Ram Karri
    # Should display "You have successfully registered! An email has been sent to you to activate your account."
    def test_o_base_case2(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("asv9mn@virginia.edu")
        name.send_keys("Taco Bell")
        address.send_keys("291 McCormick Rd")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Qwertyyy1?")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('You have successfully registered! An email has been sent to you to activate your account.', text.text)

        self.driver.refresh()
if __name__ == '__main__':
    unittest.main()