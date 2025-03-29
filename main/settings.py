
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os
os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(BASE_DIR, 'certs', 'sberbank.pem')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5(xcywjc650=r0d+fobtqsyq1pq4si_jnp(lya948f84n!0fri'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "app",
    "grpc",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# settings.py
LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'


GIGACHAT_API_URL = "https://ngw.devices.sberbank.ru:9443/api/v1/chat/completions"
GIGACHAT_API_KEY = "eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.CG7eINdXOT-Cw9PrxQi8g-JV5rLp6L3EMohjUhIK69_LzfNntJyVF40sKJgZ44V7K5DyDvL3c_ovXrMBkqrn5KnN15Fr_6mIxtqzZSrWtaPiCWhx2OxpKgP4SBjnwD4aHcgmCueatGXVR96uvaQiAGGvZ0M9ncu_Gx77uKLB_G82AFki0oeT_Ui4mhZD_Cj0W2u99-2pr1UIzy5IvUJMtEkPey18z8tJCddT85VphTh0fac67sivgxlmI3O-ByvY0AxNrkWX17Eutc2XYDhdvnIUTw2KjGaQz0Cpcg8tlxwHP7oGqxq7Jbb-fkUnjU9hyqAgN_wq_bYhZ7CGk0tc1Q.g97rjCilMiFeFwAFV4L0fg.UeHtsTauzA2hgiIKXBRCF5o1tB3KhO9wiBQERNsjHOllMqr1jUmATTIdj6xuABtpZIMxVGMA1zKo0U5OqTeB-zyVpKbjAoJ8vZOiT8CvYx4wAgDBIF0v5vCG4QoE1kQ_glcrtU2o6EFmL6PJlhqtGbKzxaPfN-7MxL580oB9U672kCQOvYGub-2JVbKvARxdXCdZov7Z-chifZs7V1YjzGY1CgsCvF42bBCsdF-FV3VGFF6eXVUWw-Flrx7SxzQZ_1lKynxe-02Ql4b0FiwpfUsY37oBZrPumuUL2RM-T80LhJpQGyS72L1ZYMRi2pS7Sq4fYg8ox_Tgeh9dX_nZwaq50di6wm8o0G0-ZNq_qT6idWcNxASTSNGMCjjivzTR77ChZczDJl8KEW0avlMaS9K7LTZis3jmKEEI5WKTPbPUruBX_pYXsw4Pq8voIDpiCXeoJa1VGKELew2FlGa-GM8_Hx0RnQcn9UWlhDQkWr0Evkpsh8HXpbw8fCfNox1J_ERF2_fH6wqwOiaYzZMUatwISsU2SFkWyXAn4g6mcApMMQl4l2EDeB8wO9h0O4l2PgQ7qSOXUNaSfWEGR4aLNyvfcimFhO89cWG52RLSzGgLpOSGSN2LLczs5d0XKVVtkpAy8l85C6vZdooVxkdvYfyHB9TW4QYjQW-wPFtDcvWSG7Gmqtaaw_iExGb0oJT4xOEYHKlfls5nLtyaioILaSgaiP5lyzUyaJT_iMx8NrU.4u8gV78ygOxPH7dInwT-bs9l5A_fhKZ4TE5FGBNL2eU"
USER_SECRET="2640ff4f-8595-4179-97a8-7d314d5903f9"
USER_ID="dc9f6626-a651-4791-be4a-7eb1d1fb120c"

# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
