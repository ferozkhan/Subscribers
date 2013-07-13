# -*- coading: utf-8 -*-

import os
import httplib2
import simplejson
import urllib
from datetime import datetime

MONGO_URI = "https://api.mongolab.com/api/1/databases/%(db)s/collections/%(collection)s?apiKey=%(api_key)s"


class DataFormatUtil(object):

    def __init__(self):
        pass

    def str_to_json(self, data):
        return simplejson.loads(data)


class API(DataFormatUtil):

    def __init__(self, **kwargs):
        super(API, self).__init__()
        self.mongo_url = MONGO_URI % kwargs
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}

    def GET(self):
        pass

    def DELETE(self, _id):
        http = httplib2.Http()
        MONGO_URL_DELETE = self.mongo_url.replace('?', '/%s?' % _id)
        response, content = http.request(
            MONGO_URL_DELETE, "DELETE", headers=self.headers)

        return response['status']

    def POST(self, email):
        http = httplib2.Http()
        data = simplejson.dumps(dict(
            subscribe_time=datetime.now().strftime("%Y-%m-%d %H:%M"), email=email))
        response, content = http.request(
            self.mongo_url, "POST", data, headers=self.headers)

        return response['status']


class Subscriber(API):

    def __init__(self, **kwargs):
        super(Subscriber, self).__init__(**kwargs)

    def add_subscriber(self, email):
        status = self.POST(email)
        return status

    def delete_subscriber(self, id):
        status = self.DELETE(id)
        return status

    def subscribers(self):
        try:
            subs = self.str_to_json(urllib.urlopen(self.mongo_url).read())
            return subs
        except Exception as ex:
            raise ex

    def subscriber(self, email):
        pass

    def is_subscriber(self, email):
        pass
