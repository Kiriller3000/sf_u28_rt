from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url='https://b2c.passport.rt.ru/'):
        super().__init__(web_driver, url)

    login = WebElement(id="username")
    password = WebElement(id='password')
    btn = WebElement(wait_after_click=True, id="kc-login")
    tab_email = WebElement(id="t-btn-tab-mail")
    tab_login = WebElement(id="t-btn-tab-login")
    tab_pa = WebElement(id="t-btn-tab-ls")
    reg_link = WebElement(wait_after_click=True, id="kc-register")
