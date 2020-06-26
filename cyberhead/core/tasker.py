from celery import Celery
from os import system


app = Celery('tasker',
            broker="pyamqp://guest@cyberhead-rmq//")


@app.task
def see_you():
    '''aca vamos a llamar a yarn start, por medio de web-gui.py'''
    '''ojo que celery no esta imprimendo ese print de aca abajo, hay un error en el medio'''
    print("See you in ten seconds!")
    system(python3 /app/cyberhead/web-gui/web-gui.py)


app.conf.beat_schedule = {
    "see-you": {
        "task": "periodic.see_you",
        "schedule": 5000.0
    }
}

