"""
    Project Name
    
    Author  : Name Surname <your_email@example.com>
    Created : 11 Jul 2015
    
    Project settings
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@mi_qqz4u(ihc!s)y!w+94oisy3o(e0*tfyzr0=i#yhodo^%9*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
# cms
    'cms',
    'treebeard',
    'menus',
    'sekizai',
    'djangocms_admin_style',
# cms plugin commons
    'aldryn_apphooks_config',
    'aldryn_boilerplates',
    'djangocms_text_ckeditor',
    'easy_thumbnails',
    'filer',
    'parler',
    'sortedm2m',
# news and blog
    'aldryn_categories',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_reversion',
    'reversion',
    'taggit',
# events
    'aldryn_common',
    'aldryn_events',
    'appconf',
    'bootstrap3',
    'django_tablib',
    'extended_choices',
    'standard_form',
# django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
# django default middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # for i18n
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
# cms middleware
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'project_name.urls'

SITE_ID = 1

WSGI_APPLICATION = 'project_name.wsgi.application'


# template configuration

TEMPLATE_CONTEXT_PROCESSORS = [
# cms context processors
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
# aldryn events
    'aldryn_boilerplates.context_processors.boilerplate',
]

TEMPLATE_DIRS = [
# cms
    os.path.join(BASE_DIR, "templates"),
]

TEMPLATE_LOADERS = [
# aldryn events
    'django.template.loaders.filesystem.Loader',
    'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
    'django.template.loaders.app_directories.Loader',    
]

CMS_TEMPLATES = (
    ('home.html', 'Home page'),
    ('page_standard.html', 'Page (Standard)'),
)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
]

TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"


# Uploaded files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/ref/settings/#media-root
# https://docs.djangoproject.com/en/1.7/ref/settings/#media-url

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# django filer
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)

# Aldryn bolierplates (dependency for Aldryn Events)
# https://docs.djangoproject.com/en/1.7/ref/settings/#staticfiles-finders

ALDRYN_BOILERPLATE_NAME = 'bootstrap3'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
