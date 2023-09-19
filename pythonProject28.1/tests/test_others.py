from pages.main_page import MainPage
from setting import *

#    Кнопка "VК" кликабельна, и открывает форму для регистранции через аккаунт "Одноклассники"
def test_vk_is_available(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.VK)
    vk_avail = main_page.get_text_of_element(MainPage.LABLE_VK)
    assert vk_avail == BaseUrl.VK


#    Кнопка "ОК" кликабельна, и открывает форму для регистранции через аккаунт "Одноклассники"
def test_ok_is_available(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.OK)
    ok_avail = main_page.get_text_of_element(MainPage.LABLE_OK)
    assert ok_avail == BaseUrl.OK