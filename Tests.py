import pytest
import time
from mimesis import Person
from RegistrationPages import RegistrationHelper


# Создаем тестовые случайные данные, для передачи их в форму регистрации.
person = Person('en')
person_email = person.email(domains=['test.com'])
person_phone = person.telephone(mask='1-4##-8##-5##3')


# Прописываем шаги теста, регистрации.
@pytest.mark.webtest
def test_registration(browser):
    registration_main_page = RegistrationHelper(browser)
    registration_main_page.go_to_site()
    print("ШАГИ ТЕСТА: \n\n")
    print("1. Перешли на сайт https://dev.devse.xyz/register. \n")
    registration_main_page.enter_data("Test", "TestFamily", person_email, person_phone, "12332111", "12332111")
    print("2. Ввели тестовые данные, в поля формы регистрации. \n")
    registration_main_page.click_on_the_registration_button()
    print("3. Нажали на кнопку Регистрация, под формой. \n\n")

    time.sleep(3)
    assert "Главная" in registration_main_page.check_present_word()
    print("РЕЗУЛЬТАТ: регистрация прошла успешно. Мы находимся на внутренней странице Dashboard. \n")

