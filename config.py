import os
_basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    APP_RUNNING_MODE = ""

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '323'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    FLATPAGES_EXTENSION = '.md'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = '18120112004@163.com'
    MAIL_PASSWORD = 'hy1314'

    BOWHEAD_MAIL_SUBJECT_PREFIX = '[Hello]'
    BOWHEAD_MAIL_SENDER = 'Lynn <18120112004@163.com>'


    MYSQL_USE_UNICODE = True
    MYSQL_CHARSET = 'utf-8'

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = os.environ.get('SECRET_KEY') or "guess what is"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    APP_RUNNING_MODE = "development"

    DEBUG = True
    TESTING = False
    API_DEV_ENABLE = True
    API_ADMIN_ENABLE = True
    CELERY_ASYNC_ENABLE = True
    CELERY_BROKER_URL = 'amqp://guest@localhost//'
    SQLALCHEMY_DATABASE_URI = 'mysql://data:data@localhost/gululu?charset=utf8&use_unicode=0'

    @staticmethod
    def init_app(app):
        pass


class TestConfig(BaseConfig):
    APP_RUNNING_MODE = "test"

    DEBUG = True
    TESTING = True
    API_DEV_ENABLE = True
    API_ADMIN_ENABLE = True
    CSRF_ENABLED = False
    CELERY_ASYNC_ENABLE = False
    SERVER_NAME = "test.bowhead.com"
    SQLALCHEMY_DATABASE_URI = 'sqlite://'  # using sqlite memory

    SERVER_NAME = "127.0.0.0:8000"
    VAULT_REOURCE_SERVER_NAME = '127.0.0.1'
    VAULT_REOURCE_SERVER_PORT = '9000'


    @staticmethod
    def init_app(app):
        pass


from config_celery import CeleryConfig

config = {
    'celery'     : CeleryConfig,
    'development': DevelopmentConfig,
    'test'       : TestConfig,
    'default'    : DevelopmentConfig
}
