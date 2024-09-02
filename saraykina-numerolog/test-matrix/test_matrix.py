import time

from allure import id, step, epic, feature, manual, description, title, suite, dynamic, label, story
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pages import icon_vk,icon_tel,icon_inst


@mark.web
@epic('Таро-нумерология')
@feature('Главная страница')
class TestMatrix:
    @mark.web
    @story('Иконка VK')
    @title('Переход по иконке VK')
    @description('Проверить возможность перехода по иконке VK')
    @label('priority', 'низкий')
    def test_matrix_step_in_vk(self):
        options = Options()
        with step('Перейти на страницу'):
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
            driver.get('https://www.saraykina-numerolog.ru/index.html')
        with step('Проверить переход на страницу Vk через иконку VK'):
            with step('Нажать на иконку "VK" и перейти на страницу VK'):
                click = driver.find_element(By.CLASS_NAME, 'socials')
                click.click()
            with step('Проверить отображение страницы Vk'):
                time.sleep(5)
       







