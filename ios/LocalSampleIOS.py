from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browserstack.local import Local
import os

userName = "BROWSERSTACK_USERNAME"
accessKey = "BROWSERSTACK_ACCESS_KEY"

desired_caps = {
    "build": "Python 3 iOS Local",
    "device": "iPhone 7",
    "browserstack.local": True,
    "app": "bs://<hashed app-id>"
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

start_local()
driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)

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

driver.quit()
stop_local()
