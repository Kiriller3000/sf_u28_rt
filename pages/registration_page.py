from pages.base import WebPage
from pages.elements import WebElement



class RegPage(WebPage):

    def __init__(self, web_driver, url='https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'):
        super().__init__(web_driver, url)

    name = WebElement(name="firstName")
    lname = WebElement(name="lastName")
    region  = WebElement(xpath="//*[@id='page-right']/div/div/div/form/div[2]/div/div/input")
    email = WebElement(id="address")
    passwd = WebElement(id="password")
    cpasswd = WebElement(id="password-confirm")
    btn_reg = WebElement(wait_after_click=True, name="register")

