
from __future__ import absolute_import
from celery import Celery

celery = Celery('subscribers',
                broker='amqp://',
                backend='amqp://',
                include=['module.subscriber'])

celery.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    celery.start()