from percy.errors import UnknownProvider
from percy.metadata.metadata_resolver import MetadataResolver
from percy.providers.app_automate import AppAutomate
from percy.providers.generic_provider import GenericProvider


class ProviderResolver:
    @staticmethod
    def resolve(driver):
        metadata = MetadataResolver.resolve(driver)
        providers = [AppAutomate, GenericProvider]
        for provider in providers:
            if provider.supports(metadata.remote_url):
                return provider(driver, metadata)
        raise UnknownProvider
