import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Inicializa o driver do Selenium
        self.driver.get('http://127.0.0.1:8000/')  # Abre a página de login

    def tearDown(self):
        self.driver.quit()  # Encerra o driver do Selenium

    def test_screen(self):
        for section in range(1, 13):
            # Clica em um dos vinhos
            self.driver.find_element(By.CLASS_NAME, f'style{section}').click()
            sleep(0.1)
            # clica no nav
            self.driver.find_element(By.XPATH, '//*[@id="header"]/div/nav/ul/li/a').click()
            sleep(0.1)
            # Retorna para a página inicial
            self.driver.find_element(By.XPATH, '//*[@id="menu"]/div/ul/li[1]/a').click()
            sleep(0.1)


if __name__ == 'main':
    unittest.main()
