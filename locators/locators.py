from selenium.webdriver.common.by import By

class Registration:
    login_and_registration = (By.CLASS_NAME, "header_flexRow__Xdqv1")
    button_no_acc = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[3]/button[2]")
    email = (By.NAME, "email")
    password = (By.NAME, "password")
    submit_password = (By.NAME, "submitPassword")
    login_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[3]/button[1]")
    user_avatar = (By.XPATH, "//button[@class='circleSmall']")
    user_name_elem = (By.XPATH, "//h3[@class='profileText name']")
    error_login = (By.CLASS_NAME, 'input_span__yWPqB')
    field_mail = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/div/div')
    field_pass = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[2]/div/div')
    field_sec_pass = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[3]/div/div')
    logout = (By.CLASS_NAME, 'spanGlobal btnSmall')
    login = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div/button')

class Announcement:
    button_announcement = (By.XPATH, '//*[@id="root"]/div/div[1]/button')
    login_window = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[1]/h1')
