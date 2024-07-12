from percy.common import log
from percy.lib import AppPercy, PercyOnAutomate
from percy.lib.cli_wrapper import CLIWrapper
from percy.environment import Environment

def percy_screenshot(driver, name: str, **kwargs):
    try:
        if not CLIWrapper.is_percy_enabled():
            return None

        ProviderClass = PercyOnAutomate if Environment.session_type == 'automate' else AppPercy
        app_percy = None
        app_percy = ProviderClass(driver)
        return app_percy.screenshot(name, **kwargs)
    except Exception as e:
        CLIWrapper().post_failed_event(str(e))
        log(f'Could not take screenshot "{name}"')
        if app_percy and app_percy.percy_options.ignore_errors is False:
            raise e
        log(e, on_debug=True)
        return None
