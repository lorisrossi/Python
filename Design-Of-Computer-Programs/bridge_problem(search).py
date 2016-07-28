import doctest

def bridge_problem(here):
    "Find the fastest (least elapsed time) path to the goal in the bridge problem."
    here = frozenset(here) | frozenset(['light'])
    explored = set() # set of states we have visited
    # State will be a (people-here, people-there, time-elapsed)
    frontier = [ [(here, frozenset())] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        here1, there1 = state1 = final_state(path)
        if not here1 or (len(here1) == 1 and 'light' in here1):
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in bsuccessors(state1).items():
            if state not in explored:
                total_cost = pcost + bcost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(frontier, path2)
    return Fail

Fail = []

def final_state(path): return path[-1]

def add_to_frontier(frontier, path):
    "Add path to frontier, replacing costlier path if there is one."
    # Find if there is an old path to the final state of this path.
    old = None
    for i,p in enumerate(frontier):
        if final_state(p) == final_state(path):
            old = i
            break
    if old is not None and path_cost(frontier[old]) < path_cost(path):
        return # Old path was better; do nothing
    elif old is not None:
        del frontier[old] # Old path was worse; delete it
    ## Now add the new path and re-sort
    frontier.append(path)
    frontier.sort(key=elapsed_time)

def elapsed_time(path):
    return path[-1][1]


def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light'. Action is represented as a tuple (person1, person2, arrow),
    where arrow is '->' for here to there and '<-' for there to here."""
    here, there = state
    if 'light' in here:
        return dict(((here  - frozenset([a, b, 'light']),
                      there | frozenset([a, b, 'light'])),
                      (a, b, '->'))
                      for a in here if a is not 'light'
                      for b in here if b is not 'light')
    else:
        return dict(((here  | frozenset([a, b, 'light']),
                      there - frozenset([a, b, 'light'])),
                      (a, b, '<-'))
                      for a in there if a is not 'light'
                      for b in there if b is not 'light')

def path_states(path):
    "Return a list of states in this path."
    return path[0::2]

def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]

def path_cost(path):
    "The total cost of a path (which is stored in a tuple with the final action)."
    ## path = [state, (action, total_cost), state, ...]
    if len(path) < 3:
        return 0
    else:
        action, total_cost = path[-2]
        return total_cost

def bcost(action):
    "Returns the cost (a number) of an action in the bridge problem."
    # An action is an (a, b, arrow) tuple; a and b are times; arrow is a string
    a, b, arrow = action
    return max(a, b)



class TestBridge: """
## There are two equally good solutions
>>> S1 = [(2, 1, '->'), (1, 1, '<-'), (5, 10, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> S2 = [(2, 1, '->'), (2, 2, '<-'), (5, 10, '->'), (1, 1, '<-'), (2, 1, '->')]
>>> path_actions(bridge_problem([1,2,5,10])) in (S1, S2)
True

>>> path_actions(bridge_problem([1,3,4])
[(1, 4, '->'), (1, 1, '<-'), (1, 3, '->')]

>>> elapsed_time(bridge_problem([1,2,5,10]))
17
"""
print doctest.testmod()

print bridge_problem([1, 2, 5, 10])
