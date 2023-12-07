import pytest
from pages.auth_page import AuthPage
from selenium.webdriver.common.by import By

def test_auth_invalid_data_for_email(web_browser):

    """тест проверяющий невозможность авторизироваться с неправильным емейлом"""

    page = AuthPage(web_browser)

    page.email.send_keys('invalid_email')

    page.password.send_keys("your_password")

    page.btn.click()

    assert page.get_current_url() != 'https://b2c.passport.rt.ru/account_b2c/page?state=ed882c5d-d92b-42ce-9c1e-904c0d5de3f9&client_id=account_b2c&theme=light#/'


def test_auth_for_invalid_number_phone(web_browser):

    """тест проверяющий возможность авторизации зарегестрированного пользователя с неправильным номером телефона"""

    page = AuthPage(web_browser)

    page.number.send_keys('invalid_number_phone')

    page.password.send_keys('Your_password')

    page.btn.click()

    assert page.get_current_url() != 'https://b2c.passport.rt.ru/account_b2c/page?state=ed882c5d-d92b-42ce-9c1e-904c0d5de3f9&client_id=account_b2c&theme=light#/'

def test_authorisation_for_temporary_code(web_browser):

    """тест проверяющию возможность получить временный код с использованием некорректного номера телефона"""

    page = AuthPage(web_browser)

    button_code = web_browser.find_element(By.XPATH, '//*[@id="back_to_otp_btn"]')

    input_number = web_browser.find_element(By.XPATH, '//*[@id="address"]')

    button_get_code = web_browser.find_element(By.XPATH, '//*[@id="otp_get_code"]')

    button_code.click()

    input_number.send_keys('invalid_number_phone')

    button_get_code.click()

    assert page.get_current_url() != 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=053cd459-327d-4b82-93a1-9465b55fccc5&client_id=lk_onlime&tab_id=IPyVtYSxPvI'

def test_auth_invalid_data_for_vk(web_browser):

    """тест проверяющий возможность авторизации с использованием некорректных данных"""

    page = AuthPage(web_browser)

    button_vk = web_browser.find_element(By.XPATH, '//*[@id="oidc_vk"]/svg')

    button_vk.click()

    input_email = web_browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/section/div/div/div/input')

    input_email.send_keys('invalid_email')

    btn_resume = web_browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div[1]/button[1]/span[1]/span')

    btn_resume.click()

    messenge = web_browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/section/div/div/span/span/span').text

    assert messenge == 'Аккаунт не найден.'