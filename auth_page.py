from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=b7c6ad8e-d017-4029-b117-fbf6ecd87364&theme&auth_type'
        super().__init__(web_driver, url)

    email = WebElement(id='username')

    number = WebElement(id='username')

    password = WebElement(id='password')

    btn = WebElement(id='kc-login')