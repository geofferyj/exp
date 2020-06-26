from sys import argv
from os import system#from cyberhead.core.builder import build


def update():
    '''reinstall outside the container'''
    system('pipx install . --force')


def enter():
    '''open a terminal into the container'''
    system('docker-compose exec cyberhead bash')


def build():
    '''erase modules and build'''
    update()
    system('docker-compose exec cyberhead python3 '
        '/app/cyberhead/core/builder.py')


def dev():
    '''start in developer mode'''
    system('docker-compose exec cyberhead '
            'celery -A tasker beat --loglevel=info --workdir /app/cyberhead/core')


def deploy():
    '''deploy to the final user'''
    dev()


def stop():
    print('tasker processes stopped')


def cli():
    cmd = argv[1]

    if cmd == 'update':
        update()

    if cmd == 'build':
        build()

    elif cmd == 'enter':
        enter()

    elif cmd == 'dev':
        dev()

    elif cmd == 'deploy':
        deploy()

    elif cmd == 'stop':
        stop()

    elif cmd == '--help' or cmd == '-h' or cmd == 'help':
        print('no written help yet, read the wrapper.py from core')

    else:
        print('Command not found, use --help for the commands list')
