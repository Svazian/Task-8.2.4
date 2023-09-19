import pytest
from pages.main_page import MainPage
from setting import *


# ТС RT 007 Ссылка Забыли пароль работает
def test_forgot_pass(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.LINK_FORGOT_PASS)
    forg_passw = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert forg_passw == BaseUrl.FORG_PASSWORD