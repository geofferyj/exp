import yaml
from shutil import rmtree, copytree
from os import mkdir, path
from subprocess import Popen


def read_compose(file):
    with open(file) as compose:
        structure = yaml.load(compose, Loader=yaml.FullLoader)
        return structure


def transfer_modules(modules):
    if path.exists('./modules'):
        rmtree('./modules')
    mkdir('./modules')
    for module in modules:
        copytree('/home/sebu/exp/' + module, './modules/' + module)
        print('COPIED: ./' + module, './modules/' + module)


def build():
    Popen("/home/sebu/exp/setup.py", shell=False)


file = r'/home/sebu/exp/cyberhead-compose.yml'
structure = read_compose(file)
transfer_modules(structure['modules'])
