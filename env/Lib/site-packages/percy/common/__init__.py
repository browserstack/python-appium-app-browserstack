import os


PERCY_LOGLEVEL = os.environ.get('PERCY_LOGLEVEL')
PERCY_DEBUG = PERCY_LOGLEVEL == 'debug'
LABEL = '[\u001b[35m' + ('percy:python' if PERCY_DEBUG else 'percy') + '\u001b[39m]'

def log(message, on_debug=None):
    if isinstance(on_debug, type(None)) or (isinstance(on_debug, bool) and PERCY_DEBUG):
        print(f'{LABEL} {message}')
