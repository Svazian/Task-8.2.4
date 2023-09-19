from pages.main_page import MainPage
from setting import *
from time import *


 #1) ТС RT 001 Меню выбора типа аутентификации: таб Номер
def test_tab_phone(driver):
    main_page = MainPage(driver)
    phone_tab = main_page.is_visible(MainPage.PHONE_TAB)
    phone_tab_text = phone_tab.text
    main_page.find_element_and_click(MainPage.PHONE_TAB)
    phone_auth = main_page.is_visible(MainPage.PlACEHOLDER_AUTH)
    placeholder_text = phone_auth.text

    assert placeholder_text == "Мобильный телефон", "Элемент с таким названием не найден"

    assert phone_tab_text == "Номер", "Элемент с таким названием не найден"


#  2) ТС RT 002 Меню выбора типа аутентификации: таб Почта
def test_tab_mail(driver):
    main_page = MainPage(driver)
    email_tab = main_page.is_visible(MainPage.EMAIL_TAB)
    email_tab_text = email_tab.text
    main_page.find_element_and_click(MainPage.EMAIL_TAB)
    email_auth = main_page.is_visible(MainPage.PlACEHOLDER_AUTH)
    placeholder_text = email_auth.text

    assert email_tab_text == "Почта", "Элемент с таким названием не найден"
    assert placeholder_text == "Электронная почта", "Элемент с таким названием не найден"

#  3) ТС RT 003 Меню выбора типа аутентификации: таб Логин
def test_tab_login(driver):
    main_page = MainPage(driver)
    login_tab = main_page.is_visible(MainPage.LOGIN_TAB)
    login_tab_text = login_tab.text
    main_page.find_element_and_click(MainPage.LOGIN_TAB)
    login_auth = main_page.is_visible(MainPage.PlACEHOLDER_AUTH)
    placeholder_text = login_auth.text

    assert login_tab_text == "Логин", "Элемент с таким названием не найден"
    assert placeholder_text == "Логин", "Элемент с таким названием не найден"


#  4) ТС RT 003 Меню выбора типа аутентификации: таб Лицевой счет
def test_tab_account(driver):
    main_page = MainPage(driver)
    ls_tab = main_page.is_visible(MainPage.LS_TAB)
    ls_tab_text = ls_tab.text
    main_page.find_element_and_click(MainPage.LS_TAB)
    ls_auth = main_page.is_visible(MainPage.PlACEHOLDER_AUTH)
    placeholder_text = ls_auth.text

    assert ls_tab_text == "Лицевой счет", "Элемент с таким названием не найден"
    assert placeholder_text == "Лицевой счет", "Элемент с таким названием не найден"