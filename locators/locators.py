from selenium.webdriver.common.by import By

class Registration:
    login_and_registration = (By.XPATH, ".//button[text()='Вход и регистрация']")
    button_no_acc = (By.XPATH, ".//button[text()='Нет аккаунта']")
    email = (By.NAME, "email")
    password = (By.NAME, "password")
    submit_password = (By.NAME, "submitPassword")
    login_button = (By.XPATH, ".//button[text()='Создать аккаунт']")
    user_avatar = (By.XPATH, "//button[@class='circleSmall']")
    user_name_elem = (By.XPATH, "//h3[@class='profileText name']")
    error_login = (By.XPATH, ".//span[text()='Ошибка']")
    error = (By.CLASS_NAME, 'input_inputError__fLUP9')
    logout = (By.XPATH, ".//button[text()='Выйти']")
    login = (By.XPATH, ".//button[text()='Войти']")


class Announcement:
    button_announcement = (By.XPATH, ".//button[text()='Разместить объявление']")
    login_window = (By.CLASS_NAME, 'popUp_titleRow__M7tGg')
    name_announcement = (By.CLASS_NAME, 'input_inputDefault__UmPK0')
    description = (By.CLASS_NAME, 'textarea_inputDefault__KvlMg')
    price = (By.CLASS_NAME, 'input_inputStandart__JweLZ')
    radiobutton = (By.CLASS_NAME, 'radioUnput_inputActive__eC-HY')
    category = (By.NAME, "category")
    hobby = (By.XPATH, ".//span[text()='Хобби']")
    city = (By.NAME, "city")
    moscow = (By.XPATH, ".// span[text() = 'Москва']")
    publish = (By.XPATH, ".//button[text()='Опубликовать']")
    my_advertisements = (By.CLASS_NAME, 'card')
