from percy.lib.cache import Cache

class DriverMetaData:
    def __init__(self, driver):
        self.driver = driver

    @property
    def session_id(self):
        return self.driver.session_id

    @property
    def command_executor_url(self):
        url = Cache.get_cache(self.session_id, Cache.command_executor_url)
        if url is None:
            url = self.driver.command_executor._url # pylint: disable=W0212
            Cache.set_cache(self.session_id, Cache.command_executor_url, url)
            return url
        return url

    @property
    def capabilities(self):
        caps = Cache.get_cache(self.session_id, Cache.capabilities)
        if caps is None:
            caps = dict(self.driver.capabilities)
            Cache.set_cache(self.session_id, Cache.capabilities, caps)
            return caps
        return caps

    @property
    def session_capabilities(self):
        session_caps = Cache.get_cache(self.session_id, Cache.session_capabilities)
        if session_caps is None:
            session_caps = dict(self.driver.desired_capabilities)
            Cache.set_cache(self.session_id, Cache.session_capabilities, session_caps)
            return session_caps
        return session_caps
