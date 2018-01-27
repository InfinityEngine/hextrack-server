import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def __merge_lists(base, settings, name):
    if not base.get(name):
        base[name] = []
    items = settings.get(name, [])
    for item in items:
        if item not in base[name]:
            base[name].append(item)


def merge_installed_apps(base, settings):
    __merge_lists(base, settings, 'INSTALLED_APPS')


def merge_hexdi_modules_list(base, settings):
    __merge_lists(base, settings, 'HEXDI_MODULES_LIST')


MANUAL_MERGE = {
    'INSTALLED_APPS': merge_installed_apps,
    'HEXDI_MODULES_LIST': merge_hexdi_modules_list
}


def module_to_dict(mdl):
    return mdl.__dict__


def merge_settings(base, settings):
    for item in settings:
        if item not in MANUAL_MERGE:
            base[item] = settings[item]
    for manual in MANUAL_MERGE:
        if manual in settings:
            MANUAL_MERGE[manual](base, settings)
