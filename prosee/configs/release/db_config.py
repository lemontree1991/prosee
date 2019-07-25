# -*- coding: UTF-8 -*-

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'AlgDisDB',
        'USER':'AlgDisDB',
        'PASSWORD':'AlgDisDB',
        'HOST':'localhost',
        'PORT':'3306',
        'OPTIONS': {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}