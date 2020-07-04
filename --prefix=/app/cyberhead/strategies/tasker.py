from celery import Celery
from os import system


app = Celery('tasker',
            broker="pyamqp://guest@cyberhead-rmq//")



@app.task
def start():
    print('strategies started')
    system('python3 /app/cyberhead/strategies/stratmanager.py')


app.conf.beat_schedule = {
    "start": {
        "task": "tasker.start",
        "schedule": 10
    }
}
