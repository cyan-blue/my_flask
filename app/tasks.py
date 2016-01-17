# -*- coding: utf-8 -*-

from factory import create_celery_app


from flask import current_app, render_template
from flask.ext.mail import Message

from . import mail

celery = create_celery_app()


@celery.task(name="mail.send_mail")
def send_async_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['BOWHEAD_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['BOWHEAD_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    with app.app_context():
        mail.send(msg)

@celery.task(name="app.remove")
def send_manager_removed_email(*recipients):
    print 'sending manager removed email...'