import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import data
from helpers import random_email
from locators import locators


class TestAnnouncement:

    def test_post_ad_unauthorized(self, driver, url):
        driver.find_element(*locators.Announcement.button_announcement).click()
        login_window_el = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Announcement.login_window))
        assert login_window_el.text == data.Registration.msg_autorization

    def test_post_an_ad_authorized(self, driver, url):
        # Регистрация нового пользователя
        driver.find_element(*locators.Registration.login_and_registration).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()

        # Заполняем форму регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))
        email = random_email()
        driver.find_element(*locators.Registration.email).send_keys(email)
        driver.find_element(*locators.Registration.password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.submit_password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.login_button).click()

        # Ждем успешной регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.user_name_elem))

        # Переход к созданию объявления
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.Announcement.button_announcement))
        driver.find_element(*locators.Announcement.button_announcement).click()

        # Заполняем объявление
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Announcement.name_announcement))
        time.sleep(3)
        driver.find_element(*locators.Announcement.name_announcement).send_keys(data.Announcement.name_announcement)
        driver.find_element(*locators.Announcement.description).send_keys(data.Announcement.description)
        driver.find_element(*locators.Announcement.price).send_keys(data.Announcement.price)

        # Выбираем радиокнопки и категории
        driver.find_element(*locators.Announcement.radiobutton).click()
        driver.find_element(*locators.Announcement.category).click()
        driver.find_element(*locators.Announcement.hobby).click()

        # Выбор города
        driver.find_element(*locators.Announcement.city).click()
        driver.find_element(*locators.Announcement.moscow).click()

        # Публикация
        driver.find_element(*locators.Announcement.publish).click()

        # Проверка, что мое объявление появилось
        my_ad = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(locators.Announcement.my_advertisements)
        )
        assert my_ad.is_displayed()

