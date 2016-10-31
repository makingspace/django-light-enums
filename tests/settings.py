import django

__doc__ = """Minimal django settings to run manage.py test command"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': __name__,
    }
}

BROKER_BACKEND = 'memory'

ROOT_URLCONF = 'tests.urls'

MIDDLEWARE_CLASSES = ()

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_light_enums',
    'tests',
)

USE_TZ = True
SECRET_KEY = "django_tests_secret_key"
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = ()

if django.VERSION < (1, 6):
    TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'
else:
    TEST_RUNNER = 'django.test.runner.DiscoverRunner'
