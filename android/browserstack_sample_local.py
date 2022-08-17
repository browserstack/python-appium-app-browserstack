from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browserstack.local import Local
import time

# Set your BrowserStack access credentials here
userName = "YOUR_USERNAME"
accessKey = "YOUR_ACCESS_KEY"

desired_caps = {
    # Set URL of the application under test
    "app" : "bs://<app-id>",

    # Specify device and os_version for testing
    "deviceName": "Google Pixel 3",
    "platformName": "android",
    "platformVersion": "9.0",

    # Set other BrowserStack capabilities
    "project" : "First Python Local project", 
    "build" : "browserstack-build-1",
    "name" : "local_test",

    # Set other BrowserStack capabilities
    "bstack:options": {
        "userName" : userName,
        "accessKey" : accessKey,
        "projectName" : "First Python Local project",
        "buildName" : "browserstack-build-1",
        "sessionName" : "local_test",
        "local" : True
    }
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

# Start BrowserStack local binary
start_local()

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_caps
)

# Test case for the BrowserStack sample Android app. 
# If you have uploaded your app, update the test case here. 
test_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, "com.example.android.basicnetworking:id/test_action"))
)
test_button.click()
WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.TextView"))
)
test_element = None
search_results = driver.find_elements_by_class_name("android.widget.TextView")
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

stop_local()
