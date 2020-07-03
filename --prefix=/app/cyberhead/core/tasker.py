from celery import Celery
from os import system


app = Celery('tasker',
            broker="pyamqp://guest@cyberhead-rmq//")


@app.task
def see_you():
    system('python3 /app/cyberhead/strategies/strategies.py')


app.conf.beat_schedule = {
    "see-you": {
        "task": "tasker.see_you",
        "schedule": 5.0
    }
}
