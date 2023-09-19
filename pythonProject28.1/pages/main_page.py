from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver.get('https://b2c.passport.rt.ru/')

    PHONE_TAB = (By.XPATH, "//div[@id='t-btn-tab-phone']")
    EMAIL_TAB = (By.XPATH, "//div[@id='t-btn-tab-mail']")
    LS_TAB = (By.XPATH, "//div[@id='t-btn-tab-ls']")
    LOGIN_TAB = (By.XPATH, "//div[@id='t-btn-tab-login']")
    AUTORIZATION = (By.XPATH, "//input[@id='username']")
    PASSWORD_AUTH = (By.XPATH, "//input[@id='password']")
    PlACEHOLDER_AUTH = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div[1]/div[2]/div/span[2]")
    BTN_AUTH = (By.XPATH, "//button[@id='kc-login']")
    LINK_FORGOT_PASS = (By.XPATH, "//a[@id='forgot_password']")
    PAGE_RIGHT = (By.XPATH, '//*[@id="page-right"]/div/div/h1')
    PAGE_NOT_UNIC = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/h2')
    REGISTRATION = (By.XPATH, "//a[@id='kc-register']")
    NAME_REG = (By.XPATH, "//input[@name='firstName']")
    LASTNAME_REG = (By.XPATH, "//input[@name='lastName']")
    REGION = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    EMAIL_REG = (By.XPATH, "//input[@id='address']")
    PASSWORD_REG = (By.XPATH, "//input[@id='password']")
    PASSWORD_REG_CONF = (By.XPATH, "//input[@id='password-confirm']")
    BUTTON_REG = (By.XPATH, "//button[@name='register']")
    NAME_REG_ERROR = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div[1]/div[1]/span")
    CONFIRM_ERROR = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div[4]/div[2]/span")
    PASSWORD_INVALID_ERROR = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div[4]/div[1]/span")
    PASSWORD_INVALID_LEN = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div[4]/div[1]/span")
    VK = (By.CSS_SELECTOR, '#oidc_vk>svg')
    LABLE_VK = (By.CSS_SELECTOR, '#install_allow')
    OK = (By.CSS_SELECTOR, '#oidc_ok>svg')
    LABLE_OK = (By.CSS_SELECTOR, '#widget-el>div.ext-widget_h>div')