#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os
import pickle

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=ed882c5d-d92b-42ce-9c1e-904c0d5de3f9&theme=light&auth_type'

        super().__init__(web_driver, url)

