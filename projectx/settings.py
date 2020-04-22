"""
Django settings for projectx project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2$v%o)#av9y$+gq93i5o$tlkf_-v(930j(y!52(yd$9l9st-0('
# SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
# print(os.getenv('DJANGO_SECRET_KEY'))
# print(os.getenv('DJANGO_DB_HOST'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
assert SECRET_KEY is not None, (
    'Please provide DJANGO_SECRET_KEY '
    'environment variable with a value')
# ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = [os.getenv('DJANGO_ALLOWED_HOSTS')]
ALLOWED_HOSTS=['localhost', 'bverge.com', 'www.bverge.com', '127.0.0.1', '[::1]', 'django', 'daphne', 'ec2-13-232-117-88.ap-south-1.compute.amazonaws.com', '13.232.117.88']
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800
FILE_UPLOAD_MAX_MEMORY_SIZE = 20971520

LOGIN_REDIRECT_URL = 'profiles:index'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'seller1',
    'metadata',
    'social_django',
    'phonenumber_field',
    'widget_tweaks',

    'album',
    'profiles',
    'chat',
    'investor',
    'advisor',
    'user_seller',
    'channels',
    'staff',

    'webpack_loader',
    'rest_framework',
    'mathfilters',
    'twilio',
    'xhtml2pdf',
    'pdf2image',
    'storages',
    'paypal.standard.ipn',
    # 'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    # 'livereload.middleware.LiveReloadScript'
]

ROOT_URLCONF = 'projectx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
                'django.template.context_processors.media',
                'projectx.context_processors.all_media',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
WSGI_APPLICATION = 'projectx.wsgi.application'
ASGI_APPLICATION = 'projectx.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}



# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': '',
#             'USER': 'root',
#             'PASSWORD': '',
#             'HOST': '',
#             'PORT': '3306',
#     }
# }
# print(os.getenv('DJANGO_DB_NAME'))

# DJANGO_DB_NAME = os.getenv('DJANGO_DB_NAME')
# DJANGO_DB_USER = os.getenv('DJANGO_DB_USER')
# DJANGO_DB_PASSWORD = os.getenv('DJANGO_DB_PASSWORD')
# DJANGO_DB_HOST = os.getenv('DJANGO_DB_HOST')
# print(DJANGO_DB_HOST)
# print(SECRET_KEY)

################################# For Production ############################

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DJANGO_DB_NAME') ,
            'USER': os.getenv('DJANGO_DB_USER') ,
            'PASSWORD': os.getenv('DJANGO_DB_PASSWORD') ,
            'HOST': os.getenv('DJANGO_DB_HOST') ,
            'PORT': 3306,
    }
}

############################## For Development #####################################

# DATABASES = {
#     'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'bvergedatabase' ,
#             'USER': 'root' ,
#             'PASSWORD': 'BvergeProject' ,
#             'HOST': 'bvergedb.cu9s3dzvusve.ap-south-1.rds.amazonaws.com' ,
#             'PORT': 3306,
#     }
# }

#####################################For Prajwal#################################################

# DATABASES = {
#     'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'bvergedatabase' ,
#             'USER': 'root' ,
#             'PASSWORD': 'wellthislooksgood@17' ,
#             'HOST': '127.0.0.1' ,
#             'PORT': 3306,
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


WEBPACK_LOADER = {
    'DEFAULT': {
            'BUNDLE_DIR_NAME': 'bundles/',
            'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.dev.json'),
        }
}


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    # 'profiles.pipeline.check_email_exists',
    # 'social_core.pipeline.social_auth.associate_by_email'
    'social_core.pipeline.user.create_user',
    'profiles.pipeline.get_avatar',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',

)
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email',]
SOCIAL_AUTH_ASSOCIATE_BY_MAIL = True
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'email']
LOGIN_ERROR_URL = '/'

SOCIAL_AUTH_LOGIN_ERROR_URL="/auth_error"

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/


################################# FOr Production ###################################

SOCIAL_AUTH_GITHUB_KEY = os.getenv('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.getenv('SOCIAL_AUTH_GITHUB_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY =os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
# #
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY')
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET')

############################################ For Development  #############################################

# SOCIAL_AUTH_GITHUB_KEY = '3587cb59299b6a333b8e'
# SOCIAL_AUTH_GITHUB_SECRET = '46941b74903fa449f227c956d723e5be9956a4aa'

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='525491482451-tbhth56o4usmjf1beuca21n4jj2de515.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'uYdpgAjU5hPMwlhgarAUZZmk'

# SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '81wmsl0nipfegt'
# SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'Y4BXLqOUgLXzor2S'


#########################################################################################################

SOCIAL_AUTH_GITHUB_SCOPE = ['user:email']
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_liteprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['emailAddress', 'formatted-name', 'public-profile-url', 'picture-url']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [
    ('id', 'id'),
    ('formattedName', 'name'),
    ('emailAddress', 'email_address'),
    ('pictureUrl', 'picture_url'),
    ('publicProfileUrl', 'profile_url'),
]




SOCIAL_AUTH_TWITTER_KEY = '9TD12xahCWCDdyLzpmw61GSM9'
SOCIAL_AUTH_TWITTER_SECRET = 'mwtdcUe4uOvvJjDk2AuQ9Mq2xiHPw3740m5iGLf6hwg3B4TNSx'
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'id,name,email',}
SOCIAL_AUTH_FIELD_SELECTORS = ['email-address',]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
# EMAIL_HOST_PASSWORD = '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' # this is your API key
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# DEFAULT_FROM_EMAIL = 'prajwalbarapatre13@gmail.com' # this is the sendgrid email


######################## For Production ###############################

EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 465

############################## For Development ###############################

# EMAIL_USE_SSL = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'admin@bverge.com'
# EMAIL_HOST_PASSWORD = 'Merge@2019'
# EMAIL_PORT = 465

###################################################################################

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'admin@bverge.com'
# EMAIL_HOST_PASSWORD = 'Merge@2019'
# EMAIL_PORT = 25




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = 'static'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'gathered_static_files')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

## AWS_ACCESS_KEY_ID = 'AKIAWASZ5HF6DL46EYBO'
## AWS_SECRET_ACCESS_KEY = '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'

# AWS_ACCESS_KEY_ID = 'AKIAWASZ5HF6ABWCZE4U'
# AWS_SECRET_ACCESS_KEY = '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'


# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# # AWS_DEFAULT_ACL = None
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
#
# AWS_LOCATION = 'static'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
#

######################## For Production ###############################

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY_ID')
AWS_STORAGE_BUCKET_NAME = 'bverge'

############################## For Development ###############################

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_ACCESS_KEY_ID = 'AKIAWASZ5HF6ABWCZE4U'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'bverge'

###################################################################################

INTERNAL_IPS = [
    '127.0.0.1'
]

USE_X_FORWARDED_HOST = True

PAYPAL_RECEIVER_EMAIL = 'businessmerge-facilitator@gmail.com'

PAYPAL_TEST = True


# Sendgrid_api = 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

