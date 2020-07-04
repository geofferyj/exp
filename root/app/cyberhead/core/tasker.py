from threading import Timer
from termcolor import colored

from builder import read_compose


RUNNING = colored('RUNNING', 'green')
FAILED = colored('FAILED', 'red')


modules = read_compose('/app/cyberhead-compose.yml')['modules']
callback_timing = 5
def import_modules():
    for module in modules:
        exec('from cyberhead import {}'.format(module), globals())


def call_modules():
    for module in modules:
        exec("""message, m_timer = {}.start()\nprint(message)""".format(module))
    Timer(callback_timing, call_modules).start()

import_modules()
call_modules()
