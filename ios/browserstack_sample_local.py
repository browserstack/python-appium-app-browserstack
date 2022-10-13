from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browserstack.local import Local
import os

# Set your BrowserStack access credentials here
userName = "YOUR_USERNAME"
accessKey = "YOUR_ACCESS_KEY"

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
options = XCUITestOptions().load_capabilities({
    # Set URL of the application under test
    "app" : "bs://<app-id>",

    # Specify device and os_version for testing
    "deviceName": "iPhone XS",
    "platformName": "ios",
    "platformVersion": "12",

    # Set other BrowserStack capabilities
    "bstack:options": {
        "userName" : userName,
        "accessKey" : accessKey,
        "projectName" : "First Python Local project",
        "buildName" : "browserstack-build-1",
        "sessionName" : "BStack local_test",
        "local" : "true"
    }
})

bs_local = None

def start_local():
    global bs_local
    bs_local = Local()
    bs_local_args = { "key": accessKey, "forcelocal": "true" }
    bs_local.start(**bs_local_args)

def stop_local():
    global bs_local
    bs_local.stop()

def existence_lambda(s):
    result = s.find_element(AppiumBy.ACCESSIBILITY_ID, "ResultBrowserStackLocal").get_attribute("value")
    return result and len(result) > 0

# Start BrowserStack local binary
start_local()

# Initialize the remote Webdriver using BrowserStack remote URL
# and options defined above
driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

# Test case for the BrowserStack sample iOS app. 
# If you have uploaded your app, update the test case here. 
test_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "TestBrowserStackLocal"))
)
test_button.click()
WebDriverWait(driver, 30).until(existence_lambda)
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

stop_local()
