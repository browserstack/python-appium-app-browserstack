from percy.metadata.metadata import Metadata
from percy.lib.cache import Cache


class AndroidMetadata(Metadata):
    def __init__(self, driver):
        super().__init__(driver)
        self._bars = None
        self._viewport_rect = self.capabilities.get('viewportRect', None)

    @property
    def device_screen_size(self):
        width, height = self.capabilities.get('deviceScreenSize', '1x1').split('x')
        return {'width': int(width), 'height': int(height)}

    def get_system_bars(self):
        self._bars = Cache.get_cache(self.session_id, Cache.system_bars)
        if self._viewport_rect:
            try:
                self._bars = {
                    'statusBar': {'height': self._viewport_rect['top']},
                    'navigationBar': {
                        'height': self.device_screen_size['height'] - self._viewport_rect['height'] - self._viewport_rect['top']
                    }
                }
            except Exception:
                self._bars = None
        if not self._bars:
            self._bars = self.driver.get_system_bars()
            Cache.set_cache(self.session_id, Cache.system_bars, self._bars)
        return self._bars

    @property
    def status_bar(self):
        status_bar = self.get_system_bars().get('statusBar')
        if status_bar.get('height') == 1:
            response = self.value_from_devices_info('status_bar', self.device_name.upper(), self.os_version)
            return {'height': response}
        return status_bar

    @property
    def navigation_bar(self):
        navigation_bar = self.get_system_bars().get('navigationBar')
        if navigation_bar.get('height') == 1:
            response = {'height': self.value_from_devices_info('nav_bar', self.device_name.upper(), self.os_version)}
            return response
        return navigation_bar

    @property
    def viewport(self):
        return self.capabilities.get('viewportRect', {})

    @property
    def scale_factor(self):
        return 1

    @property
    def device_name(self):
        if self._device_name is None:
            desired_caps = self.capabilities.get('desired', {})
            _device_name = desired_caps.get('deviceName')
            _device = desired_caps.get('device')
            _device_name = _device_name or _device
            _device_model = self.capabilities.get('deviceModel')
            self._device_name = _device_name or _device_model
        return self._device_name
