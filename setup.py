# -*- coding: utf-8 -*-

import imp
from os import path

from setuptools import find_packages, setup

CODE_DIRECTORY = 'fanyi'
here = path.abspath(path.dirname(__file__))

metadata = imp.load_source(
    'metadata', path.join(here, CODE_DIRECTORY, 'metadata.py'))

setup(
    name=metadata.name,
    version=metadata.version,

    description=metadata.description,
    url=metadata.url,

    author=metadata.author,
    author_email=metadata.email,
    license='GPLv3',
    platforms='any',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Environment :: Console',
        'Environment :: Web Environment',

        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',

        'Topic :: Education',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Utilities',
    ],

    keywords='translation search Chinese English',
    packages=find_packages(exclude=['docs', 'tests*']),
    zip_safe=False,

    install_requires=[
        'requests',
        'xmltodict',
        'clint'
    ],

    entry_points={
        'console_scripts': [
            'fanyi = fanyi.__main__:main',
        ],
    },
)

