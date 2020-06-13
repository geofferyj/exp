from setuptools import setup, find_packages
from os import environ, path


environ['CH_PATH'] = path.dirname(path.realpath(__file__))

setup(name='cyberhead',
    version='1.0',
    description='modular automated trading',
    url='cyberhead.uk',
    author='cyberhead',
    author_email='info@cyberhead.uk',
    license='MIT',
    packages=find_packages('modules'),
    zip_safe=False)

setup(name='wrapper',
    version='1.0',
    description='modular automated trading',
    url='cyberhead.uk',
    author='cyberhead',
    author_email='info@cyberhead.uk',
    license='MIT',
    packages=find_packages('modules'),
    zip_safe=False)
