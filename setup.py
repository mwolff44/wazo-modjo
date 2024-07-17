#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml

from setuptools import find_packages
from setuptools import setup

with open('wazo/plugin.yml') as file:
    metadata = yaml.load(file)

setup(
    name=metadata['name'],
    version=metadata['version'],
    description=metadata['display_name'],
    author=metadata['author'],
    url=metadata['homepage'],

    packages=find_packages(),
    entry_points={
        'wazo_call_logd.plugins': [
            'modjo = wazo_modjo.plugin:Plugin'
        ],
    },
)
