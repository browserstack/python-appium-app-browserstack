from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
options = XCUITestOptions().load_capabilities({
    # Specify device and os_version for testing
    "deviceName": "iPhone XS",
    "platformName": "ios",
    "platformVersion": "12"

    # Add your caps here
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

# Test case for the BrowserStack sample iOS app. 
# If you have uploaded your app, update the test case here. 
test_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "TestBrowserStackLocal"))
)
test_button.click()
result_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "ResultBrowserStackLocal")
result_string = result_element.text.lower()
if result_string.__contains__("not working"):
    screenshot_file = "%s/screenshot.png" % os.getcwd()
    driver.save_screenshot(screenshot_file)
    print ("Screenshot stored at %s" % screenshot_file)
    print ("Unexpected BrowserStackLocal test result")
else:
    assert(result_string.__contains__("up and running"))

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
