import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



class PythonOrgSearch(unittest.TestCase):

    """
    Search Engine
    """
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000/")
        self.assertIn("Home", driver.title)
        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
