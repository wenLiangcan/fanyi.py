#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['iciba_translate']

import xmltodict

from ..common import http_get

service_info = 'iciba.com'

params = {
    #'type': 'json', # 支持 json，可是 json 不返回例句！(╯°Д°)╯︵ ┻━┻
    'key': 'B792B1B7DBD9B48F8D861075810E3A1A',
    'w': ''
}

api = 'http://dict-co.iciba.com/api/dictionary.php'

def query(words):
    params['w'] = words.lower()   # Lower case can get more detailed results
    r = http_get(api, params)
    data = xmltodict.parse(r.text)['dict']
    data['key'] = words
    return data

def compile(data):
    return {
        'head': {
            'words': data['key'],
            'phonetic': None if not data.get('ps') \
            else (data['ps'],) if type(data['ps']) is str \
            else {
                'uk': data['ps'][0],
                'us': data['ps'][1]
            },
            'service': service_info
        },

        'explains': (
            # sentence
            (data['fy'],) if data.get('fy') \

            # word
            ## with single acception
            else (
                data['pos'] + ' ' + data['acceptation'],
            ) if type(data.get('pos')) is str

            ## with multiple acceptions
            else [
                ' '.join(item)
                for item in zip(data['pos'], data['acceptation'])
            ] if data.get('pos') and data.get('pos')[0] \

            ## no result
            else None
        ),

        'examples': None if not data.get('sent') \
        else [
            {
                'key': item['orig'],
                'value': item['trans']
            }
            for item in data['sent']
        ]
    }

def translate(words):
    return compile(query(words))

iciba_translate = translate

