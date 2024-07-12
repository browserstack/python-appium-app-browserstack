class PercyOptions:
    IGNORE_ERRORS = 'ignoreErrors'
    ENABLED = 'enabled'
    PERCY_OPTIONS = ['percy:options', 'percyOptions']

    def __init__(self, capabilities):
        self._capabilities = capabilities
        self.percy_options = self._parse_percy_options() or {}

    def _parse_percy_options(self):
        options = list(map(self._capabilities.get, self.PERCY_OPTIONS))
        options = (options[0] or options[1]) if any(options) else {}
        if options: return options
        if options is not None and self.IGNORE_ERRORS not in options:
            options[self.IGNORE_ERRORS] = self._capabilities.get(f'percy.{self.IGNORE_ERRORS}', True)
        if options is not None and self.ENABLED not in options:
            options[self.ENABLED] = self._capabilities.get(f'percy.{self.ENABLED}', True)
        return options

    @property
    def ignore_errors(self):
        return self.percy_options.get(self.IGNORE_ERRORS, True)

    @property
    def enabled(self):
        return self.percy_options.get(self.ENABLED, True)
