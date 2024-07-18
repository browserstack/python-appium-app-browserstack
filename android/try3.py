
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time
import json
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.touch_action import TouchAction


bs_username = 'dheerajsurakasul_Q7m2uU'
bs_access_key = "zfFk58FFmpo2EXcoxaVY"


bs_caps = {
    "browserstack.user":bs_username ,
    "browserstack.key": bs_access_key,
    "device": "Google Pixel 5",
    "os_version": "12.0",
    "real_mobile": "true",
    "app": "bs://cb2ab40efd24469e530cd0607f8b0a5b191bff30",
    "name": "Appium Test with BrowserStack",
}

driver = webdriver.Remote(
    command_executor="https://hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=bs_caps
)

language_indices = {
    'french': 1,
    'spanish': 2,
    'arabic':3,
    'german':4,
    'english':5,
    'bengali':6,
    'nepali':7    
}
with open('input.json') as f:
        data = json.load(f)
        selected_language = data['language']
index = language_indices.get(selected_language.lower())
print(selected_language, index)

elements_to_check = [
    (MobileBy.XPATH, '//android.widget.TextView[@text="Continue to app"]', "Continue to app clicked"),
    (MobileBy.XPATH, '//android.widget.TextView[@text="Skip video"]', "Skip video clicked"),
    (MobileBy.XPATH, '//android.widget.Button', "Generic button clicked"),
    (MobileBy.XPATH, '//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/close_icon"]', "Close icon clicked")
]
def handle_ads(driver):
    for locator, xpath, message in elements_to_check:
        try:
            element = WebDriverWait(driver,6).until(EC.presence_of_element_located((locator, xpath)))
            if element.is_displayed():
                element.click()
                print(message)
                break
        except (TimeoutException, NoSuchElementException):
            continue

try:
    element = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((MobileBy.XPATH,"//android.widget.TextView[@text='Continue to app']")))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    xpath = f'(//android.widget.LinearLayout[@resource-id="com.hd.video.downloader.xv:id/ll"])[{index}]'
    element = WebDriverWait(driver,6).until(
        EC.presence_of_element_located((MobileBy.XPATH, xpath)))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver,6).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/next"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

r=3
for i in range(r):
    try:
        element = WebDriverWait(driver,6).until(
            EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/btnNext"]')))
        if element.is_displayed():
            element.click()
            print("Ok button clicked")
        else:
            handle_ads(driver)
            r+=1
    except Exception as e:
        print(e)
handle_ads(driver)

try:
    element = WebDriverWait(driver,6).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/start"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

handle_ads(driver)

try:
    element = WebDriverWait(driver,6).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/facebook"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

driver.quit()

