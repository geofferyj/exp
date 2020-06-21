import yaml
from shutil import rmtree, copytree
from os import path, system


def read_compose(file):
    with open(file) as compose:
        structure = yaml.load(compose, Loader=yaml.FullLoader)
        return structure


def transfer_modules(modules):
    for module in modules:
        if path.exists('/app/cyberhead/' + module):
            rmtree('/app/cyberhead/' + module)
        copytree(modules[module]['dir'], '/app/cyberhead/' + module)
        print('COPIED: /app/cyberhead/' + module, '/app/cyberhead/' + module)


def build(file):
    structure = read_compose(file)
    transfer_modules(structure['modules'])
    system('python3 /app/setup.py install')
    system('pip3 install -r /app/cyberhead/requirements.txt')
