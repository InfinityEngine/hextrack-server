import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def module_to_dict(mdl):
    return mdl.__dict__


def merge_settings(base, settings):
    for item in settings:
        base[item] = settings[item]
