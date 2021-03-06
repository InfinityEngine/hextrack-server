import os
import importlib
from hextrack.settings import common

ENVIRONMENT_NAME = os.environ.get('ENV', 'NOENV')

# Try to import environment settings
try:
    ENVIRONMENT = importlib.import_module('hextrack.settings.environment.{}'.format(ENVIRONMENT_NAME), package=__name__)
    ENVIRONMENT_SETTINGS = common.module_to_dict(ENVIRONMENT)
except ImportError:
    raise Exception("Can't import {} environment settings".format(ENVIRONMENT_NAME))

# You can use these environment settings in your components
