import os
import unittest
from config import config
from app import create_app, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from celery import Celery


def create_worker_for_celery(config_name=None):
    print "app config name: %s\n" % config_name
    if config_name is not None:
        if config_name in config.keys():
            pass
        else:
            print "Wrong app config name: %s. Use default instead." % config_name
            config_name = 'default'
    else:
        config_name = 'default'

    app = create_app(config_name)

    return app


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


app = create_worker_for_celery('celery')
app = make_celery(app)

if __name__ == '__main__':    
    app.run()
