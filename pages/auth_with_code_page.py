from pages.base import WebPage
from pages.elements import WebElement


class AuthPageCode(WebPage):

    def __init__(self, web_driver, url='https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_decosystems&redirect_uri=https://start.rt.ru/&response_type=code&scope=openid&theme=light'):
        super().__init__(web_driver, url)

    login = WebElement(id="address")
    btn = WebElement(wait_after_click=False, id="otp_get_code")
