import os
from percy import percy_screenshot
class PercySDK:
  def screenshot(driver, name, **kwargs):
    percy_screenshot(driver, name, **kwargs)
