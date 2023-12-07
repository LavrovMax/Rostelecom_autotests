import pytest
from pages.auth_page import AuthPage
from selenium.webdriver.common.by import By


def test_authorisation_for_email(web_browser):

    """тест проверяющий авторизацию зарегестрированного пользователя с помощью почты"""

    page = AuthPage(web_browser)

    page.email.send_keys('your_email')

    page.password.send_keys("your_password")

    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=ed882c5d-d92b-42ce-9c1e-904c0d5de3f9&client_id=account_b2c&theme=light#/'


def test_authorisation_for_number_phone(web_browser):

    """тест проверяющий авторизацию зарегестрированного пользователя через номер телефона"""

    page = AuthPage(web_browser)

    page.number.send_keys('+7**********')

    page.password.send_keys('Your_password')

    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=ed882c5d-d92b-42ce-9c1e-904c0d5de3f9&client_id=account_b2c&theme=light#/'


def test_registration_form(web_browser):

    """тест проверяющий регистрацию нового пользователя"""

    page = AuthPage(web_browser)

    button_registation = web_browser.find_element(By.XPATH,'//*[@id="kc-register"]')

    first_name = web_browser.find_element(By.XPATH,'//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')

    last_name = web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    email = web_browser.find_element(By.ID, 'address')

    password = web_browser.find_element(By.ID, 'password')

    confirmation_pass = web_browser.find_element(By.ID, 'password-confirm')

    button_register = web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button')

    button_registation.click()

    first_name.send_keys()

    last_name.send_keys()

    email.send_keys()

    password.send_keys()

    confirmation_pass.send_keys()

    button_register.click()

def test_add_number_phone(web_browser):

    """тест проверяющий возможность добавления номера телефона в ЛК"""

    page = AuthPage(web_browser)

    page.email.send_keys("your_email")

    page.password.send_keys("your_password")

    page.btn.click()

    button_number_add = web_browser.find_element(By.ID, "phone_action")

    button_number_code = web_browser.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[5]/div/div/div/div/div/div/div/div[1]/div')

    button_number_add.click()

    button_number_code.send_keys("******")

    messenge = web_browser.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[5]/div/div/div/div/p[1]').text

    assert messenge == 'Номер телефона изменён'

def test_authorisation_for_temporary_code(web_browser):

    """тест проверяющию авторизацию по временному коду"""

    page = AuthPage(web_browser)

    button_code = web_browser.find_element(By.XPATH, '//*[@id="back_to_otp_btn"]')

    input_number = web_browser.find_element(By.XPATH, '//*[@id="address"]')

    button_get_code = web_browser.find_element(By.XPATH, '//*[@id="otp_get_code"]')

    button_code.click()

    input_number.send_keys('+7**********')

    button_get_code.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=053cd459-327d-4b82-93a1-9465b55fccc5&client_id=lk_onlime&tab_id=IPyVtYSxPvI'

def test_exit_the_authorisation(web_browser):

    """тест проверяющий возможность выйти из ЛК"""

    page = AuthPage(web_browser)

    page.email.send_keys('your_email')

    page.password.send_keys("Your_password")

    page.btn.click()

    button_exit = web_browser.find_element(By.XPATH, '//*[@id="logout-btn"]')

    button_exit.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=a64f093c-3485-4577-8256-7df48e082db2&theme=light&auth_type'








