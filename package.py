# -*- coding: utf-8 -*-
name = 'shotgun_api3'

version = '3.0.41'

description = 'A Python-based API for accessing Shotgun and integrating with other tools'

help = 'https://github.com/shotgunsoftware/python-api/wiki'

authors = ['Shotgun Software']

requires = [
    'python-2.4+'
]

def commands():
    env.PYTHONPATH.prepend("{root}")
