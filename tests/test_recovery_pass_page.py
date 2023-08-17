from pages.recovery_pass_page import RecoveryPageFirst
from pages.recovery_pass_page import RecoveryPageSecond
from pages.auth_page import AuthPage
import pytest, libch

#
# Тесты восстановления пароля 24-теста
#



@pytest.mark.positive
class TestRecoveryPass:
    """Класс позитивных тестов страницы восстановления пароля.
       Техника классов эквивалентности - парольная строка от 8 до 20 символов включительно."""

    @pytest.mark.parametrize("login", ['+7 999 678 15 10', 'jetowej607@tipent.com', 'rtkid_1691659653400'],
                             ids=['registered phone', 'registered email', 'registered login'])
    def test_recovery_pass_with_phone_email_login(self, web_browser, login):
        """Тест восстановления пароля по телефону, логину, почте. Нижняя граница допустимой длины поля пароль.
           Техника перехода состояний - после ввода нового пароля осуществляется переход на страницу авторизации(проверяем это).
           Для проверки изменения пароля регистрируемся с ним в системе."""
        first_page = RecoveryPageFirst(web_browser)
        first_page.login.send_keys(login)
        first_page.wait_page_loaded(sleep_time=20)      #Если нужно ввести капчу вручную
        first_page.btn.click()
        first_page.wait_page_loaded(sleep_time=30)        #Для ввода кода родтверждения

        second_page = RecoveryPageSecond(web_browser, first_page.get_current_url())
        second_page.pass_new.send_keys('P@SSw0rd')      #Пароль 8 символов
        second_page.pass_confirm.send_keys('P@SSw0rd')  #Пароль 8 символов
        second_page.btn_save_pass.click()

        assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate' in second_page.get_current_url(), "Не перешел на страницу авторизации"

        # После восстановления пароля проверяем авторизацию
        auth_page = AuthPage(web_browser, second_page.get_current_url())
        auth_page.login.send_keys(login)
        auth_page.password.send_keys('P@SSw0rd')
        # page.wait_page_loaded(sleep_time=15)  #Если нужно ввести капчу вручную
        auth_page.btn.click()

        assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in auth_page.get_current_url(), \
            "Ошибка авторизации Логин: {0}, Пароль: P@SSw0rd".format(login)




    @pytest.mark.skip(reason='No Personal Account')
    @pytest.mark.xfail(reason='No Personal Account')
    @pytest.mark.parametrize("pa, password", [('pa', '20symbolssssssssssss')], ids=['registered PA and registered password'])
    def test_recovery_pass_with_pa(self, web_browser, pa, password):
        """Тест восстановления пароля по лицевому счету + верхняя граница длины поля пароль."""
        first_page = RecoveryPageFirst(web_browser)
        first_page.tab_pa.click()
        first_page.login.send_keys(pa)
        first_page.wait_page_loaded(sleep_time=20)      #Если нужно ввести капчу вручную
        first_page.btn.click()
        first_page.wait_page_loaded(sleep_time=30)        #Для ввода кода родтверждения

        second_page = RecoveryPageSecond(web_browser, first_page.get_current_url())
        second_page.pass_new.send_keys(password)
        second_page.pass_confirm.send_keys(password)
        second_page.btn_save_pass.click()

        assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate' in second_page.get_current_url(), "Не перешел на страницу авторизации"

        # После восстановления пароля проверяем авторизацию
        auth_page = AuthPage(web_browser, second_page.get_current_url())
        auth_page.login.send_keys(pa)
        auth_page.password.send_keys('P@SSw0rd')
        # page.wait_page_loaded(sleep_time=15)  #Если нужно ввести капчу вручную
        auth_page.btn.click()

        assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in auth_page.get_current_url(), \
            "Ошибка авторизации Логин: {0}, Пароль: P@SSw0rd".format(pa)





