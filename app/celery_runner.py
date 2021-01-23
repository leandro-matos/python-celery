from celery import Celery
import time
import datetime

celery = Celery('hello', broker='amqp://guest:guest@localhost:5672//')

@celery.task
def hello(msg):
    time.sleep(20)
    with open('file.log', 'a') as file:
        file.write(f'{msg} - {datetime.datetime.now()}\n')
        print(f'{msg} - {datetime.datetime.now()}\n')