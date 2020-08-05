from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os, json, threading


config_file_path = os.path.join(os.path.dirname(__file__), "config.json")
print("Path to the config file: %s" % (config_file_path))
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['username']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['access_key']

def test(device_index):
    """
     Test for BrowserStack sample Wikipedia Android app.
     Note: If you have uploaded your app to BrowserStack update the test here.
    """

    desired_capabilities = CONFIG['capabilities']
    desired_capabilities['device'] = CONFIG['environments'][device_index]['device']
    
    driver = webdriver.Remote(
    desired_capabilities = dict(desired_capabilities),
    command_executor = "http://%s:%s@hub-cloud.browserstack.com/wd/hub" % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
    )

    search_element = WebDriverWait(driver, 30).until (
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
    )

    search_element.click()

    search_input = WebDriverWait(driver, 30).until (
    EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
    )

    search_input.send_keys("BrowserStack")

    time.sleep(5)

    search_results = driver.find_elements_by_class_name("android.widget.TextView")

    assert(len(search_results) > 0)

    driver.quit()


if __name__ == "__main__":
    jobs = []
    for index in range(2):
        thread = threading.Thread(target=test,args=(index,))
        jobs.append(thread)
        thread.start()

    for thread in jobs:
        thread.join()

