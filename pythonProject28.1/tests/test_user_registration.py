import pytest
from pages.main_page import MainPage
from setting import *
from calculated import *
import time

# ТС RT 008 Коppектность работы ссылки Зарегистрироваться
def test_check_in(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    check = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert check == BaseUrl.CHECK_IN

# ТС RT 009 Регистрация нового полтьзователя Позитивный сценарий
def test_reg_positive(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, valid_name)
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_email)
    main_page.input_data(MainPage.PASSWORD_REG, valid_password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, valid_password)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    regist = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert regist == BaseUrl.CONFIRM_EMAIL

# ТС RT 010 Регистрация пользователя с почтой, которая уже была использована
# для регистрации Негативный сценарий
def test_reg_invalid_mail(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, valid_name)
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_email)
    main_page.input_data(MainPage.PASSWORD_REG, password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, password)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    regist = main_page.get_text_of_element(MainPage.PAGE_NOT_UNIC)
    assert regist == BaseUrl.ACCOUNT_NOT_UNIC

# ТС RT 011 Регистрация пользователя с телефоном, который уже был использован
# для регистрации Негативный сценарий

def test_reg_invalid_phone(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, valid_name)
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_phone)
    main_page.input_data(MainPage.PASSWORD_REG, password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, password)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    regist = main_page.get_text_of_element(MainPage.PAGE_NOT_UNIC)
    assert regist == BaseUrl.ACCOUNT_NOT_UNIC

# ТС RT 012 Регистрация пользователя с невалидным полем Имя (длина символов <2) Негативный сценарий

def test_reg_invalid_name_len_1(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, generate_name(1))
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_phone)
    main_page.input_data(MainPage.PASSWORD_REG, password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, password)
    time.sleep(10)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    error_input_name = main_page.is_visible(MainPage.NAME_REG_ERROR)
    text_error = error_input_name.text
    regist = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert regist != BaseUrl.CONFIRM_EMAIL
    assert text_error == BaseUrl.NAME_INVALID

# ТС RT 012 Регистрация пользователя с невалидным полем Имя (длина символов >30) Негативный сценарий
def test_reg_invalid_name_len_31(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, generate_name(31))
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_phone)
    main_page.input_data(MainPage.PASSWORD_REG, password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, password)
    time.sleep(10)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    error_input_name = main_page.is_visible(MainPage.NAME_REG_ERROR)
    text_error = error_input_name.text
    regist = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert regist != BaseUrl.CONFIRM_EMAIL
    assert text_error == BaseUrl.NAME_INVALID

# ТС RT 012 Регистрация пользователя с невалидным полем Имя (использование латиницы и спецсимволов) Негативный сценарий

def test_reg_invalid_name(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, generate_name(5, valid=False))
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_phone)
    main_page.input_data(MainPage.PASSWORD_REG, password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, password)
    time.sleep(10)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    error_input_name = main_page.is_visible(MainPage.NAME_REG_ERROR)
    text_error = error_input_name.text
    regist = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert regist != BaseUrl.CONFIRM_EMAIL
    assert text_error == BaseUrl.NAME_INVALID

#ТС RT 013 Не совпадают пароли в поле Пароль и Повторите пароль Негативный сценарий
def test_reg_invalid_confirm_password(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, valid_name)
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_email)
    main_page.input_data(MainPage.PASSWORD_REG, valid_password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, password)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    regist = main_page.get_text_of_element(MainPage.CONFIRM_ERROR)
    assert regist == BaseUrl.CONFIRM_PASS_ERROR

    # ТС RT 014 Ввод значения не только с латинскими буквами в поле ввода "Пароль"
def test_reg_invalid_password(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, valid_name)
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_email)
    main_page.input_data(MainPage.PASSWORD_REG, random_invalid_password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, random_invalid_password)
    time.sleep(10)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    regist = main_page.get_text_of_element(MainPage.PASSWORD_INVALID_ERROR)

    assert regist == BaseUrl.PASSWORD_ERROR_INVALID
    assert regist != BaseUrl.CONFIRM_EMAIL


    # ТС RT 015 Ввод значения "Пароль" меньше 8 символов
@pytest.mark.q
def test_reg_invalid_password(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, valid_name)
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_email)
    main_page.input_data(MainPage.PASSWORD_REG, random_invalid_password_len_6)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, random_invalid_password_len_6)
    time.sleep(10)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    regist = main_page.get_text_of_element(MainPage.PASSWORD_INVALID_ERROR)

    assert regist == BaseUrl.PASSWORD_ERROR_INVALID
    assert regist != BaseUrl.CONFIRM_EMAIL