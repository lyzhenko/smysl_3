from django.test import TestCase
from selenium import webdriver


class BasicInstallTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_install(self):
        self.browser.get('http://localhost:8000')
        self.assertTrue('Установка прошла успешно! Поздравляем!' in self.browser.title, 'Тест пройден успешно!')
        self.fail('Not implemented')


class MainTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_create_url(self):
        self.browser.get('http://localhost:8000/main')
        self.assertTrue('http://localhost:8000/main' in self.browser.current_url, 'Тест пройден успешно!')
