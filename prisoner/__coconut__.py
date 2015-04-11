#!/usr/bin/env python

# Compiled with Coconut version 0.2.1-dev [Eocene]

# Coconut Header: --------------------------------------------------------------

from __future__ import with_statement, print_function, absolute_import, unicode_literals, division
try:
    from future_builtins import *
except ImportError:
    pass

"""Built-In Coconut Functions."""

import functools
partial = functools.partial
reduce = functools.reduce

import operator
itemgetter = operator.itemgetter
attrgetter = operator.attrgetter
methodcaller = operator.methodcaller

import itertools
chain = itertools.chain
islice = itertools.islice
takewhile = itertools.takewhile
dropwhile = itertools.dropwhile
tee = itertools.tee

import collections
data = collections.namedtuple

def iterable(obj):
    """Determines Whether An Object Is Iterable."""
    try:
        iter(obj)
    except TypeError:
        return False
    else:
        return True

def bool_and(a, b):
    """Boolean And Operator Function."""
    return a and b

def bool_or(a, b):
    """Boolean Or Operator Function."""
    return a or b

def compose(f, g):
    """Composing (f..g)."""
    return lambda *args, **kwargs: f(g(*args, **kwargs))

def pipe(*args):
    """Pipelining (x |> func)."""
    out = args[0]
    for func in args[1:]:
        out = func(out)
    return out

def recursive(func):
    """Tail Call Optimizer."""
    state = [True, None]
    recurse = object()
    @functools.wraps(func)
    def tailed_func(*args, **kwargs):
        """Tail Recursion Wrapper."""
        if state[0]:
            state[0] = False
            try:
                while True:
                    result = func(*args, **kwargs)
                    if result is recurse:
                        args, kwargs = state[1]
                        state[1] = None
                    else:
                        return result
            finally:
                state[0] = True
        else:
            state[1] = args, kwargs
            return recurse
    return tailed_func
