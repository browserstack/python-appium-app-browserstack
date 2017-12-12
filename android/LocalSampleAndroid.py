from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browserstack.local import Local
import time

userName = "BROWSERSTACK_USERNAME"
accessKey = "BROWSERSTACK_ACCESS_KEY"

desired_caps = {
    "build": "Python Android Local",
    "device": "Samsung Galaxy S7",
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

start_local()
driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)
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
print matched_string
assert(matched_string.__contains__("The active connection is wifi"))
assert(matched_string.__contains__("Up and running"))

driver.quit()
stop_local()
