#!/usr/bin/env python3
import os

from flask_rq import get_worker
from raven import Client
from raven.transport.http import HTTPTransport
from rq.contrib.sentry import register_sentry

from server import create_app

if __name__ == '__main__':
    # default to dev config
    env = os.getenv('OK_ENV', 'prod')
    app = create_app(env)
    with app.app_context():
        worker = get_worker()
        sentry_dsn = os.getenv('SENTRY_DSN')
        if sentry_dsn:
            client = Client(sentry_dsn, transport=HTTPTransport)
            # disable sentry for now (causes worker CrashLoopBackOff in kubernetes)
            # register_sentry(client, worker)
        worker.work()
