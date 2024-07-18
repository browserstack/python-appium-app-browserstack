import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.set_capability('sessionName', 'BStack Local Test')

# The webdriver management will be handled by the browserstack-sdk
# so this will be overridden and tests will run browserstack -
# without any changes to the test files!
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options)

try:
    driver.get('http://bs-local.com:45454')
    page_title = driver.title
    # check if local connected successfully
    if 'BrowserStack Local' in page_title:
        # mark test as passed if Local website is accessible
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Local Test ran successfully"}}')
    else:
        # mark test as failed if Local website is not accessible
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Local test setup failed"}}')
except Exception as err:
    message = 'Exception: ' + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')

# Stop the driver
driver.quit()
