import os
from os import environ
from pathlib import Path

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Secret key for the application
SECRET_KEY = 'wooooof'

# Debug mode (set to False in production)
DEBUG = False

# Allowed hosts
ALLOWED_HOSTS = []

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'GwRyMOBac7troWR',
        'HOST': 'romarin-sql.internal',
        'PORT': '5432',
    }
}

# Postgres cluster romarin-sql created
#   Username:    postgres
#   Password:    GwRyMOBac7troWR
#   Hostname:    romarin-sql.internal
#   Flycast:     fdaa:9:51d5:0:1::2
#   Proxy port:  5432
#   Postgres port:  5433
#   Connection string: postgres://postgres:GwRyMOBac7troWR@romarin-sql.flycast:5432

# Default session configuration
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1,
    participation_fee=0
)

# Define session configurations
SESSION_CONFIGS = [
    dict(
        name='romarin',
        display_name='Romarin',
        num_demo_participants=2,  # Change to an appropriate number of participants for demo sessions
        app_sequence=[
            'introduction',
            'prisoner',
            'end'
        ]
    ),
]

# Language code for the application
LANGUAGE_CODE = 'en'

# Currency code for real-world currency
REAL_WORLD_CURRENCY_CODE = 'EUR'

# Use points in the application
USE_POINTS = True

# HTML content for the demo page introduction
DEMO_PAGE_INTRO_HTML = ''

# Fields to be added to each participant
PARTICIPANT_FIELDS = []

# Fields to be added to each session
SESSION_FIELDS = []

# Configuration for rooms (if any)
ROOMS = []

# Admin username and password (admin password should be set in an environment variable for security)
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'GarciaFaria73!'

# Installed applications
INSTALLED_APPS = [
    'otree',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'introduction', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'wsgi.application'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '_static')

# oTree settings
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [
    dict(
        name='romarin',
        display_name='Romarin',
        num_demo_participants=2,  # Set an appropriate number of participants
        app_sequence=[
            'introduction',
            'prisoner',
            'public_goods',
            'market_entry',
            'questions',
            'end'
        ]
    ),
]


### OLD CODE ###

# import os
# from pathlib import Path

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')
# ADMIN_PASSWORD = os.environ.get('OTREE_ADMIN_PASSWORD')

# DEBUG = False

# ALLOWED_HOSTS = ['*']

# LANGUAGE_CODE = 'en-us'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# INSTALLED_APPS = [
#     'otree',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'introduction',
#     'prisoners_dilemma_1',
#     'public_goods_1',
#     'market_entry_1',
#     'prisoners_dilemma_2',
#     'public_goods_2',
#     'market_entry_2',
#     'post_game_questions',
#     'end',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',  # Keep CSRF middleware enabled
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'yourapp.middlewares.DisableCSRFForSpecificViewsMiddleware',  # Add custom middleware
# ]

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'introduction', 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     #os.path.join(BASE_DIR, 'static'),
# ]

# SESSION_CONFIG_DEFAULTS = {
#     'real_world_currency_per_point': 1.00,
#     'participation_fee': 0.00,
#     'doc': "",
# }

# SESSION_CONFIGS = [
#     {
#         'name': 'otree_experimental_econ',
#         'display_name': "Experimental Economics",
#         'num_demo_participants': 4,
#         'app_sequence': [
#             'introduction',
#             'prisoners_dilemma_1',
#             'public_goods_1',
#             'market_entry_1',
#             'prisoners_dilemma_2',
#             'public_goods_2',
#             'market_entry_2',
#             'post_game_questions',
#             'end'
#         ],
#     },
# ]

# INSTALLED_OTREE_APPS = [
#     'introduction',
#     'prisoners_dilemma_1',
#     'public_goods_1',
#     'market_entry_1',
#     'prisoners_dilemma_2',
#     'public_goods_2',
#     'market_entry_2',
#     'post_game_questions',
#     'end',
# ]

# CSRF_TRUSTED_ORIGINS = ['https://romarin.fly.dev/']
# CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = False