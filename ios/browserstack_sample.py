from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the remote Webdriver using BrowserStack remote URL
driver = webdriver.Remote("http://hub.browserstack.com/wd/hub")

# Test case for the BrowserStack sample iOS app.
# If you have uploaded your app, update the test case here. 
text_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Button"))
)
text_button.click()
text_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
)
text_input.send_keys("hello@browserstack.com"+"\n")
time.sleep(5)
text_output = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Output"))
)
if text_output!=None and text_output.text=="hello@browserstack.com":
	assert True
else:
	assert False

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
