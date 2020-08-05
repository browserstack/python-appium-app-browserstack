from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browserstack.local import Local
import time
import os, json

config_file_path = os.path.join(os.path.dirname(__file__), "config.json")
print("Config file path: %s" % (config_file_path))
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['username']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['access_key']

def start_local():
    global bs_local
    bs_local = Local()
    bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY, "forcelocal": "true" }
    bs_local.start(**bs_local_args)

def stop_local():
    global bs_local
    bs_local.stop()

def existence_lambda(s):
    result = s.find_element_by_accessibility_id("ResultBrowserStackLocal").get_attribute("value")
    return result and len(result) > 0

def test():
    """
     Test for BrowserStack's sample local iOS app.
     Note: If you have uploaded your app to BrowserStack update the test here.
    """

    start_local()

    desired_capabilities = CONFIG['capabilities']

    driver = webdriver.Remote(
    desired_capabilities = desired_capabilities,
    command_executor = "http://%s:%s@hub-cloud.browserstack.com/wd/hub" % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
    )

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


if __name__ == "__main__":
    test()
