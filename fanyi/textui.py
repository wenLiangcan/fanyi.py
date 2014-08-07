#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from clint.textui import colored, indent, puts


def _dim(string):
    """Dim the string.
    """
    Style = colored.colorama.Style
    if Style.NORMAL in string:
        return string.replace(Style.NORMAL, Style.DIM, 1)
    else:
        return string.join([Style.DIM, Style.NORMAL])

colored.dim = _dim

def high_light(words, texts):
    """High lighting keywords.
    """
    # Dirty hack for optimizing Chinese words matching.
    # Because Chinese language does not use spaces for word segmentaion,
    # the word boundary pattern `\b` isn't work for Chinese words.
    if ' ' in texts:
        ptn = re.compile(r'\b{}\b'.format(words), re.IGNORECASE)
    else:
        ptn = re.compile(r'{}'.format(words), re.IGNORECASE)

    # Set keywords to white and bold
    def repl(m):
        return str(colored.white(m.group(), bold=True))

    return re.sub(ptn, repl, texts)

def get_output(translation):
    """Convert the translation data to readable texts.

    The function accept a dictionary which has structure as below:

    {
        'head': {
            'words': <str words>,
            'phonetic': None | (<str phonetic>,) | {'uk': <str>, 'us' <str>:},
            'service' <str service_name>:
        },
        'explains': None | [<str explains>, ...],
        'examples': None | [{'key':, 'value':}, ...]
    }
    """
    result = {}

    # head
    head = translation['head']
    result['head'] = '\n'
    result['head'] += head['words']
    if head['phonetic']:
        if len(head['phonetic']) == 2:
            result['head'] += colored.magenta(
                '  英[ {} ]  美[ {} ]'.format(
                    head['phonetic']['uk'], head['phonetic']['us']
                )
            )
        else:
            result['head'] += colored.magenta(
                '  [ {} ]'.format(head['phonetic'][0])
            )
    result['head'] += colored.dim('  ~  '+head['service'])

    # explains
    result['explains'] = ''
    if translation.get('explains'):
        for item in translation['explains']:
            result['explains'] += colored.dim('\n- ') + colored.green(item)

    # examples
    result['examples'] = ''
    if translation.get('examples'):
        for index, value in enumerate(translation['examples']):
            result['examples'] += colored.dim('\n{}. '.format(index+1)) + \
                high_light(head['words'], value['key']) + \
                '\n   ' + colored.cyan(value['value'])

    return result

def show(translation, convertor=get_output, i=1):
    """Convert the raw translation data and print it with indent.

    The default indent level is 1.
    """
    result = convertor(translation)

    def put_section(section, output=result):
        if output.get(section):
            puts(output.get(section))

    with indent(i):
        put_section('head')
        put_section('explains')
        put_section('examples')