@pytest.mark.negative
class TestRecoveryPassNegative:
    """Класс негативных тестов."""

    @pytest.mark.parametrize("login_field", ['+78886781510', '-7 547 56666,55.567-5757', '', 'efevev@vevreve.com', 'wcw@ed-fv@.com.ru', \
                              'rtkid_9999999999999', 'rtkid_999aa999999', libch.RANDOM_STRING, libch.generate_string(255), libch.generate_string(1001)], \
                             ids=['non-existent phone', 'incorrect phone', 'empty string', 'non-existent email', 'incorrect email', \
                                  'non-existent login', 'incorrect login', 'special chars', 'string(255)', 'string(1001)'])
    def test_recovery_pass_with_phone_email_login_negative(self, web_browser, login_field):
        """Тест поля для ввода телефона, почты, логина."""
        first_page = RecoveryPageFirst(web_browser)
        first_page.login.send_keys(login_field)
        # first_page.wait_page_loaded(sleep_time=15)  #Если нужно ввести капчу вручную
        first_page.btn.click()

        error_msg = first_page.errormsg(('id', "form-error-message"))
        if not error_msg:
            error_msg = first_page.errormsg(('xpath', '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span'))

        assert error_msg == 'Неверный логин или пароль' or error_msg == 'Введите' \
            or 'https://b2c.passport.rt.ru/account_b2c/page?state=' not in first_page.get_current_url()



    @pytest.mark.parametrize("login_field", ['574012777000', '', '-12.3了人我中$%^&*', libch.generate_string(255),libch.generate_string(1001)], \
                                        ids=['non-existent personal account', 'empty string', 'special chars', 'string(255)', 'string(1001)'])
    def test_recovery_pass_with_phone_email_login_negative(self, web_browser, login_field):
        """Тест поля для ввода лс."""
        first_page = RecoveryPageFirst(web_browser)
        first_page.login.send_keys(login_field)
        # first_page.wait_page_loaded(sleep_time=15)  #Если нужно ввести капчу вручную
        first_page.btn.click()

        error_msg = first_page.errormsg(('id', "form-error-message"))
        if not error_msg:
            error_msg = first_page.errormsg(('xpath', '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span'))

        assert error_msg == 'Неверный логин или пароль' or error_msg == 'Введите' \
            or 'https://b2c.passport.rt.ru/account_b2c/page?state=' not in first_page.get_current_url()



    @pytest.mark.skip(reason='No Personal Account')
    @pytest.mark.xfail(reason='No Personal Account')
    @pytest.mark.parametrize("password_field", ['7Sym-ls', '21symbolsssssssssssss', '', \
                                          libch.RANDOM_STRING, libch.generate_string(255), libch.generate_string(1001)], \
                                          ids=['7 symbols', '21 symbols', \
                                               'empty string', 'special chars', 'string(255)', 'string(1001)'])
    def test_recovery_pass_with_pa(self, web_browser, password_field):
        """Тест поля для ввода пароля."""

        first_page = RecoveryPageFirst(web_browser)
        # first_page.tab_pa.click()
        valid_pa = '574012777000'
        first_page.login.send_keys(valid_pa)
        first_page.wait_page_loaded(sleep_time=15)      #Если нужно ввести капчу вручную
        first_page.btn.click()
        first_page.wait_page_loaded(sleep_time=30)        #Для ввода кода родтверждения

        second_page = RecoveryPageSecond(web_browser, first_page.get_current_url())
        second_page.pass_new.send_keys(password_field)
        second_page.pass_confirm.send_keys(password_field)
        second_page.btn_save_pass.click()

        error_msg = second_page.errormsg(('xpath', '//*[@id="page-right"]/div/div/div/form/div/div[1]/span'))
        assert bool(error_msg) == True




    @pytest.mark.parametrize("login", ['+9851167924', 'jetowej607@tipent.com', 'rtkid_1691659653400'], \
                             ids=['registered phone', 'registered email', 'registered login'])
    @pytest.mark.parametrize("password", ['P@SSw0rd'], ids=['mismatched password'])
    def test_password_confirmation(self, web_browser, login, password):
        """Тест подтверждения пароля."""
        first_page = RecoveryPageFirst(web_browser)
        first_page.login.send_keys(login)
        first_page.wait_page_loaded(sleep_time=15)      #Если нужно ввести капчу вручную
        first_page.btn.click()
        first_page.wait_page_loaded(sleep_time=30)        #Для ввода кода родтверждения

        second_page = RecoveryPageSecond(web_browser, first_page.get_current_url())
        second_page.pass_new.send_keys('P@PASSword0')
        second_page.pass_confirm.send_keys(password)   #Несовпадающий пароль
        second_page.btn_save_pass.click()

        error_msg = second_page.errormsg(('xpath', '//*[@id="page-right"]/div/div/div/form/div/div[2]/span'))
        assert bool(error_msg) == True
