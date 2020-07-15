from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browserstack.local import Local
import time
import os, json

config_file_path = os.path.join(os.path.dirname(__file__), "config.json")
print("Config file = %s" % (config_file_path))
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['username']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['access_key']

bs_local = None

def start_local():
    global bs_local
    bs_local = Local()
    bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY, "forcelocal": "true" }
    bs_local.start(**bs_local_args)

def stop_local():
    global bs_local
    bs_local.stop()

def test():
    """
     Test for BrowserStack's sample local Android app.
     Note: If you have uploaded your app to BrowserStack update the test here.
    """

    start_local()

    desired_capabilities = CONFIG['capabilities']

    driver = webdriver.Remote(
    desired_capabilities = desired_capabilities,
    command_executor = "http://%s:%s@hub-cloud.browserstack.com/wd/hub" % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
    )

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

    driver.quit()

    stop_local()


if __name__ == "__main__":
    test()