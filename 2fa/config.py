import os


class Configuration(object):
    DEBUG = True

    MAIL_SERVER = os.getenv('SERVER')
    MAIL_PORT = os.getenv('PORT')
    MAIL_USERNAME = os.getenv('EMAIL')
    MAIL_PASSWORD = os.getenv('PASSWORD')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/auth_user'