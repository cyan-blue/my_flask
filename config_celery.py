from config import BaseConfig
from kombu import Exchange, Queue

class CeleryConfig(BaseConfig):
    APP_RUNNING_MODE = "celery"

    DEBUG = True
    TESTING = False
    API_DEV_ENABLE = True
    API_ADMIN_ENABLE = True
    CELERY_ASYNC_ENABLE = True
    CELERY_BROKER_URL = 'amqp://guest@localhost//'

    CELERY_DEFAULT_QUEUE = 'default'
    CELERY_QUEUES = (
            Queue('default', routing_key='app.#'),
            Queue('mail',  routing_key='mail.#'),
            Queue('async',  routing_key='async.#'),
        )
    CELERY_DEFAULT_EXCHANGE = 'defaultexchange'
    CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
    CELERY_DEFAULT_ROUTING_KEY = 'default'
    CELERY_ROUTES = {
                        'mail.send_mail': {
                            'queue': 'mail',
                            'routing_key': 'mail.send_mail'
                        },
                        'app.remove': {
                            'queue': 'async',
                            'routing_key': 'async.test'
                        },
                    }


    @staticmethod
    def init_app(app):
        pass