from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import data
from helpers import random_email
from locators import locators


class TestRegistration:
    TIMEOUT_SHORT = 3
    TIMEOUT_LONG = 5

    def open_registration_form(self, driver):
        driver.find_element(*locators.Registration.login_and_registration).click()
        WebDriverWait(driver, self.TIMEOUT_SHORT).until(EC.visibility_of_element_located(locators.Registration.button_no_acc))
        driver.find_element(*locators.Registration.button_no_acc).click()

    def fill_registration_form(self, driver, email, password):
        WebDriverWait(driver, self.TIMEOUT_SHORT).until(EC.visibility_of_element_located(locators.Registration.email))
        driver.find_element(*locators.Registration.email).send_keys(email)
        driver.find_element(*locators.Registration.password).send_keys(password)
        driver.find_element(*locators.Registration.submit_password).send_keys(password)
        driver.find_element(*locators.Registration.login_button).click()

    def logout(self, driver):
        WebDriverWait(driver, self.TIMEOUT_SHORT).until(EC.visibility_of_element_located(locators.Registration.logout))
        driver.find_element(*locators.Registration.logout).click()

    def login_as_registered_user(self, driver, email, password):
        self.open_registration_form(driver)
        self.fill_registration_form(driver, email, password)
        WebDriverWait(driver, self.TIMEOUT_LONG).until(EC.visibility_of_element_located(locators.Registration.user_name_elem))
        user_name_elem = driver.find_element(*locators.Registration.user_name_elem)
        user_name = user_name_elem.text
        user_avatar = driver.find_element(*locators.Registration.user_avatar)
        return user_name, user_avatar

    def test_registration(self, driver, url):
        self.open_registration_form(driver)
        email = random_email()
        self.fill_registration_form(driver, email, data.Registration.password)

        # Проверка успешной регистрации
        WebDriverWait(driver, self.TIMEOUT_LONG).until(EC.visibility_of_element_located(locators.Registration.user_name_elem))
        user_name, user_avatar = self.login_and_get_user_info(driver)

        assert user_name == data.Registration.user_name
        assert user_avatar.is_displayed()

    def test_registration_no_mask(self, driver, url):
        self.open_registration_form(driver)
        WebDriverWait(driver, self.TIMEOUT_SHORT).until(EC.visibility_of_element_located(locators.Registration.email))
        driver.find_element(*locators.Registration.email).send_keys(data.Registration.uncorrect_email)
        driver.find_element(*locators.Registration.password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.submit_password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.login_button).click()

        WebDriverWait(driver, self.TIMEOUT_SHORT).until(EC.visibility_of_element_located(locators.Registration.error_login))
        error_text = driver.find_element(*locators.Registration.error_login).text

        email_error_class = driver.find_element(*locators.Registration.error).get_attribute('class')

        assert error_text == data.Registration.error
        assert email_error_class == data.Registration.error_class, "Поля не подсвечены красным"

    def test_registration_exists(self, driver, url):
        email = random_email()
        self.open_registration_form(driver)
        self.fill_registration_form(driver, email, data.Registration.password)

        # Ждём и выходим из профиля
        WebDriverWait(driver, self.TIMEOUT_SHORT).until(EC.visibility_of_element_located(locators.Registration.logout))
        self.logout(driver)

        # Повторная регистрация с тем же email
        self.open_registration_form(driver)
        self.fill_registration_form(driver, email, data.Registration.password)

        # Проверка ошибки
        WebDriverWait(driver, self.TIMEOUT_SHORT).until(EC.visibility_of_element_located(locators.Registration.error_login))
        error_text = driver.find_element(*locators.Registration.error_login).text

        email_error_class = driver.find_element(*locators.Registration.error).get_attribute('class')

        assert error_text == data.Registration.error
        assert email_error_class == data.Registration.error_class

    def test_login_exists(self, driver, url):
        email = random_email()
        # Регистрация нового пользователя
        self.open_registration_form(driver)
        self.fill_registration_form(driver, email, data.Registration.password)

        # Вход под этим пользователем
        WebDriverWait(driver, self.TIMEOUT_SHORT).until(EC.visibility_of_element_located(locators.Registration.logout))
        self.logout(driver)

        # Войти еще раз
        self.open_registration_form(driver)
        WebDriverWait(driver, self.TIMEOUT_SHORT).until(EC.visibility_of_element_located(locators.Registration.email))
        driver.find_element(*locators.Registration.email).send_keys(email)
        driver.find_element(*locators.Registration.password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.login).click()

        # Проверка успешного входа
        WebDriverWait(driver, self.TIMEOUT_LONG).until(EC.visibility_of_element_located(locators.Registration.user_name_elem))
        user_name, user_avatar = self.login_and_get_user_info(driver)

        assert user_name == data.Registration.user_name
        assert user_avatar.is_displayed()

    def test_logout_exists(self, driver, url):
        # Аналогично другим тестам, можно через `login_as_registered_user`
        email = random_email()
        self.open_registration_form(driver)
        self.fill_registration_form(driver, email, data.Registration.password)

        # Войти и выйти
        WebDriverWait(driver, self.TIMEOUT_SHORT).until(EC.visibility_of_element_located(locators.Registration.logout))
        self.logout(driver)

        # Послать повторный логин и убеждаться, что элементы скрыты/не отображаются
        WebDriverWait(driver, self.TIMEOUT_SHORT).until(EC.visibility_of_element_located(locators.Registration.email))
        driver.find_element(*locators.Registration.email).send_keys(email)
        driver.find_element(*locators.Registration.password).send_keys(data.Registration.password)
        driver.find_element(*locators.Registration.login).click()

        user_name_elem = WebDriverWait(driver, self.TIMEOUT_LONG).until(EC.visibility_of_element_located(locators.Registration.user_name_elem))
        user_name = user_name_elem.text
        user_avatar = driver.find_element(*locators.Registration.user_avatar)

        # Проверки: что пользователь не авторизован (элементы скрыты/отсутствуют)
        assert not user_name_elem.is_displayed()
        assert not user_avatar.is_displayed()
        assert driver.find_element(*locators.Registration.login_and_registration).is_displayed()

    def login_and_get_user_info(self, driver):
        """Вспомогательный метод для получения имени и аватара пользователя после авторизации."""
        user_name_elem = WebDriverWait(driver, self.TIMEOUT_LONG).until(EC.visibility_of_element_located(locators.Registration.user_name_elem))
        user_name = user_name_elem.text
        user_avatar = driver.find_element(*locators.Registration.user_avatar)
        return user_name, user_avatar
