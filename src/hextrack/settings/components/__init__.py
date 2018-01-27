import os
import importlib

from hextrack.settings import common

COMPONENT_NAMES = os.environ.get('COMPONENTS', 'core')
COMPONENTS = COMPONENT_NAMES.split(',')
COMPONENT_SETTINGS = []

try:
    for component in COMPONENTS:
        component_module = importlib.import_module('hextrack.settings.components.{}'.format(component),
                                                   package=__name__)
        component_settings = common.module_to_dict(component_module)
        COMPONENT_SETTINGS.append(component_settings)
except ImportError:
    raise Exception("Can't import {} component.".format(component))
