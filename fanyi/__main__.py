#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import threading
from os import path

from .metadata import version
from .services import iciba, youdao
from .textui import colored, show


def print_help():
    """Print help message.
    """
    print(colored.cyan('usage: ') + path.basename(sys.argv[0]) + \
          ' [English|Chinglish|中文]')
    print('\n    ' + colored.green('v'+ version) + \
          colored.dim('  Simple command line translator, powered by Python.'))

def translator(words):
    """Call online translate services concurrently.
    """
    services = [youdao, iciba]

    lock = threading.Lock()
    # Print result from one service at a time.
    def call_show(result):
        lock.acquire()
        show(result)
        lock.release()

    def call_service(service, w=words):
        result = service.translate(w)
        call_show(result)

    for s in services:
        threading.Thread(
            target=call_service, args=(s,)).start()

def main():
    """Setuptools entry point.
    """
    if len(sys.argv) < 2:
        print_help()
    else:
        words = ' '.join(sys.argv[1:])
        translator(words)

