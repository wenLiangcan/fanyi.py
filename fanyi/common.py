#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def http_get(url, params=None, timeout=20, encode='utf-8', **kwargs):
    """Wrapper for requests.get().

    By default, it sets connection timeout to 20 seconds and
    response encoding to utf-8.
    """
    r = requests.get(url, params=params, timeout=timeout, **kwargs)
    r.encoding = encode
    return r

