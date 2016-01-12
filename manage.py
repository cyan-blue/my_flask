#!/usr/bin/env python
import os
from flask import Flask, current_app
from app import create_app
from flask.ext.script import Manager, Shell


if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]



print os.getenv('FLASK_CONFIG') or 'default'
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context))
@manager.command
def list_routes():
    """List all routes for the application"""
    import urllib
    from flask import current_app, url_for
    app = current_app
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        if rule.endpoint in ("blog.admin_delete_post",
        					 "blog.admin_edit_post",
        					 "blog.view_post",
        					 "blog.api_get_page",
        					 "blog.api_get_post",
        					 "blog.show_page",
        					 "blog.view_post_only_id"):
        	continue
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote(
            "{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line

@manager.command
def deploy():
    """Run deployment tasks."""
    pass


if __name__ == '__main__':
    manager.run()

