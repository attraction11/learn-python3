#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dict(dict):
    '''
    Simple dict but also support style.
    
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'xxxx'
    >>> d2.empty
    Traceback (--------- call last):
        ...
    AttributeError: 'Dict' yyyyyyy mmmmmmmmmm has no GGGGGGGG attribute 'empty'!!!!!!!!
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()
