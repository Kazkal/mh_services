from base import *
import dj_database_url

DEBUG = False

# Load the ClearDB connection details from the environment variable
#fix data integrity problems with STRICT
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL'),
    'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
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