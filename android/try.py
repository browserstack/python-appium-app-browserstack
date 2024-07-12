from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.touch_action import TouchAction


bs_username = 'dheerajsurakasul_98ku2q'
bs_access_key = "gEYY1vefyyYAENWGCYMc"


bs_caps = {
    "browserstack.user":bs_username ,
    "browserstack.key": bs_access_key,
    "device": "Google Pixel 3",
    "os_version": "12.0",
    "real_mobile": "true",
    "app": "bs://ab8b26223e3dd1c88b1c3254c9a506e56c1361bf",
    "name": "Appium Test with BrowserStack",
}

driver = webdriver.Remote(
    command_executor="https://hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=bs_caps
)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.TextView[@resource-id="com.emicalcultor.loanpro_loanemicalcultor:id/btn1"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.TextView[@resource-id="com.emicalcultor.loanpro_loanemicalcultor:id/next"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageButton[@content-desc="Close tab"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.TextView[@resource-id="com.emicalcultor.loanpro_loanemicalcultor:id/next_btn"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageButton[@content-desc="Close tab"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.emicalcultor.loanpro_loanemicalcultor:id/emi_btn"]/android.widget.ImageView')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageButton[@content-desc="Close tab"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.EditText[@resource-id="com.emicalcultor.loanpro_loanemicalcultor:id/et_total_amount_emi"]')))
    if element.is_displayed():
        element.clear()
        element.send_keys('99999999')
        print("Data sent")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.EditText[@resource-id="com.emicalcultor.loanpro_loanemicalcultor:id/et_int_ret_emi"]')))
    if element.is_displayed():
        element.clear()
        element.send_keys('15')
        print("Data sent")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.EditText[@resource-id="com.emicalcultor.loanpro_loanemicalcultor:id/et_duration_emi"]')))
    if element.is_displayed():
        element.clear()
        element.send_keys('25')
        print("Data sent")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.TextView[@resource-id="com.emicalcultor.loanpro_loanemicalcultor:id/tv_cals_emi"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

driver.quit()