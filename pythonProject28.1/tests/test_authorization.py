import pytest
import time

from pages.main_page import MainPage
from setting import *



# ТС RT 005 Авторизация пользователя по номеру телефона
def test_auhorization_phone(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.PHONE_TAB)
    main_page.input_data(MainPage.AUTORIZATION, valid_phone)
    main_page.input_data(MainPage.PASSWORD_AUTH, valid_password)
    time.sleep(20) #На случай необходимости ввода капчи
    main_page.find_element_and_click(MainPage.BTN_AUTH)
    targetURL = driver.current_url.find('/account_b2c/')

    assert targetURL != -1, 'Ошибка авторизации'

# ТС RT 006 Авторизация пользователя по почте
def test_auhorization_mail(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.EMAIL_TAB)
    main_page.input_data(MainPage.AUTORIZATION, valid_email)
    main_page.input_data(MainPage.PASSWORD_AUTH, valid_password)
    time.sleep(20) #На случай необходимости ввода капчи
    main_page.find_element_and_click(MainPage.BTN_AUTH)
    targetURL = driver.current_url.find('/account_b2c/')

    assert targetURL != -1, 'Ошибка авторизации'