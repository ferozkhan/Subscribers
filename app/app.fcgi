#!/usr/bin/python

import sys
import application
from flup.server.fcgi import WSGIServer

PYTHON_SITE_PACKAGES = "<your_local_path>/lib/python2.7/site-packages"
sys.path.insert(0, PYTHON_SITE_PACKAGES)


class ApplicaitonStarter(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        return self.app(environ, start_response)


app = ApplicaitonStarter(application)


if __name__ == "__main__":
    WSGIServer(app).run()
