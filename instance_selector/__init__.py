import django


__version__ = "2.1.1"

if django.VERSION < (3, 2):
    default_app_config = "%s.apps.AppConfig" % __name__
