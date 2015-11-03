#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Compiled with Coconut version 0.3.3-dev [Lauric]

"""
Author: Evan Hubinger
Date Created: 2014
Description: A Prisoner's Dilemma Adjudicator.
"""

# Coconut Header: --------------------------------------------------------------

from __future__ import with_statement, print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
if _coconut_sys.version_info < (3,):
    py2_filter, py2_hex, py2_map, py2_oct, py2_zip = filter, hex, map, oct, zip
    from future_builtins import *
    py2_range, range = range, xrange
    py2_int = int
    _coconut_int, _coconut_long = int, long
    class _coconut_metaint(type):
        def __instancecheck__(cls, inst):
            return isinstance(inst, (_coconut_int, _coconut_long))
    class int(_coconut_int):
        """Python 3 int."""
        __metaclass__ = _coconut_metaint
    py2_chr, chr = chr, unichr
    bytes, str = str, unicode
    _coconut_encoding = "UTF-8"
    py2_print = print
    _coconut_print = print
    def print(*args, **kwargs):
        """Python 3 print."""
        return _coconut_print(*(str(x).encode(_coconut_encoding) for x in args), **kwargs)
    py2_input = raw_input
    _coconut_input = raw_input
    def input(*args, **kwargs):
        """Python 3 input."""
        return _coconut_input(*args, **kwargs).decode(_coconut_encoding)

import os.path as _coconut_os_path
_coconut_sys.path.append(_coconut_os_path.dirname(_coconut_os_path.abspath(__file__)))
import __coconut__

__coconut_version__ = __coconut__.version
reduce = __coconut__.functools.reduce
itemgetter = __coconut__.operator.itemgetter
attrgetter = __coconut__.operator.attrgetter
methodcaller = __coconut__.operator.methodcaller
takewhile = __coconut__.itertools.takewhile
dropwhile = __coconut__.itertools.dropwhile
tee = __coconut__.itertools.tee
recursive = __coconut__.recursive
MatchError = __coconut__.MatchError

# Compiled Coconut: ------------------------------------------------------------


