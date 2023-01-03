import unittest
from time import sleep

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self) -> None:
        self.driver.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.driver.get('http://localhost:8000')
        todo_in_title = 'To-Do' in self.driver.title
        self.assertTrue(todo_in_title)
        header_text = self.driver.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.driver.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Купить мясо')
        inputbox.send_keys(Keys.ENTER)
        sleep(1)

        table = self.driver.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Купить мясо' for row in rows),
            f'Current is {table.text}'
        )

        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        sleep(10)

        table = self.driver.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '2: Сделать мушку из павлиньих перьев' for row in rows)
        )


if __name__ == '__main__':
    unittest.main()
