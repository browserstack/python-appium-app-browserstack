import json
import os
from abc import ABC, abstractmethod
from percy.common import log


_DEVICE_INFO_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'configs', 'devices.json')
with open(_DEVICE_INFO_FILE_PATH, 'r', encoding='utf-8') as fp:
    _DEVICE_INFO = json.load(fp)

class Metadata(ABC):
    def __init__(self, driver):
        self.driver = driver
        self._device_name = None
        self._os_version = None
        self.device_info = {}

    @property
    def capabilities(self):
        return self.driver.capabilities

    @property
    def session_id(self):
        return self.driver.session_id

    @property
    def os_name(self):
        return self.capabilities.get('platformName')

    @property
    def os_version(self):
        os_version = self.capabilities.get('os_version') or self.capabilities.get('platformVersion', '')
        os_version = self._os_version or os_version
        try:
            return str(int(float(os_version)))
        except Exception:
            return ''

    @property
    def remote_url(self):
        return self.driver.command_executor._url

    def get_orientation(self, **kwargs):
        orientation = kwargs.get('orientation', self.capabilities.get('orientation', 'PORTRAIT'))
        if orientation.lower() == 'auto':
            orientation = self.orientation
        return orientation.upper()

    @property
    def orientation(self):
        return self.driver.orientation.lower()

    @property
    @abstractmethod
    def device_screen_size(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def device_name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def status_bar(self):
        raise NotImplementedError

    @property
    def status_bar_height(self):
        return self.status_bar['height']

    @property
    @abstractmethod
    def navigation_bar(self):
        raise NotImplementedError

    @property
    def navigation_bar_height(self):
        return self.navigation_bar['height']

    @property
    @abstractmethod
    def viewport(self):
        raise NotImplementedError

    def execute_script(self, command):
        return self.driver.execute_script(command)

    def value_from_devices_info(self, key, device_name, os_version=None):
        device_info = self.get_device_info(device_name)
        if os_version:
            device_info = device_info.get(os_version, {})
        return int(device_info.get(key, 0))

    def get_device_info(self, device_name):
        if self.device_info:
            return self.device_info
        self.device_info = _DEVICE_INFO.get(device_name.lower(), {})
        if not self.device_info: log(f'{device_name.lower()} does not exist in config.')
        return self.device_info
