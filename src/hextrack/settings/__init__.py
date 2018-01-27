from hextrack.settings import common

from .main_settings import *
from .environment import *
from .components import *

common.merge_settings(globals(), ENVIRONMENT_SETTINGS)
for component in COMPONENT_SETTINGS:
    common.merge_settings(globals(), component)
