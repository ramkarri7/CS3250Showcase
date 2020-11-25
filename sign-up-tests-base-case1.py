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

    # (A4,B1,C1,D1,E1,F1)
    # Anurag Vathalurin
    # Should display "Please enter a valid email."
    def test_a_invalid_email(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("avathalurin")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a valid email.', text.text)

        self.driver.refresh()

    # (A2,B1,C1,D1,E1,F1)
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
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('One or more fields are missing!', text.text)

        self.driver.refresh()

    # (A3,B1,C1,D1,E1,F1)
    # Anurag Vathalurin
    # Should display "Email is already registered."
    def test_c_taken_email(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("ramkarri7@gmail.com")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Email is already registered.', text.text)

        self.driver.refresh()

    # (A1,B3,C1,D1,E1,F1)
    # Anurag Vathalurin
    # Should display "One or more fields are missing"
    def test_d_empty_eatery_name(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("avathalurin@gmail.com")
        name.send_keys("")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('One or more fields are missing!', text.text)

        self.driver.refresh()

    # (A1,B2,C1,D1,E1,F1)
    # Anurag Vathalurin
    # Should display "This store seems to already exist."
    def test_p_taken_eatery_name(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("zislam.kh.9674h@chanmelon.com")
        name.send_keys("Quick Pizza")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('This store seems to already exist.', text.text)

        self.driver.refresh()

    # (A1,B1,C3,D1,E1,F1)
    # Anurag Vathalurin
    # Should display "One or more fields are missing!"
    def test_f_empty_address(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("avathalurin@gmail.com")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('One or more fields are missing!', text.text)

        self.driver.refresh()

    # (A1,B1,C2,D1,E1,F1)
    # Anurag Vathalurin
    # (FAILS) Should display "Address is invalid."; however, application doesn't test to see if address is valid, thus creating an account
    def test_z_invalid_address(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("3el-mohadi-r@usabrains.us")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("123456789")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Address is invalid', text.text)

        self.driver.refresh()

    # (A1,B1,C4,D1,E1,F1)
    # Anurag Vathalurin
    # (FAILS) Should display "Your address is taken"; however, the application doesn't test to see if the address is taken by another account, thus creating this account
    def test_y_taken_address(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("ssoufiane.amoori@cheapnitros.com")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("9410 W Broad St")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Your address is taken.', text.text)

        self.driver.refresh()

    # (A1,B1,C1,D3,E1,F1)
    # Anurag Vathalurin
    # Should display "One or more fields are missing!"
    def test_g_empty_zipcode(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("avathalurin@gmail.com")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('One or more fields are missing!', text.text)

        self.driver.refresh()

    # (A1,B1,C1,D2,E1,F1)
    # Anurag Vathalurin
    # Should display "Please enter a valid zip code!"
    def test_h_invalid_zipcode(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("avathalurin@gmail.com")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("12345678910111213141516")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a valid zip code!', text.text)

        self.driver.refresh()

    # (A1,B1,C1,D1,E3,F1)
    # Anurag Vathalurin
    # (FAILS) Should display "Please enter a valid email."; however, the application doesn't test to see if the inputted city exists/is valid thus creating the account
    def test_x_invalid_city(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("mabdo@rochmeve.ml")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("Ch4r1otte5vi11e")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a valid city!', text.text)

        self.driver.refresh()

    # (A1,B1,C1,D1,E2,F1)
    # Anurag Vathalurin
    # Should display "One or more fields are missing!"
    def test_i_empty_city(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("avathalurin@gmail.com")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('One or more fields are missing!', text.text)

        self.driver.refresh()

    # (A1,B1,C1,D1,E1,F3)
    # Anurag Vathalurin
    # Should display "Please enter a stronger password."
    def test_j_password_less_than_8(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("avathalurin@gmail.com")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Thrs6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a stronger password.', text.text)

        self.driver.refresh()

    # (A1,B1,C1,D1,E1,F6)
    # Anurag Vathalurin
    # Should display "Please enter a stronger password."
    def test_k_password_no_uppercase_letter(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("avathalurin@gmail.com")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a stronger password.', text.text)

        self.driver.refresh()

    # (A1,B1,C1,D1,E1,F5)
    # Anurag Vathalurin
    # Should display "Please enter a stronger password."
    def test_l_password_no_number(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("avathalurin@gmail.com")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a stronger password.', text.text)

        self.driver.refresh()

    # (A1,B1,C1,D1,E1,F4)
    # Anurag Vathalurin
    # Should display "Please enter a stronger password."
    def test_m_password_no_special_char(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("avathalurin@gmail.com")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars6")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('Please enter a stronger password.', text.text)

        self.driver.refresh()

    # (A1,B1,C1,D1,E1,F2)
    # Anurag Vathalurin
    # Should display "One or more fields are missing!"
    def test_n_empty_password(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("avathalurin@gmail.com")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('One or more fields are missing!', text.text)

        self.driver.refresh()

    # (A1,B1,C1,D1,E1,F1)
    # Anurag Vathalurin
    # Should display "You have successfully registered! An email has been sent to you to activate your account."
    def test_o_base_case1(self):
        email = self.driver.find_element_by_id('email')
        name = self.driver.find_element_by_id('storeName')
        address = self.driver.find_element_by_id('location')
        zipcode = self.driver.find_element_by_id('zipCode')
        city = self.driver.find_element_by_id('city')
        password = self.driver.find_element_by_id('password')

        email.send_keys("avathalurin@gmail.com")
        name.send_keys("Anurag's Biriyani Palace")
        address.send_keys("85 Engineer's Way")
        zipcode.send_keys("22903")
        city.send_keys("Charlottesville")
        password.send_keys("Thenewcars6!")

        self.driver.find_element_by_id('sign-up-button').click()
        text = self.driver.find_element_by_class_name('jss3')

        self.assertEqual('You have successfully registered! An email has been sent to you to activate your account.', text.text)

        self.driver.refresh()
if __name__ == '__main__':
    unittest.main()