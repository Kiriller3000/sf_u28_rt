from pages.base import WebPage
from pages.elements import WebElement


class RecoveryPageFirst(WebPage):

    def __init__(self, web_driver, url='https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'):
        super().__init__(web_driver, url)

    login = WebElement(id="username")
    tab_email = WebElement(id="t-btn-tab-mail")
    tab_login = WebElement(id="t-btn-tab-login")
    tab_pa = WebElement(id="t-btn-tab-ls")
    btn = WebElement(wait_after_click=True, id="reset")


class RecoveryPageSecond(WebPage):
    def __init__(self, web_driver, url=''):
        super().__init__(web_driver, url)

    pass_new = WebElement(id="password-new")
    pass_confirm = WebElement(id="password-confirm")
    btn_save_pass = WebElement(wait_after_click=True, id="t-btn-reset-pass")