from sys import argv
from os import system
from cyberhead.core.builder import build


def update():
    '''reinstall outside the container'''
    system('pipx install . --force')


def enter():
    '''open a terminal into the container'''
    system('docker-compose exec cyberhead bash')


def dev():
    '''start in developer mode'''
    update()
    build(r'/app/cyberhead-compose.yml')
    system('docker-compose exec cyberhead pip3 install .')


def deploy():
    '''deploy to the final user'''
    dev()


def stop():
    print('tasker processes stopped')


def cli():
    cmd = argv[1]

    if cmd == 'update':
        update()

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
