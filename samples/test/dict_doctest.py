#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

<<<<<<< HEAD
    >>> d1 = 
    >>> d1['x'] = 100
    >>> dsaasd1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
=======

>>>>>>> f4e8f2d (yyyy)
    
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'xxxx'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' yyyyyyy has no attribute 'empty'
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
