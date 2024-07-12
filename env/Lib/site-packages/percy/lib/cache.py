import time


class Cache:
    CACHE = {}
    CACHE_TIMEOUT = 5 * 60  # 5 * 60 seconds
    TIMEOUT_KEY = 'last_access_time'

    # Caching Keys
    session_details = 'session_details'
    system_bars = 'system_bars'
    window_size = 'window_size'
    viewport = 'viewport'
    session_capabilities = 'session_capabilities'
    capabilities = 'capabilities'
    command_executor_url = 'command_executor_url'

    @classmethod
    def set_cache(cls, session_id, property, value):
        if not isinstance(session_id, str):
            raise TypeError('Argument session_id should be string')
        if not isinstance(property, str):
            raise TypeError('Argument property should be string')
        session = cls.CACHE.get(session_id, {})
        session[cls.TIMEOUT_KEY] = time.time()
        session[property] = value
        cls.CACHE[session_id] = session

    @classmethod
    def get_cache(cls, session_id, property):
        cls.cleanup_cache()
        if not isinstance(session_id, str):
            raise TypeError('Argument session_id should be string')
        if not isinstance(property, str):
            raise TypeError('Argument property should be string')
        session = cls.CACHE.get(session_id, {})
        return session.get(property, None)

    @classmethod
    def cleanup_cache(cls):
        now = time.time()
        session_ids = []
        for session_id, session in cls.CACHE.items():
            timestamp = session[cls.TIMEOUT_KEY]
            if now - timestamp >= cls.CACHE_TIMEOUT:
                session_ids.append(session_id)
        list(map(cls.CACHE.pop, session_ids))
