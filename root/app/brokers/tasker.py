from celery import Celery
from os import system


app = Celery('tasker',
            broker="pyamqp://guest@cyberhead-rmq//")



@app.task
def start():
    print('brokers started')


app.conf.beat_schedule = {
    "start": {
        "task": "tasker.start",
        "schedule": 10
    }
}
