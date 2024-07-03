from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    "deviceName": "Google Pixel 3",
    "platformName": "android",
    "platformVersion": "9.0",

    # Add your caps here
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

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
