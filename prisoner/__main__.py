#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Compiled with Coconut version 0.3.3-dev [Lauric]

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

# IMPORTS:

import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prisoner import dilemma, bots

# BOT LISTS:

base_bots = {"cooperate": bots.cooperate_bot, "defect": bots.defect_bot, "tit_for_tat": bots.tit_for_tat_bot, "punisher": bots.punisher_bot, "nice_switcher": bots.nice_switcher_bot, "mean_switcher": bots.mean_switcher_bot, "exploit_or_tft": bots.exploit_or_tft_bot, "exploit_or_switch": bots.exploit_or_switch_bot, "exploit_or_punish": bots.exploit_or_punish_bot, "justice_mirror": bots.justice_mirror_bot, "mirror_or_tft": bots.mirror_or_tft_bot, "exploit_or_mirror": bots.exploit_or_mirror_bot, "tft_or_mirror": bots.tft_or_mirror_bot, "switch_or_mirror": bots.switch_or_mirror_bot, "punish_or_mirror": bots.punish_or_mirror_bot, "simulate_or_tft": bots.simulate_or_tft_bot, "simulate_or_mirror": bots.simulate_or_mirror_bot}

extra_bots = {"mirror_bots": bots.mirror_bot}

random_bots = {"coin_flip": bots.coin_flip_bot, "nice_tft": bots.nice_tft_bot, "delayed_tft": bots.delayed_tft_bot, "exploit_or_nice_tft": bots.exploit_or_nice_tft_bot, "exploit_or_delayed_tft": bots.exploit_or_delayed_tft_bot, "nice_tft_or_mirror": bots.nice_tft_or_mirror_bot, "delayed_tft_or_mirror": bots.delayed_tft_or_mirror_bot}

slow_bots = {"lookahead_or_tft": bots.lookahead_or_tft_bot}

quick_bots = base_bots.copy()
quick_bots.update(random_bots)

deterministic_bots = base_bots.copy()
deterministic_bots.update(slow_bots)

main_bots = base_bots.copy()
main_bots.update(random_bots)
main_bots.update(slow_bots)

all_bots = main_bots.copy()
all_bots.update(extra_bots)

# MAIN:

def main(bots):
    results = dilemma.winners(bots, time=1, debug=2)
    print("\n\n==== WINNERS ====\n")
    for winner in (reversed)(results):
        print("    " + winner)

if __name__ == "__main__":
    main(all_bots)
