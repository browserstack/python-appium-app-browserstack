from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browserstack.local import Local
import os

# Initialize the remote Webdriver using BrowserStack remote URL
driver = webdriver.Remote("http://hub.browserstack.com/wd/hub")

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
