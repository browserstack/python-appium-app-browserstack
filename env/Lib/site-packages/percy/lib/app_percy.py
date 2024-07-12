from appium.webdriver.webdriver import WebDriver
from percy.errors import DriverNotSupported
from percy.lib.percy_options import PercyOptions
from percy.providers.provider_resolver import ProviderResolver
from percy.metadata import MetadataResolver


class AppPercy:
    def __init__(self, driver):
        if not isinstance(driver, WebDriver):
            raise DriverNotSupported
        self.driver = driver
        self.metadata = MetadataResolver.resolve(self.driver)
        self.provider = ProviderResolver.resolve(self.driver)
        self.percy_options = PercyOptions(self.metadata.capabilities)

    def screenshot(self, name: str, **kwargs):
        if not self.percy_options.enabled:
            return None
        if not isinstance(name, str):
            raise TypeError('Argument name should be a string')
        device_name = kwargs.get('device_name')
        if device_name and not isinstance(device_name, str):
            raise TypeError('Argument device_name should be a string')
        fullscreen = kwargs.get('full_screen')
        if fullscreen and not isinstance(fullscreen, bool):
            raise TypeError('Argument fullscreen should be a boolean')
        status_bar_height = kwargs.get('status_bar_height')
        if status_bar_height and not isinstance(status_bar_height, int):
            raise TypeError('Argument status_bar_height should be a integer')
        nav_bar_height = kwargs.get('nav_bar_height')
        if nav_bar_height and not isinstance(nav_bar_height, int):
            raise TypeError('Argument nav_bar_height should be a integer')
        orientation = kwargs.get('orientation')
        if orientation and not isinstance(orientation, str):
            raise TypeError('Argument orientation should be a string and portrait/landscape')
        sync = kwargs.get('sync')
        if sync and not isinstance(sync, bool):
            raise TypeError('Argument sync should be a boolean')
        test_case = kwargs.get('test_case')
        if test_case and not isinstance(test_case, str):
            raise TypeError('Argument test_case should be a string')
        th_test_case_execution_id = kwargs.get('th_test_case_execution_id')
        if th_test_case_execution_id and not isinstance(th_test_case_execution_id, str):
            raise TypeError('Argument th_test_case_execution_id should be a string')
        return self.provider.screenshot(name, **kwargs)
