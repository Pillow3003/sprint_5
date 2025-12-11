from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers import random_email
from locators import locators


class TestAnnouncement:
    def test_post_an_ad_unauthorized(self, driver, url):
        driver.find_element(*locators.Announcement.button_announcement).click()
        login_window_el = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Announcement.login_window))

        assert login_window_el.text == 'Чтобы разместить объявление, авторизуйтесь'

    def test_post_an_ad_authorized(self, driver, url):
        # Нажимаем "Вход и регистрация"
        driver.find_element(*locators.Registration.login_and_registration).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()

        # Заполняем форму регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))
        email = driver.find_element(*locators.Registration.email).send_keys(random_email())
        driver.find_element(*locators.Registration.password).send_keys("1234")
        driver.find_element(*locators.Registration.submit_password).send_keys("1234")
        driver.find_element(*locators.Registration.logout).click()
        driver.find_element(*locators.Registration.login).click()
        driver.find_element(*locators.Registration.login).send_keys(email)
        driver.find_element(*locators.Registration.password).send_keys("1234")
        login_window_el = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Announcement.login_window))



