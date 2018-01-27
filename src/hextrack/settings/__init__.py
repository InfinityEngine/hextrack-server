from hextrack.settings import common
import importlib

from .main_settings import *
from .environment import *

COMPONENT_NAMES = os.environ.get('COMPONENTS', 'core')
COMPONENTS = COMPONENT_NAMES.split(',')

try:
    for component in COMPONENTS:
        component_module = importlib.import_module('hextrack.settings.components.{}'.format(component),
                                                   package=__name__)
        component_settings = common.module_to_dict(component_module)
        common.merge_settings(globals(), component_settings)
except ImportError:
    raise Exception("Can't import {} component.".format(component))
