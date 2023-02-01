from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browserstack.local import Local
import time

# Initialize the remote Webdriver using BrowserStack remote URL
driver = webdriver.Remote("http://hub.browserstack.com/wd/hub")#, options=options)

# Test case for the BrowserStack sample Android app. 
# If you have uploaded your app, update the test case here. 
test_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ID, "com.example.android.basicnetworking:id/test_action"))
)
test_button.click()
WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.TextView"))
)
test_element = None
search_results = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.TextView")
for result in search_results:
    if result.text.__contains__("The active connection is"):
        test_element = result
if test_element is None:
    raise Exception("Cannot find the needed TextView element from app")
matched_string = test_element.text
print (matched_string)
assert(matched_string.__contains__("The active connection is wifi"))
assert(matched_string.__contains__("Up and running"))

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
