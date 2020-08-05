from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os, json

config_file_path = os.path.join(os.path.dirname(__file__), "config.json")
print("Path to the config file: %s" % (config_file_path))
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['username']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['access_key']

def test():
    """
     Test for BrowserStack sample iOS app.
     Note: If you have uploaded your app to BrowserStack update the test here.
    """

    desired_capabilities = CONFIG['capabilities']

    driver = webdriver.Remote(
    desired_capabilities = desired_capabilities,
    command_executor = "http://%s:%s@hub-cloud.browserstack.com/wd/hub" % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
    )

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

    driver.quit()


if __name__ == "__main__":
    test()
