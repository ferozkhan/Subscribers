# -*- coading: utf-8 -*-

import os
import requests
import simplejson
import decorators as decor
from datetime import datetime
from app_celery import celery


MONGO_URI = 'https://api.mongolab.com/api/1/databases/%(db)s/collections/%(collection)s?apiKey=%(api_key)s'


@decor.cacher('subscribers')
def get_all_subscribres(mongo_config):
    subscribers = requests.get(MONGO_URI % mongo_config)
    return subscribers.json()


@decor.sync_cache('subscribers')
@celery.task
def delete_subscriber(mongo_config, email):
    mongo_delete_url = (MONGO_URI % mongo_config).replace('?', '/%s?' % id)
    r = requests.delete(mongo_delete_url)


@decor.sync_cache('subscribers')
@celery.task
def add_subscriber(mongo_config, email):
    data = simplejson.dumps(dict(subscribe_time=datetime.now().strftime('%Y-%m-%d %H:%M'), email=email))
    r = requests.post(MONGO_URI % mongo_config, data=data, headers = {'Content-Type': 'application/json;charset=UTF-8'})

