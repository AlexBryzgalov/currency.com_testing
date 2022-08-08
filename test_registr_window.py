from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_registration_window(self):
        link = "https://currency.com/en"
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.get(link)
        sign_up_button = browser.find_element(By.XPATH, '(//a[@class="singInBtn js_signup "])[1]')
        sign_up_button.click()
        continue_button = browser.find_element(By.XPATH, '(//button[@type="submit"])[4]')
        continue_button_text = continue_button.text


        self.assertEqual(continue_button_text.lower(), 'continue', "Should be a string 'continue'")

        
if __name__ == "__main__":
    unittest.main()

