from pages.auth_page import AuthPage
import pytest, libch


#
# Тесты авторизации по логину и паролю - 23 тестов
#

@pytest.mark.positive
class TestAuthorisation:
    """Класс позитивных тестов"""

    @pytest.mark.parametrize("login", ['+79996781510', 'jetowej607@tipent.com', 'rtkid_1691659653400'], \
                             ids=['registered phone', 'registered email', 'registered login'])
    def test_authorisation_with_phone_email_login(self, web_browser, login):
        """Группа позитивных тестов на авторизацию.
           При вводе корректных значений телефона, email,
           логина(кроме личевого счета) нужный таб выбирается автоматически."""
        auth_page = AuthPage(web_browser)
        auth_page.login.send_keys(login)
        registered_pass = "PASSword0"
        auth_page.password.send_keys(registered_pass)
        # auth_page.wait_page_loaded(sleep_time=15)  #Если нужно ввести капчу вручную
        auth_page.btn.click()

        assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in auth_page.get_current_url()

    @pytest.mark.skip(reason='No Personal Account')
    @pytest.mark.xfail(reason='No Personal Account')
    @pytest.mark.parametrize("login, password", [('****pa*****', '8symbols'), ('****pa*****', '20symbolssssssssssss')], \
                             ids=['low limit pass', 'upper limit pass'])
    def test_authorisation_with_pa(self, web_browser, login, password):
        """Тест авторизации по лицевому счету.
           А также тест на соответствие допустимой длины пароля,
           согласно требованиям(8-20 символов)."""
        auth_page = AuthPage(web_browser)
        auth_page.tab_pa.click()
        auth_page.login.send_keys(login)
        auth_page.password.send_keys(password)
        auth_page.wait_page_loaded(sleep_time=15)  # Если нужно ввести капчу вручную
        auth_page.btn.click()

        assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in auth_page.get_current_url()




@pytest.mark.negative
class TestAuthorisationNegative:
    """Группа негативных тестов на авторизацию с неверными и не допустимыми данными.
       Техника предугадывания ошибки - текстовое поле(нет смысла вводить INT_MAX, а также отрицательные и прочие числа);
       проверка телефона, логина, ЛС, email происходит на сервисе по шаблону.
       Нет смысла тестировать комбинацию значений двух полей сразу.
       Для сокращения числа тестов, тестируются отдельно поля логина и пароля"""

    @pytest.mark.parametrize("login_field", ['+78886781510', '-7 547 56666,55.567-5757', '', 'efevev@vevreve.com', 'wcw@ed-fv@.com.ru', \
                                       'rtkid_9999999999999', 'rtkid_999aa999999', '-12.3了人我中$%^&*', libch.generate_string(255),libch.generate_string(1001)], \
                                        ids=['non-existent phone', 'incorrect phone', 'empty string', 'non-existent email', 'incorrect email', \
                                             'non-existent login', 'incorrect login', 'special chars', 'string(255)', 'string(1001)'])
    def test_authorisation_with_phone_email_login_negative(self, web_browser, login_field):
        """Тест поля для ввода телефона, логина, почты."""
        auth_page = AuthPage(web_browser)
        auth_page.login.send_keys(login_field)
        auth_page.password.send_keys('ValidP@ssw0rd')
        auth_page.wait_page_loaded(sleep_time=15)  # Если нужно ввести капчу вручную
        auth_page.btn.click()

        error_msg = auth_page.errormsg(('id', "form-error-message"))
        if not error_msg:
            error_msg = auth_page.errormsg(('xpath', '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span'))

        assert error_msg == 'Неверный логин или пароль' or error_msg == 'Введите' \
               or 'https://b2c.passport.rt.ru/account_b2c/page?state=' not in auth_page.get_current_url()




    @pytest.mark.xfail(reason='No Personal Account')
    @pytest.mark.parametrize("login_field", ['574012777000', '', '-12.3了人我中$%^&*', libch.generate_string(255),libch.generate_string(1001)], \
                                        ids=['non-existent personal account', 'empty string', 'special chars', 'string(255)', 'string(1001)'])
    def test_authorisation_with_phone_email_login_negative(self, web_browser, login_field):
        """Тест поля для ввода лс."""
        auth_page = AuthPage(web_browser)
        auth_page.tab_pa.click()
        auth_page.login.send_keys(login_field)
        auth_page.password.send_keys('ValidP@ssw0rd')
        auth_page.wait_page_loaded(sleep_time=15)  # Если нужно ввести капчу вручную
        auth_page.btn.click()

        error_msg = auth_page.errormsg(('id', "form-error-message"))
        if not error_msg:
            error_msg = auth_page.errormsg(('xpath', '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span'))

        assert error_msg == 'Неверный логин или пароль' or error_msg == 'Введите' \
               or 'https://b2c.passport.rt.ru/account_b2c/page?state=' not in auth_page.get_current_url()





    @pytest.mark.parametrize("password_field", ['Non-existentP@ssw0rd', '7Sym-ls', '21symbolsssssssssssss', '', \
                                                libch.RANDOM_STRING, libch.generate_string(255), libch.generate_string(1001)], \
                             ids=['non-existent password', '7 symbols', '21 symbols', \
                                  'empty string', 'special chars', 'string(255)', 'string(1001)'])
    def test_authorisation_with_pa_negative(self, web_browser, password_field):
        """Тест поля для ввода пароля."""
        auth_page = AuthPage(web_browser)
        auth_page.tab_pa.click()
        valid_personal_account = '574012777000'
        auth_page.login.send_keys(valid_personal_account)
        auth_page.password.send_keys(password_field)
        # auth_page.wait_page_loaded(sleep_time=15)  #Если нужно ввести капчу вручную
        auth_page.btn.click()

        error_msg = auth_page.errormsg(('id', "form-error-message"))
        assert error_msg == 'Неверный логин или пароль' \
               or 'https://b2c.passport.rt.ru/account_b2c/page?state=' not in auth_page.get_current_url()
        # or error_msg.text == 'Неверно введен текст с картинки'
