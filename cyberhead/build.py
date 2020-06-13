import yaml
from shutil import rmtree, copytree
from os import path
from subprocess import Popen


def read_compose(file):
    with open(file) as compose:
        structure = yaml.load(compose, Loader=yaml.FullLoader)
        return structure


def transfer_modules(modules):
    for module in modules:
        if path.exists('./' + module):
            rmtree('./' + module)
        copytree(modules[module]['dir'], './' + module)
        print('COPIED: ./' + module, './' + module)


def build(file):
    structure = read_compose(file)
    transfer_modules(structure['modules'])
    Popen("/home/sebu/exp/setup.py", shell=False)


build(r'/home/sebu/exp/cyberhead-compose.yml')
