import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def merge_installed_apps(base, settings):
    if not base.get('INSTALLED_APPS'):
        base['INSTALLED_APPS'] = []
    apps = settings.get('INSTALLED_APPS', [])
    for app in apps:
        if app not in base['INSTALLED_APPS']:
            base['INSTALLED_APPS'].append(app)


MANUAL_MERGE = {
    'INSTALLED_APPS': merge_installed_apps
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
