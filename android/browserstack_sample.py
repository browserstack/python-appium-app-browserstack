from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_cap = {
    # Set URL of the application under test
    "app" : "bs://<app-id>",

    # Specify device and os_version for testing
    "deviceName": "Google Pixel 3",
    "platformName": "android",
    "platformVersion": "9.0",

    # Set other BrowserStack capabilities
    "bstack:options": {
        "userName" : "YOUR_USERNAME",
        "accessKey" : "YOUR_ACCESS_KEY",
        "projectName" : "First Python project",
        "buildName" : "browserstack-build-1",
        "sessionName" : "first_test"
    }
}

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=desired_cap
)

# Test case for the BrowserStack sample Android app.
# If you have uploaded your app, update the test case here.
search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
)
search_element.click()
search_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
)
search_input.send_keys("BrowserStack")
time.sleep(5)
search_results = driver.find_elements_by_class_name("android.widget.TextView")
assert (len(search_results) > 0)

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
