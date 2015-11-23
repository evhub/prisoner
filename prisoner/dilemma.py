#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0x32c7a53e

# Compiled with Coconut version 0.3.4-post_dev [Macapuno]

# Coconut Header: --------------------------------------------------------------

from __future__ import with_statement, print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
if _coconut_sys.version_info < (3,):
    _coconut_encoding = "UTF-8"
    py2_filter, py2_hex, py2_map, py2_oct, py2_zip, py2_open, py2_range, py2_int, py2_chr, py2_str, py2_print, py2_input = filter, hex, map, oct, zip, open, range, int, chr, str, print, input
    _coconut_int, _coconut_long, _coconut_str, _coconut_bytearray, _coconut_print, _coconut_unicode, _coconut_raw_input = int, long, str, bytearray, print, unicode, raw_input
    range, chr, str = xrange, unichr, unicode
    from future_builtins import *
    from io import open
    class _coconut_metaint(type):
        def __instancecheck__(cls, inst):
            return isinstance(inst, (_coconut_int, _coconut_long))
    class int(_coconut_int):
        """Python 3 int."""
        __metaclass__ = _coconut_metaint
    class _coconut_metabytes(type):
        def __instancecheck__(cls, inst):
            return isinstance(inst, _coconut_str)
    class bytes(_coconut_str):
        """Python 3 bytes."""
        __metaclass__ = _coconut_metabytes
        def __new__(cls, *args, **kwargs):
            """Python 3 bytes constructor."""
            return _coconut_str.__new__(cls, _coconut_bytearray(*args, **kwargs))
    def print(*args, **kwargs):
        """Python 3 print."""
        return _coconut_print(*(_coconut_unicode(x).encode(_coconut_encoding) for x in args), **kwargs)
    def input(*args, **kwargs):
        """Python 3 input."""
        return _coconut_raw_input(*args, **kwargs).decode(_coconut_encoding)

import os.path as _coconut_os_path
_coconut_sys.path.append(_coconut_os_path.dirname(_coconut_os_path.abspath(__file__)))
import __coconut__

__coconut_version__ = __coconut__.version
reduce = __coconut__.functools.reduce
takewhile = __coconut__.itertools.takewhile
dropwhile = __coconut__.itertools.dropwhile
tee = __coconut__.itertools.tee
recursive = __coconut__.recursive
datamaker = __coconut__.datamaker
MatchError = __coconut__.MatchError

# Compiled Coconut: ------------------------------------------------------------

# IMPORTS:

import itertools
import random
import threading

# DEFAULTS:

default_payoffs = ((2, 2), (0, 3), (3, 0), (1, 1))

def around(n): return int(random.gauss(n, n / 10))
default_rounds = around(100)

# BOT CONSTRUCTOR:

class pd_bot(object):
    default = False

    def __init__(self, *funcs):
        self.funcs = (tuple)(funcs)

    def copy(self):
        out = pd_bot(*self.funcs)
        out.default = self.default
        return out

    def __iadd__(self, other):
        if isinstance(other, pd_bot):
            self.funcs += (other.funcs)
            return self
        else:
            raise TypeError("pd_bot objects can only be added to other pd_bot objects, not " + repr(other))

    def __add__(self, other):
        out = self.copy()
        out += (other)
        return out

    def __call__(self, self_hist, opp_hist, opp_bot, time=None):
        for func in self.funcs:
            if time is None:
                result = func(list(self_hist), list(opp_hist), opp_bot)
            else:
                result = time_limit(__coconut__.functools.partial(func, list(self_hist), list(opp_hist), opp_bot), None, time)
            if result is not None:
                return (bool)(result)
        return self.default

# GAME UTILITIES:

def time_limit(func, default, time):
    class storage(__coconut__.object):
        result = default
        def run(self):
            try:
                self.result = func()
            except (RuntimeError):
                pass
    store = storage()
    runner = threading.Thread(target=store.run)
    runner.start()
    runner.join(time)
    if runner.isAlive():
        runner.terminate()
    return store.result

def bot_call(a, a_hist, b, b_hist, time=None):
    if isinstance(a, pd_bot) and isinstance(b, pd_bot):
        return (bool)(a(list(a_hist), list(b_hist), b, time))
    else:
        raise TypeError("bots must be pd_bot objects, not " + repr(a) + " and " + repr(b))

def moves(a, b, a_hist, b_hist, time=None):
    return (bot_call(a, a_hist, b, b_hist, time), bot_call(b, b_hist, a, a_hist, time))

