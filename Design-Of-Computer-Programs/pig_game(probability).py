## states are tuples of the form:
## (p, me, you, pending) where
## p: an int, 0 or 1, indicating which player's turn it is
## me: an int, the player-to-move's current score
## you: an int, the other player's current score
## pending: an int, the number of point accumulated on current turn, not yet scored
import random
from toolsUnit3 import memo

goal = 50
possible_moves = ['roll', 'hold']

def dierolls():
    "Generate die rolls."
    while True:
        yield random.randint(1,6)

def play_pig(A, B, dierolls=dierolls()):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    strategies = [A, B]
    state = (0, 0, 0, 0)
    if strategies[0](state) not in possible_moves:
        return strategies[1]
    if strategies[1](state) not in possible_moves:
        return strategies[0]
    while True:
        (p, me, you, pending) = state
        if me >= goal:
            return strategies[p]
        elif you >= goal:
            return strategies[other[p]]
        elif strategies[p](state) == 'hold':
            state = hold(state)
        else:
            state = roll(state, next(dierolls))

def clueless(state):
    "A strategy that ignores the state and chooses at random from possible moves."
    return random.choice(possible_moves)

def hold_at(x):
    "Return a strategy that holds if pending >= x or player reaches goal."
    def strategy(state):
        (p, me, you, pending) = state
        return 'hold' if (pending >= x or me + pending >= goal) else 'roll'
    strategy.__name__ = 'hold_at(%d)' % x
    return strategy

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    (p, me, you, pending) = state
    return (other[p], you, me+pending, 0)

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me+1, 0) # pig out; other player's turn
    else:
        return (p, me, you, pending+d) # accumulate die roll in pending

other = {1:0, 0:1} # mapping from player to other player

## Optimal pig

def best_action(state, actions, Q, U): # Q is Quality, U is Utility (game theory)
    "Return the optimal action for a state, given U."
    def EU(action): return Q(state, action, U)
    return max(actions(state), key = EU)

def max_wins(state):
    "The optimal pig strategy chooses an action with the highest win probability."
    return best_action(state, pig_actions, Q_pig, Pwin)

def max_diffs(state):
    """A strategy that maximizes the expected difference between my final score
    and my opponent's."""
    return best_action(state, pig_actions, Q_pig, win_diff)

@memo
def Pwin(state):
    """The utility of a state; here just the probability that an optimal player
    whose turn it is to move can win from the current state."""
    # Assumes opponent also plays with optimal strategy.
    (p, me, you, pending) = state
    if me + pending >= goal:
        return 1
    elif you >= goal:
        return 0
    else:
        return max(Q_pig(state, action, Pwin)
                    for action in pig_actions(state))

@memo
def win_diff(state):
    "The utility of a state: here the winning differential (pos or neg)."
    (p, me, you, pending) = state
    if me + pending >= goal or you >= goal:
        return (me + pending - you)
    else:
        return max(Q_pig(state, action, win_diff)
                    for action in pig_actions(state))

def Q_pig(state, action, Pwin):
    "The expected value of choosing action in state."
    if action == 'hold':
        return 1 - Pwin(hold(state))
    if action == 'roll':
        return (1 - Pwin(roll(state,1))
                + sum(Pwin(roll(state, d)) for d in (2,3,4,5,6))) / 6
    raise ValueError

def pig_actions(state):
    "The legal actions from a state."
    _, _, _, pending = state
    return ['roll', 'hold'] if pending else ['roll']

## Confronta max_wins e max_diffs

states = [(0, me, you, pending)
          for me in range(41) for you in range(41) for pending in range(41)
          if me + pending <= goal]

from collections import defaultdict

def story():
    r = defaultdict(lambda: [0, 0])
    for s in states:
        w, d = max_wins(s), max_diffs(s)
        if w != d:
            _, _, _, pending = s
            i = 0 if (w == 'roll') else 1
            r[pending][i] += 1
    for (delta, (wrolls, drolls)) in sorted(r.items()):
        print '%4d: %3d %3d' % (delta, wrolls, drolls)

def test_actions():
    s = (0, 10, 20, 30)
    assert hold(s) == (1, 20, 40, 0)
    assert roll(s, 6) == (0, 10, 20, 36)
    assert roll(s, 1) == (1, 20, 11, 0)
    return 'test actions passes'

def test():
    A, B = hold_at(50), clueless
    rolls = iter([6, 6, 6, 6, 6, 6, 6, 6, 6])
    assert play_pig(A, B, rolls) == A
    return 'tests pass'

#print test()
#story()
