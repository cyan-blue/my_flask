# -*- coding: utf-8 -*-
from celery import Celery
from app import create_app

def create_celery_app(app=None):

    app = app or create_app('celery')
    print app.config['CELERY_BROKER_URL']
    celery = Celery(__name__, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
