from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import data
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
        driver.find_element(*locators.Registration.password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.submit_password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.login_button).click()

        # Проверяем переход на страницу профиля
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.Registration.user_name_elem))
        user_name_elem = driver.find_element(*locators.Registration.user_name_elem)
        user_name = user_name_elem.text

        user_avatar = driver.find_element(*locators.Registration.user_avatar)

        # Проверки
        assert user_name == data.Registration.user_name
        assert user_avatar.is_displayed()

    def test_registration_no_mask(self, driver, url):
        # Нажимаем "Вход и регистрация"
        driver.find_element(*locators.Registration.login_and_registration).click()

        # Ждём и кликаем "Нет аккаунта"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()

        # Заполняем форму регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))
        driver.find_element(*locators.Registration.email).send_keys(data.Registration.uncorrect_email)
        driver.find_element(*locators.Registration.password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.submit_password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.login_button).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.error_login))
        login = driver.find_element(*locators.Registration.error_login).text
        email_field = driver.find_element(*locators.Registration.error)
        password_field = driver.find_element(*locators.Registration.error)
        repeat_password_field = driver.find_element(*locators.Registration.error)

        assert login == data.Registration.error
        assert email_field.get_attribute('class') == data.Registration.error_class, "Email поле не подсвечено красным"
        assert password_field.get_attribute('class') == data.Registration.error_class, "Пароль поле не подсвечено красным"
        assert repeat_password_field.get_attribute('class') == data.Registration.error_class, "Повторный пароль не подсвечен красным"

    def test_registration_exists(self, driver, url):
        # Нажимаем "Вход и регистрация"
        driver.find_element(*locators.Registration.login_and_registration).click()

        # Ждём и кликаем "Нет аккаунта"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()

        # Заполняем форму регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))
        email = random_email()
        driver.find_element(*locators.Registration.email).send_keys(email)
        driver.find_element(*locators.Registration.password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.submit_password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.login_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.logout))
        driver.find_element(*locators.Registration.logout).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.Registration.login_and_registration))
        driver.find_element(*locators.Registration.login_and_registration).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))

        driver.find_element(*locators.Registration.email).send_keys(email)
        driver.find_element(*locators.Registration.password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.submit_password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.login_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.error_login))

        login = driver.find_element(*locators.Registration.error_login).text
        email_field = driver.find_element(*locators.Registration.error)
        password_field = driver.find_element(*locators.Registration.error)
        repeat_password_field = driver.find_element(*locators.Registration.error)

        assert login == data.Registration.error
        assert email_field.get_attribute('class') == data.Registration.error_class, "Email поле не подсвечено красным"
        assert password_field.get_attribute('class') == data.Registration.error_class, "Пароль поле не подсвечено красным"
        assert repeat_password_field.get_attribute('class') == data.Registration.error_class, "Повторный пароль не подсвечен красным"

    def test_login_exists(self, driver, url):
        driver.find_element(*locators.Registration.login_and_registration).click()

        # Ждём и кликаем "Нет аккаунта"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()

        # Заполняем форму регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))
        email = random_email()

        driver.find_element(*locators.Registration.email).send_keys(email)
        driver.find_element(*locators.Registration.password).send_keys(data.Registration.password)

        driver.find_element(*locators.Registration.submit_password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.login_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.logout))
        driver.find_element(*locators.Registration.logout).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.Registration.login_and_registration))
        driver.find_element(*locators.Registration.login_and_registration).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))
        driver.find_element(*locators.Registration.email).send_keys(email)
        driver.find_element(*locators.Registration.password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.login).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.Registration.user_name_elem))
        user_name_elem = driver.find_element(*locators.Registration.user_name_elem)
        user_name = user_name_elem.text
        user_avatar = driver.find_element(*locators.Registration.user_avatar)

        assert user_name == data.Registration.user_name
        assert user_avatar.is_displayed()

    def test_logout_exists(self, driver, url):
        # Нажимаем "Вход и регистрация"
        driver.find_element(*locators.Registration.login_and_registration).click()

        # Ждём и кликаем "Нет аккаунта"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()

        # Заполняем форму регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.email))
        email = random_email()
        driver.find_element(*locators.Registration.email).send_keys(email)
        driver.find_element(*locators.Registration.password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.submit_password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.login_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.Registration.logout))
        driver.find_element(*locators.Registration.logout).click()

        user_name_elem = driver.find_element(*locators.Registration.user_name_elem)
        user_name = user_name_elem.text
        user_avatar = driver.find_element(*locators.Registration.user_avatar)

        assert not user_name_elem.is_displayed()
        assert not user_avatar.is_displayed()
        assert locators.Registration.login_and_registration.is_displayed()
