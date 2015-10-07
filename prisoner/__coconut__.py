
# Coconut Header: --------------------------------------------------------------

from __future__ import with_statement, print_function, absolute_import, unicode_literals, division
try: from future_builtins import *
except ImportError: pass
try: xrange
except NameError: pass
else:
    range = xrange
try: ascii
except NameError: ascii = repr
try: unichr
except NameError: pass
else:
    py2_chr = chr
    chr = unichr
_coconut_encoding = "UTF-8"
try: unicode
except NameError: pass
else:
    bytes, str = str, unicode
    py2_print = print
    def print(*args, **kwargs):
        """Wraps py2_print."""
        return py2_print(*(str(x).encode(_coconut_encoding) for x in args), **kwargs)
try: raw_input
except NameError: pass
else:
    py2_input = raw_input
    def input(*args, **kwargs):
        """Wraps py2_input."""
        return py2_input(*args, **kwargs).decode(_coconut_encoding)

"""Built-in Coconut Functions."""

import functools
import operator
import itertools
import collections

try:
    import collections.abc as abc
except ImportError:
    abc = collections

object = object
int = int
set = set
frozenset = frozenset
tuple = tuple
list = list
len = len
isinstance = isinstance
getattr = getattr
slice = slice

def recursive(func):
    """Tail Call Optimizer."""
    state = [True, None] # toplevel, (args, kwargs)
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

class MatchError(Exception):
    pass
