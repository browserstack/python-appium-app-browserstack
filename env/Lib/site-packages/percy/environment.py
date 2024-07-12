import platform

from appium.version import version as APPIUM_VERSION
from percy.version import __version__ as SDK_VERSION

class Environment:
    percy_build_id = None
    percy_build_url = None
    session_type = None

    @staticmethod
    def _get_client_info(flag=False):
        if flag:
            return 'percy-appium-app-python/' + SDK_VERSION
        return 'percy-appium-app/' + SDK_VERSION

    @staticmethod
    def _get_env_info():
        return ['appium/' + APPIUM_VERSION, 'python/' + platform.python_version()]
