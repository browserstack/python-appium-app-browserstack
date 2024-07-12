from percy.errors import PlatformNotSupported
from percy.metadata.android_metadata import AndroidMetadata
from percy.metadata.ios_metadata import IOSMetadata


class MetadataResolver:
    @staticmethod
    def resolve(driver):
        platform_name = driver.capabilities.get('platformName', '').lower()
        if platform_name == 'android':
            return AndroidMetadata(driver)
        if platform_name == 'ios':
            return IOSMetadata(driver)
        raise PlatformNotSupported
