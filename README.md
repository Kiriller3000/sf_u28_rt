# Итоговый проект QAP

    Тестирование интерфеса авторизации, регистрации, восстановления пароля от 
    Ростелеком Информационные технологии.

# Настройка проекта:
    1. Создаем виртуальное окружение командой:
        python -m venv venv
    2. Активируем виртуальное окружение командой (MacOS/Linux):
        source venv/bin/activate
       для Windows другая команда:
        \env\Scripts\activate.bat
    3. Установка зависимостей:
        pip install -r requirements.txt
    4. Настроить в IDE(Pycharm) текущий интерпритатор, выбрав текущее вертуальное окружение


# Запуск тестов:
    Нажмите на зеленую стрелочку слева от названия теста, если она вдруг не появилась, 
    значит вы не установили библиотеку pytest. Установите командой: pip install pytest. 
    
    После этого нужно выбрать PyTest в качестве интерпретатора. Для этого переходим в меню 
    PyCharm —> Preferences —> Tools —> Python integration tools и в разделе Testing выбираем PyTest.

    Для запуска из командной строки Windows перейдите в папку с проектом: 
        pytest --driver Chrome --driver-path chdrv.exe -v tests/<имя_файла_тестов>
        
    <имя_файла_тестов> = test_auth_page - Тестирование страницы авторизации
                         test_auth_with_code_page - Тестирование авторизации с помощью временного кода
                         test_recovery_pass_page - Тестирование восстановления пароля
                         test_registration_page - Тестирование регистрации пользователя в системе
                         
    Для запуска из командной строки MacOS/Linux:
        Загрузите Selenium WebDriver(https://chromedriver.chromium.org/downloads) и 
        бросьте в папку с проектом.
        pytest --driver Chrome --driver-path chromedriver -v tests/<имя_файла_тестов>

    Для браузера Firefox скачайте драйвер(https://github.com/mozilla/geckodriver/releases). 
        OS Windows: pytest --driver Firefox --driver-path geckodriver.exe -v tests/<имя_файла_тестов>
        MacOS/Linux: pytest --driver Firefox --driver-path geckodriver -v tests/<имя_файла_тестов>


