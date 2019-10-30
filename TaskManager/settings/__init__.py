import os

# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
IS_PRODUCTION = os.environ.get('IS_PRODUCTION')
if IS_PRODUCTION == 'True':
    from .prod import *
else:
    from .dev import *
