from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_cap = {
    # Set your access credentials
    "browserstack.user" : "YOUR_USERNAME",
    "browserstack.key" : "YOUR_ACCESS_KEY",

    # Set URL of the application under test
    "app" : "bs://<app-id>",

    # Specify device and os_version for testing
    "device" : "iPhone 11 Pro",
    "os_version" : "13",
    
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "browserstack-build-1",
    "name" : "first_test"
}

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap
)

# Test case for the BrowserStack sample Android app. 
# If you have uploaded your app, update the test case here. 
text_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Button"))
)
text_button.click()
text_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Input"))
)
text_input.send_keys("hello@browserstack.com"+"\n")
time.sleep(5)
text_output = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Output"))
)
if text_output!=None and text_output.text=="hello@browserstack.com":
	assert True
else:
	assert False

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()