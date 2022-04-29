from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
desired_caps = dict(
 platformName='Android',
 platformVersion='10',
 automationName='uiautomator2',
 deviceName='Android Emulator',
 app=PATH('../../../apps/selendroid-test-app.apk')
)
self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='item')
el.click()
