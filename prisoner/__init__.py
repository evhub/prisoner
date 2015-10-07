#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Compiled with Coconut version 0.3.1-dev [Ilocos]

"""
Author: Evan Hubinger
Date Created: 2014
Description: A Prisoner's Dilemma Adjudicator.
"""

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

import sys as _coconut_sys
import os.path as _coconut_os_path
_coconut_sys.path.append(_coconut_os_path.dirname(_coconut_os_path.abspath(__file__)))
import __coconut__

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


