from threading import Timer
from termcolor import colored

from builder import read_compose


RUNNING = colored('RUNNING', 'green')
FAILED = colored('FAILED', 'red')


def call_modules():
    modules = read_compose('/app/cyberhead-compose.yml')
    for module in modules['modules']:
        print(module)
        exec('from cyberhead.{} import start'.format(module), globals())
        module_answer, callback_timing = start()
        Timer(callback_timing, call_modules, []).start()

call_modules()
