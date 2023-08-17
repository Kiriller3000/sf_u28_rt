from pages.auth_with_code_page import AuthPageCode
import pytest, libch

#
# Тесты авторизации по временному коду - 10 tests
#

@pytest.mark.xfail(reason='No Personal Account')
@pytest.mark.positive
@pytest.mark.parametrize("login_field", ['+79996781510', 'jetowej607@tipent.com', 'rtkid_1691659653400', '574012777000'], \
                         ids=['registered phone', 'registered email', 'unregistered phone', 'unregistered email'])
def test_authorisation_with_code(web_browser, login_field):
    """Позитивные тесты."""
    page = AuthPageCode(web_browser)
    page.login.send_keys(login_field)
    page.wait_page_loaded(sleep_time=20)
    page.btn.click()
    page.wait_page_loaded(sleep_time=30)  #Если нужно ввести код вручную

    assert 'https://start.rt.ru/?tab=main' in page.get_current_url()



@pytest.mark.negative
@pytest.mark.parametrize("login_field", ['-7 000 116-80-25', 'srgb-@..sddfv@wwcwc.nn', '', libch.RANDOM_STRING, \
                                         libch.generate_string(255), libch.generate_string(1001)], \
                                         ids=['unacceptable phone', 'unacceptable email', 'empty field', \
                                         'random string', 'big string', 'very big string'])

def test_authorisation_with_code_negative(web_browser, login_field):
    """Негативные тесты.
       Техника предугадывания ошибки - текстовое поле; проверка телефона и email по шаблону."""
    page = AuthPageCode(web_browser)
    page.login.send_keys(login_field)
    page.btn.click()

    browser = web_browser
    error = browser.find_element('xpath', '//*[@id="page-right"]/div/div/div/form/div[1]/div/span')

    assert error.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
