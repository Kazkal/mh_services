from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://mh-maintenance-services.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'admin@mhservices.co.uk'


SITE_URL = 'https://mh-maintenance-services.herokuapp.com'
ALLOWED_HOSTS.append('mh-maintenance-services.herokuapp.com')

# Log DEBUG information to the console as DEBUG=false
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}