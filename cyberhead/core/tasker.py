from celery import Celery
from os import system


app = Celery('tasker',
            broker="pyamqp://guest@cyberhead-rmq//")


@app.task
def see_you():
    print('Sending task')
    system('python3 /app/cyberhead/strategies/stratmanager.py')
    print('Task send')


app.conf.beat_schedule = {
    "see-you": {
        "task": "tasker.see_you",
        "schedule": 0
    }
}


