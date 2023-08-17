import pytest
import uuid

from selenium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def web_browser(request):

    # service = Service('../chdrv.exe')
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # browser = webdriver.Chrome(service=service, options=chrome_options)
    
    browser = Service('../chdrv.exe')
    browser = webdriver.Chrome(service=browser)
    browser.maximize_window()
    
    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:

        # Make screen-shot for local debug:
        browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

        # For happy debugging:
        print('URL: ', browser.current_url)
        print('Browser logs:')
        for log in browser.get_log('browser'):
            print(log)

    # browser.save_screenshot('screenshots\\' + request.function.__name__ + '.png')
    browser.quit()
