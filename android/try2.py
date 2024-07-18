
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time
import json
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

try:
    element = WebDriverWait(driver, 20).until(
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
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH, xpath)))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/next"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

for i in range(3):
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/btnNext"]')))
        if element.is_displayed():
            element.click()
            print("Ok button clicked")
        else:
            print("Button is not visible.")
    except Exception as e:
        print(e)


try:
    element = WebDriverWait(driver,6).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.TextView[@text="Skip video"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver,2).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.Button')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)


try:
    element = WebDriverWait(driver,6).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/close_icon"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/facebook"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.EditText[@resource-id="com.hd.video.downloader.xv:id/et_text"]')))
    if element.is_displayed():
        element.clear()
        element.send_keys('https://www.facebook.com/gabbybarrett5/videos/pick-me-up-music-video-out-nowhttpsfbwatchcpewlci11v/2797924943847507/')
        print("Data sent")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageView[@resource-id="com.hd.video.downloader.xv:id/loginBtn1"]')))
    if element.is_displayed():
        element.click()
        print("Ok button clicked")
    else:
        print("Button is not visible.")
except Exception as e:
    print(e)
    
driver.quit()