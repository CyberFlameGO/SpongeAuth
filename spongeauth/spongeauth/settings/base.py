"""
Django settings for spongeauth project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "tr2#$_hu73wp2p&jt@%u#d%xx859%32o)8f(dy1+&o!z2o=c1)"

DEBUG = False

ALLOWED_HOSTS = ["auth.spongepowered.org", "localhost", "auth", "spongeauth_auth"]

REQUIRE_EMAIL_CONFIRM = True

# Application definition

INSTALLED_APPS = [
    "core",
    "accounts",
    "twofa",
    "sso",
    "migrator",
    "api",
    "crispy_forms",
    "dal",
    "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "user_sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_rq",
]

MIDDLEWARE = [
    "core.middleware.XRealIPMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "user_sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "accounts.middleware.EnforceVerifiedEmails",
    "accounts.middleware.EnforceToSAccepted",
]

SESSION_ENGINE = "user_sessions.backends.db"

ROOT_URLCONF = "spongeauth.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "spongeauth.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "spongeauth"),
        "USER": os.getenv("DB_USER", ""),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", ""),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static-build")]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

LOGIN_REDIRECT_URL = "/"

GOOGLE_CLIENT_ID = "375961146994-9cnsdrrhs12geakfbmgiq9e3mfhqo3av.apps.googleusercontent.com"
GOOGLE_SCOPES = ["profile", "email"]

CRISPY_TEMPLATE_PACK = "bootstrap3"

AUTH_USER_MODEL = "accounts.User"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# e.g.
# SSO_ENDPOINTS = {
#     'discourse': {
#         'sync_sso_endpoint': (
#             'http://discourse.example.com/admin/users/sync_sso'),
#         'sso_secret': 'discourse-sso-secret',
#         'api_key': 'discourse-api-key',
#     },
# }
SSO_ENDPOINTS = {}

IS_TESTING = False

# The period for which an avatar change token for an organisation is valid.
# Default: 30 minutes in seconds
ACCOUNTS_AVATAR_CHANGE_MAX_AGE = 1800
ACCOUNTS_AVATAR_RESIZE_MAX_DIMENSION = 240
ACCOUNTS_AVATAR_CHANGE_GROUPS = ["dummy"]

# Redis queue settings.
RQ_QUEUES = {"default": {"HOST": "localhost", "PORT": 6379, "DB": 0, "DEFAULT_TIMEOUT": 300}}

LETTER_AVATAR_BASE = "https://forums-cdn.spongepowered.org/" "letter_avatar_proxy/v2/letter/{}/{}/240.png"
