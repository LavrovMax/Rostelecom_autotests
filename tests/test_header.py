import pytest
from pages.auth_page import AuthPage
from selenium.webdriver.common.by import By


def test_btn_rt(web_browser):

    """тест проверяющий работоспособновсть вкладки ведущий на сайт ростелекома"""

    page = AuthPage(web_browser)

    page.email.send_keys('Lavrovmax4571@mail.ru')

    page.password.send_keys('Gfhfyjqz91')

    page.btn.click()

    button_rt = web_browser.find_element(By.XPATH, '//*[@id="rt-btn"]')

    button_rt.click()

    assert page.get_current_url() == 'https://msk.rt.ru/'

def test_business_tab(web_browser):

    """тест проверяющий работоспособность вкладки для бизнеса"""

    page = web_browser.get('https://msk.rt.ru/')

    button_business = web_browser.find_element(By.XPATH, '//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[1]/a[2]')

    button_business.click()

    assert page.get_current_url() == 'https://msk.rt.ru/b2b'

def test_for_operators_tab(web_browser):

    """тест проверяющий работоспособность вкладки для операторов"""

    page = web_browser.get('https://msk.rt.ru/')

    button_business = web_browser.find_element(By.XPATH, '//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[1]/a[2]')

    button_business.click()

    assert page.get_current_url() == 'https://msk.rt.ru/b2b'

def test_the_blog_tab(web_browser):

    """тест проверяющий работоспособность вкладки блог"""

    page = web_browser.get('https://msk.rt.ru/')

    button_menu = web_browser.find_elements(By.XPATH, '//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[2]/div/svg')

    button_menu.click()

    button_blog = web_browser.find_element(By.XPATH, '//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[2]/div[2]/a[2]')

    button_blog.click()

    assert page.get_current_url() == 'https://blog.rt.ru/'

def test_the_help_tab(web_browser):

    """тест проверяющий работоспособность вкладки помощь"""

    page = web_browser.get('https://msk.rt.ru/')

    button_help = web_browser.find_elements(By.XPATH, '//*[@id="block-b2cverkhneemenyuvozlelogotipanovoe"]/div/div/div/div[1]/a[1]/span[1]')

    button_help.click()

    assert page.get_current_url() == 'https://msk.rt.ru/help'

def test_about_the_company(web_browser):

    """тест проверяющий работоспособность вкладки о компании"""

    page = web_browser.get('https://msk.rt.ru/')

    button_menu = web_browser.find_element(By.XPATH, '//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[2]/div[1]')

    button_about_the_company = web_browser.find_element(By.XPATH, '//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[2]/div[2]/a[5]/span[1]')

    button_menu.click()

    button_about_the_company.click()

    assert page.get_current_url() == 'https://www.company.rt.ru/about/info/'

def test_for_partners(web_browser):

    """тестирование вкладки для партнеров"""

    page = web_browser.get('https://msk.rt.ru/')

    button_menu = web_browser.find_element(By.XPATH, '//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[2]/div[1]')

    button_for_partners = web_browser.find_element(By.XPATH, '//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[2]/div[2]/a[4]/span[1]')

    button_menu.click()

    button_for_partners.click()

    assert page.get_current_url() == 'https://msk.rt.ru/partners'

def test_for_investors(web_browser):

    """тестирование вкладки для инвесторов"""

    page = web_browser.get('https://msk.rt.ru/')

    button_menu = web_browser.find_element(By.XPATH, '//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[2]/div[1]')

    button_for_investors = web_browser.find_element(By.XPATH, '//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[2]/div[2]/a[5]')

    button_menu.click()

    button_for_investors.click()

    assert page.get_current_url() == 'https://www.company.rt.ru/ir/'

def test_bonuses_tab(web_browser):

    """тестирование вкладки бонусы"""

    page = web_browser.get('https://msk.rt.ru/')

    button_headder_menu = web_browser.find_element(By.XPATH, '/html/body/div[3]/div/div/header/div[1]/div[1]/div/div[2]/div[1]/div[2]')

    button_headder_menu.click()

    button_bonuses = web_browser.find_element(By.XPATH, '//*[@id="block-b2cverkhneemenyuvozlelogotipatouch"]/div/div/a[2]/div/div/div')

    button_bonuses.click()

    assert page.get_current_url() == 'https://msk.rt.ru/bonus'

def test_services(web_browser):

    """тестирование вкладки услуги Ростелекома"""

    page = web_browser.get('https://msk.rt.ru/')

    button_headder_menu = web_browser.find_element(By.XPATH, '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[1]/div[2]')

    button_headder_menu.click()

    button_payment = web_browser.find_element(By.XPATH, '//*[@id="block-b2cverkhneemenyuvozlelogotipatouch"]/div/div/div/div')

    button_payment.click()

    button_services = web_browser.find_element(By.XPATH, '//*[@id="block-b2cverkhneemenyuvozlelogotipatouch"]/div/div/a[1]/div/div/div')

    button_services.click()

    assert page.get_current_url == 'https://msk.rt.ru/payment'