from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers import random_email
from locators import locators


class TestRegistration:
    def test_registration(self, driver, url):
        # Нажимаем "Вход и регистрация"
        driver.find_element(*locators.Registration.login_and_registration).click()

        # Ждём и кликаем "Нет аккаунта"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()

        # Заполняем форму регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))
        driver.find_element(*locators.Registration.email).send_keys(random_email())
        driver.find_element(*locators.Registration.password).send_keys("1234")
        driver.find_element(*locators.Registration.submit_password).send_keys("1234")
        driver.find_element(*locators.Registration.login_button).click()

        # Проверяем переход на страницу профиля
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.Registration.user_name_elem))
        user_name_elem = driver.find_element(*locators.Registration.user_name_elem)
        user_name = user_name_elem.text

        user_avatar = driver.find_element(*locators.Registration.user_avatar)

        # Проверки
        assert user_name == 'User.'
        assert user_avatar.is_displayed()


    def test_registration_no_mask(self, driver, url):
        # Нажимаем "Вход и регистрация"
        driver.find_element(*locators.Registration.login_and_registration).click()

        # Ждём и кликаем "Нет аккаунта"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()

        # Заполняем форму регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))
        driver.find_element(*locators.Registration.email).send_keys('asd')
        driver.find_element(*locators.Registration.password).send_keys("1234")
        driver.find_element(*locators.Registration.submit_password).send_keys("1234")
        driver.find_element(*locators.Registration.login_button).click()

        login = driver.find_element(*locators.Registration.error_login).get_attribute('text')
        field_mail = driver.find_element(*locators.Registration.field_mail)
        field_pass = driver.find_element(*locators.Registration.field_pass)
        field_sec_pass = driver.find_element(*locators.Registration.field_sec_pass)

        assert login == "Ошибка"
        assert field_mail.border in ['rgb(255, 0, 0)', 'rgba(255, 0, 0, 1)']
        assert field_pass.border in ['rgb(255, 0, 0)', 'rgba(255, 0, 0, 1)']
        assert field_sec_pass.border in ['rgb(255, 0, 0)', 'rgba(255, 0, 0, 1)']


    def test_registration_exists(self, driver, url):
        # Нажимаем "Вход и регистрация"
        driver.find_element(*locators.Registration.login_and_registration).click()

        # Ждём и кликаем "Нет аккаунта"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()

        # Заполняем форму регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))
        email = driver.find_element(*locators.Registration.email).send_keys(random_email())
        driver.find_element(*locators.Registration.password).send_keys("1234")
        driver.find_element(*locators.Registration.submit_password).send_keys("1234")
        driver.find_element(*locators.Registration.logout).click()
        driver.find_element(*locators.Registration.login_and_registration).click()


        login = driver.find_element(*locators.Registration.error_login).get_attribute('text')
        field_mail = driver.find_element(*locators.Registration.field_mail)
        field_pass = driver.find_element(*locators.Registration.field_pass)
        field_sec_pass = driver.find_element(*locators.Registration.field_sec_pass)

        assert login == "Ошибка"
        assert field_mail.border in ['rgb(255, 0, 0)', 'rgba(255, 0, 0, 1)']
        assert field_pass.border in ['rgb(255, 0, 0)', 'rgba(255, 0, 0, 1)']
        assert field_sec_pass.border in ['rgb(255, 0, 0)', 'rgba(255, 0, 0, 1)']

    def test_login_exists(self, driver, url):
        # Нажимаем "Вход и регистрация"
        driver.find_element(*locators.Registration.login_and_registration).click()

        # Ждём и кликаем "Нет аккаунта"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()

        # Заполняем форму регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))
        email = driver.find_element(*locators.Registration.email).send_keys(random_email())
        driver.find_element(*locators.Registration.password).send_keys("1234")
        driver.find_element(*locators.Registration.submit_password).send_keys("1234")
        driver.find_element(*locators.Registration.logout).click()
        driver.find_element(*locators.Registration.login_and_registration).click()


        login = driver.find_element(*locators.Registration.error_login).get_attribute('text')
        field_mail = driver.find_element(*locators.Registration.field_mail)
        field_pass = driver.find_element(*locators.Registration.field_pass)
        field_sec_pass = driver.find_element(*locators.Registration.field_sec_pass)

        assert login == "Ошибка"
        assert field_mail.border in ['rgb(255, 0, 0)', 'rgba(255, 0, 0, 1)']
        assert field_pass.border in ['rgb(255, 0, 0)', 'rgba(255, 0, 0, 1)']
        assert field_sec_pass.border in ['rgb(255, 0, 0)', 'rgba(255, 0, 0, 1)']

    def test_logout_exists(self, driver, url):
        # Нажимаем "Вход и регистрация"
        driver.find_element(*locators.Registration.login_and_registration).click()

        # Ждём и кликаем "Нет аккаунта"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()

        # Заполняем форму регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))
        email = driver.find_element(*locators.Registration.email).send_keys(random_email())
        driver.find_element(*locators.Registration.password).send_keys("1234")
        driver.find_element(*locators.Registration.submit_password).send_keys("1234")
        driver.find_element(*locators.Registration.logout).click()
        driver.find_element(*locators.Registration.login_and_registration).click()


        login = driver.find_element(*locators.Registration.error_login).get_attribute('text')
        field_mail = driver.find_element(*locators.Registration.field_mail)
        field_pass = driver.find_element(*locators.Registration.field_pass)
        field_sec_pass = driver.find_element(*locators.Registration.field_sec_pass)