from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browserstack.local import Local
import os

# Set your BrowserStack access credentials here
userName = "YOUR_USERNAME"
accessKey = "YOUR_ACCESS_KEY"

desired_caps = {
    "browserstack.user" : userName,
    "browserstack.key" : accessKey,

    # Set URL of the application under test
    "app" : "<bs://app-id>",

    # Specify device and os_version for testing
    "device" : "iPhone 11 Pro",
    "os_version" : "13",

    #Set BrowserStack Local capability as True
    "browserstack.local": True,

     # Set other BrowserStack capabilities
    "project" : "First Python Local project", 
    "build" : "browserstack-build-1",
    "name" : "local_test"
}

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
    result = s.find_element_by_accessibility_id("ResultBrowserStackLocal").get_attribute("value")
    return result and len(result) > 0

# Start BrowserStack local binary
start_local()

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_caps
)

# Test case for the BrowserStack sample iOS app. 
# If you have uploaded your app, update the test case here. 
test_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "TestBrowserStackLocal"))
)
test_button.click()
WebDriverWait(driver, 30).until(existence_lambda)
result_element = driver.find_element_by_accessibility_id("ResultBrowserStackLocal")
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