def game(a, b, a_hist=None, b_hist=None, time=None, debug=0):
    if a_hist is None:
        a_hist = []
    else:
        a_hist = list(a_hist)
    if b_hist is None:
        b_hist = []
    else:
        b_hist = list(b_hist)
    while True:
        a_c, b_c = moves(a, b, a_hist, b_hist, time)
        a_hist.append(a_c)
        b_hist.append(b_c)
        if debug > 0:
            print("    " + str(a_c) + " " * (a_c + 1) + str(b_c))
        yield a_c, b_c

def score_move(a_c, b_c, payoffs=default_payoffs):
    if a_c and b_c:
        return payoffs[0]
    elif a_c:
        return payoffs[1]
    elif b_c:
        return payoffs[2]
    else:
        return payoffs[3]

def score_game(moveiter, payoffs=default_payoffs):
    a_score = 0
    b_score = 0
    for a_c, b_c in moveiter:
        a_change, b_change = score_move(a_c, b_c, payoffs)
        a_score += (a_change)
        b_score += (b_change)
        yield (a_score, b_score)

def tally(a, b, a_hist=None, b_hist=None, time=None, payoffs=default_payoffs, debug=0):
    return (__coconut__.functools.partial(score_game, payoffs=payoffs))(game(a, b, a_hist, b_hist, time, debug))

def round_robin(participants, time=None, rounds=default_rounds, payoffs=default_payoffs, debug=0):
    if rounds > 0:
        scores = {}
        for participant in participants:
            scores[participant] = 0
        for a, b in itertools.permutations(participants.keys(), 2):
            if debug > 0:
                print("\n-- " + a + " vs. " + b + " --")
            a_score, b_score = (lambda i: __coconut__.itertools.islice(tally(participants[a], participants[b], time=time, payoffs=payoffs, debug=debug - 1), i.start, i.stop, i.step) if isinstance(i, __coconut__.slice) else next(__coconut__.itertools.islice(tally(participants[a], participants[b], time=time, payoffs=payoffs, debug=debug - 1), i, i + 1)))(rounds - 1)
            scores[a] += (a_score)
            scores[b] += (b_score)
            if debug > 0:
                print("    " + a + ": " + str(a_score))
                print("    " + b + ": " + str(b_score))
        return scores
    else:
        raise ValueError("rounds must be > 0")

def score_sort(scores):
    return (__coconut__.functools.partial(sorted, key=lambda p: p[1]))(scores.items())

def tournament(participants, time=None, rounds=default_rounds, payoffs=default_payoffs, debug=0):
    if debug > 0:
        count = 0
    while len(participants) > 1:
        if not isinstance(rounds, int):
            rounds = rounds()
        if debug > 0:
            count += (1)
            print("\n\n==== ROUND " + str(count) + " ====")
        scores = round_robin(participants, time, rounds, payoffs, debug - 1)
        yield scores
        participants = participants.copy()
        lowest = None
        for name, score in (score_sort)(scores):
            if lowest is None:
                lowest = score
            if score == lowest:
                del participants[name]

def score_repr(scores):
    out = ["{"]
    for name, score in (reversed)((score_sort)(scores)):
        out.append("    " + name + ": " + str(score))
    out.append("}")
    return "\n".join(out)

def winners(participants, limit=None, time=None, rounds=default_rounds, payoffs=default_payoffs, debug=0):
    count = 0
    for scores in tournament(participants, time, rounds, payoffs, debug - 1):
        count += (1)
        if debug > 0:
            print("\nROUND " + str(count) + " RESULTS:\n" + score_repr(scores))
        if limit is not None and count >= limit:
            break
    return (list)(scores.keys())

# BOT UTILITIES:

def simulate(self_bot, self_hist, opp_bot, opp_hist, self_move=None, opp_move=None):
    if opp_move is None:
        opp_move = opp_bot(opp_hist, self_hist, self_bot)
    if self_move is None:
        return (simulate(self_bot, self_hist, opp_bot, opp_hist, True, opp_move), simulate(self_bot, self_hist, opp_bot, opp_hist, False, opp_move))
    else:
        return __coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: (_coconut_lazy_item() for _coconut_lazy_item in (lambda: (self_move, opp_move),)), lambda: game(self_bot, opp_bot, self_hist + [self_move], opp_hist + [opp_move], None))))

def winnings(self_bot, self_hist, opp_bot, opp_hist, self_move=None, payoffs=default_payoffs):
    simulation = simulate(self_bot, self_hist, opp_bot, opp_hist, self_move)
    if self_move is None:
        return (score_game(simulation[0], payoffs=payoffs), score_game(simulation[1], payoffs=payoffs))
    else:
        return score_game(simulation, payoffs=payoffs)

def decide(c_scores, d_scores):
    if c_scores[0] > d_scores[0]:
        return True
    elif d_scores[0] > c_scores[0]:
        return False
    elif c_scores[1] < d_scores[1]:
        return True
    elif d_scores[1] < c_scores[1]:
        return False
    else:
        return None
