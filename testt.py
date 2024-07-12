from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:deviceName": "000703437000891",
	"appium:app": "C:\\Users\\sriyo\\Downloads\\Get Diamond FFF Skin Emotes_1.0.0_apkcombo.com.apk",
	"appium:automationName": "UiAutomator2",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)



# time.sleep(5)
# try:
#     element = driver.find_element_by_id('00000000-0000-020c-0000-000900000003')
#     if element.is_displayed():
#         element.click()
#         print("Close button clicked successfully!")
#     else:
#         print("Close button is not visible.")

# except NoSuchElementException:
#     print("Close button not found.")


time.sleep(5)
try:
    element = driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Continue to App FFF Skin Tool"]')
    if element.is_displayed():
        element.click()
        print("Close button clicked successfully!")
    else:
        print("Close button is not visible.")

except NoSuchElementException:
    print("Close button not found.")

