from pages.registration_page import RegPage
from pages.auth_page import AuthPage
import pytest, libch, libf



# Тесты формы регистрации - 16-тестов.
# Форма регистрации по прямой ссылки не открывается в тестовом ПО,
# поэтому используется форма авторизации и ссылка на ней.


@pytest.mark.positive
class TestRegistrationPage:
    """Класс позитивных тестов."""

    @pytest.mark.parametrize("fname", ['Им', 'Имя', libch.generate_string(29, 'и') , libch.generate_string(15, 'м'),  libch.generate_string(30, 'м')], \
                             ids=['Им', 'Имя', '29"и"', '15"м"', '30"м"'])
    def test_registration_fname_field(self, web_browser, fname):
        """Тест поля имени, согласно требованиям."""
        auth_page = AuthPage(web_browser)
        auth_page.reg_link.click()

        reg_page = RegPage(web_browser, auth_page.get_current_url())
        reg_page.name.send_keys(fname)
        reg_page.lname.send_keys('Фамилия')
        reg_page.email.send_keys('wijof73343@weishu8.com')
        password = libf.generatehexstring(12)
        reg_page.passwd.send_keys(password)
        reg_page.cpasswd.send_keys(password)
        reg_page.btn_reg.click()
        reg_page.wait_page_loaded(sleep_time=35)  #Если нужно ввести код подтверждения вручную

        assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in reg_page.get_current_url(), "Неуспешная регистрация"


    @pytest.mark.parametrize("lname", ['Фа', 'Фам', libch.generate_string(29, 'и'), libch.generate_string(15, 'м'), libch.generate_string(30, 'м')], \
                             ids=['Фа', 'Фам', '29"и"', '15"м"', '30"м"'])
    def test_registration_lname_field(self, web_browser, lname):
        """Тест поля фамилии, согласно требованиям."""
        auth_page = AuthPage(web_browser)
        auth_page.reg_link.click()

        reg_page = RegPage(web_browser, auth_page.get_current_url())
        reg_page.name.send_keys('Имя')
        reg_page.lname.send_keys(lname)
        reg_page.email.send_keys('wijof43@weishu8.com')
        password = libf.generatehexstring(12)
        reg_page.passwd.send_keys(password)
        reg_page.cpasswd.send_keys(password)
        reg_page.btn_reg.click()
        reg_page.wait_page_loaded(sleep_time=35)  #Если нужно ввести код подтверждения вручную

        assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in reg_page.get_current_url(), "Неуспешная регистрация"



    @pytest.mark.parametrize("login", ['9994565420', '+7999456-14-25', '-79851152635', '7 (999) 456-14-20', 'Wozmojniy-e_mai.l@ecec4vf.com', \
                                       libch.generate_string(63)+'@somthingdomen.ru'], \
                             ids=['9994565420-Valid Phone', '+7999456-14-25-Valid Phone', '-79851152635-Valid Phone', \
                                  '7 (999) 456-14-20-Valid Phone', 'Wozmojniy-e_mai.l@ecec4vf.com-Valid Email', \
                                  '63symbols in username-Valid Email'])
    def test_registration_lоgin_field(self, web_browser, login):
        """Тест поля логина."""
        auth_page = AuthPage(web_browser)
        auth_page.reg_link.click()

        reg_page = RegPage(web_browser, auth_page.get_current_url())
        reg_page.name.send_keys('Имя')
        reg_page.lname.send_keys('Фамилия')
        reg_page.email.send_keys(login)
        password = libf.generatehexstring(12)
        reg_page.passwd.send_keys(password)
        reg_page.cpasswd.send_keys(password)
        reg_page.btn_reg.click()
        reg_page.wait_page_loaded(sleep_time=35)  #Если нужно ввести код подтверждения вручную

        assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in reg_page.get_current_url(), "Неуспешная регистрация"



    @pytest.mark.parametrize("login, password", [('Wozmojni.email@ececf33.com', libf.generatehexstring(8)), \
                                                 ('AnotherEmail@ececf.com', libf.generatehexstring(20)), \
                                                 ('OtherValidEmail@email.com', libf.generatehexstring(15))], \
                                                    ids=['8Sybbols password', '15 symbols password',' 20Symbols password'])
    def test_registration_pass_field(self, web_browser, login, password):
        """Тест полей для ввода пароля."""
        auth_page = AuthPage(web_browser)
        auth_page.reg_link.click()

        reg_page = RegPage(web_browser, auth_page.get_current_url())
        reg_page.name.send_keys('Имя')
        reg_page.lname.send_keys('Фамилия')
        reg_page.email.send_keys(login)
        reg_page.passwd.send_keys(password)
        reg_page.cpasswd.send_keys(password)
        reg_page.btn_reg.click()
        reg_page.wait_page_loaded(sleep_time=35)  # Если нужно ввести код подтверждения вручную

        assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in reg_page.get_current_url(), "Неуспешная регистрация"



@pytest.mark.negative
class TestRegistrationPageNegative:
    # /* ..............................
    # .................................
    # .................................
    # .................................
    # /*
    pass

