Prisoner
========

A Python prisoner's dilemma competition adjudicator, written in [Coconut](https://github.com/evhub/coconut).

## Goal

The goal of the competition is to write a Prisoner's Dilemma bot that survives into the final round. Each round, every bot is pitted against every other bot for approximately (but not usually exactly) 100 rounds, and the bot or bots with the lowest average score among all the games they played that round are eliminated. The game continues until all the bots left are tied.

Score is determined as follows:

- Both cooperate:
    * +1 score for both
- Both defect:
    * no change in score
- One cooperates, one defects:
    * Cooperator: -1 score
    * Defector: +2 score

## Instructions

First, create a Python (`.py`) file containing this code:
```python
from prisoner.dilemma import *

@pd_bot
def my_bot_name(self_hist, opp_hist, opp_bot):
    <code>
```

Next, in place of `<code>`, insert whatever Python code you want that returns either `True` for cooperate or `False` for defect. To do this, you have use of the arguments `self_hist` (a list containing all your previous moves), `opp_hist` (a list containing all your opponent's previous moves), and `opp_bot` (your opponent's bot function).

All bot functions will be timed out in the case of infinite recursion and `False` assumed if nothing has been returned. To prevent this, bots may be added together, and if the first bot times out the second bot will be used instead.

## Examples

Cooperate:
```python
@pd_bot
def cooperate_bot(self_hist, opp_hist, opp_bot):
    return True
```

Defect:
```python
@pd_bot
def defect_bot(self_hist, opp_hist, opp_bot):
    return False
```

Coin Flip:
```python
@pd_bot
def coin_flip_bot(self_hist, opp_hist, opp_bot):
    return random.getrandbits(1)
```

Tit for Tat:
```python
@pd_bot
def tit_for_tat_bot(self_hist, opp_hist, opp_bot):
    if opp_hist:
        return opp_hist[-1]
    else:
        return True
```

Mirror:
```python
@pd_bot
def mirror_bot(self_hist, opp_hist, opp_bot):
    return opp_bot(opp_hist, self_hist, mirror_bot)
mirror_bot += cooperate_bot
```
