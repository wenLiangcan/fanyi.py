#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['youdao_translate']

from ..common import http_get

service_info = 'fanyi.youdao.com'

params = {
    'keyfrom': 'fanyi-py',
    'key': '830666419',
    'type': 'data',
    'doctype': 'json',
    'version': '1.1',
    'q': ''
}

api = 'http://fanyi.youdao.com/openapi.do'

def query(words):
    params['q'] = words
    r = http_get(api, params)
    data = r.json()
    data['query'] = words # To avoid the numeric character references in returned data
    return data

def compile(data):
    basic = data.get('basic')
    return {
        'head': {
            'words': data.get('query'),
            'phonetic': None if not basic or len(basic) < 2 \
            else (basic['phonetic'],) if len(basic) == 2 \
            else {
                'uk': basic['uk-phonetic'],
                'us': basic['us-phonetic']
            },
            'service': service_info
        },

        'explains': basic.get('explains') if basic else None,

        'examples': None if not data.get('web') \
        else [
            {
                'key': item['key'],
                'value': '，'.join(item['value'])
            }
            for item in data['web']
        ]
    }

def translate(words):
    return compile(query(words))

youdao_translate = translate

