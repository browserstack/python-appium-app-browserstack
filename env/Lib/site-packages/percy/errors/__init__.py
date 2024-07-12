class BaseException(Exception):
    pass

class UnsupportedDevice(BaseException):
    pass

class UnknownProvider(BaseException):
    pass

class PlatformNotSupported(BaseException):
    pass

class DriverNotSupported(BaseException):
    pass

class CLIException(Exception):
    pass
