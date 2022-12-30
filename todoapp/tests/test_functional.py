import unittest

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestUI(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self) -> None:
        self.driver.quit()

    def test_getindex(self):
        self.skipTest('Test get root is not implemented')
        self.driver.get('http://localhost:8000')
        self.assertTrue('To-do' in self.driver.page_source)

        self.fail('End of test!')


if __name__ == '__main__':
    unittest.main()
