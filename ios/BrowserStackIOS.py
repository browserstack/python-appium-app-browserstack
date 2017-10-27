from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

userName = "BROWSERSTACK_USERNAME"
accessKey = "BROWSERSTACK_ACCESS_KEY"

desired_caps = {
    "build": "Python iOS",
    "realMobile": True,
    "device": "iPhone 7",
    "automationName": "XCUITest",
    "app": "bs://<hashed app-id>"
}

driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub.browserstack.com/wd/hub", desired_caps)

login_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Log In"))
)
login_button.click()

email_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Email address"))
)
email_input.send_keys("hello@browserstack.com")

driver.find_element_by_accessibility_id("Next").click()
time.sleep(5)

text_elements = driver.find_elements_by_xpath("//XCUIElementTypeStaticText")
assert(len(text_elements) > 0)
elements = filter(
    lambda x: x.__contains__("not registered on WordPress.com"),
    [x.text for x in text_elements]
)
assert(len(elements) > 0)
driver.quit()
