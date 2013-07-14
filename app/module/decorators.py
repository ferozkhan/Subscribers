# -*- encoding: utf-8 -*-

import redis
import simplejson


pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
_redis = redis.Redis(connection_pool=pool)


def cacher(argument):
    def wrap(func):
        def wrapped(*args, **kwargs):
            data = _redis.get(argument)
            if data is None:
                out = func(*args, **kwargs)
                _redis.set(argument, simplejson.dumps(out))
                return out
            return simplejson.loads(data)
        return wrapped
    return wrap


def sync_cache(argument):
    def wrap(func):
        def wrapped(*args, **kwargs):
            _id = args[1]
            _data_list = simplejson.loads(_redis.get(argument))
            for index, row in enumerate(_data_list):
                if row['_id']['$oid'] == _id:
                    del _data_list[index]
                    break
            _redis.set(argument, simplejson.dumps(_data_list))
            func.delay(*args, **kwargs)
        return wrapped
    return wrap