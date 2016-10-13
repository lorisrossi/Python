romania_map = {'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
               'Zerind': [('Arad', 75), ('Oradea', 71)],
               'Sibiu': [('Arad', 140), ('Oradea', 151),
                         ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
               'Timisoara': [('Arad', 118), ('Lugoj', 111)],
               'Oradea': [('Zerind', 71), ('Sibiu', 151)],
               'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
               'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97),
                                  ('Craiova', 146)],
               'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
               'Bucharest': [('Fagaras', 211), ('Pitesti', 101),
                             ('Urziceni', 85), ('Giurgiu', 90)],
               'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138),
                           ('Bucharest', 101)],
               'Craiova': [('Rimnicu Vilcea', 146), ('Pitesti', 138),
                           ('Drobeta', 120)],
               'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
               'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
               'Giurgiu': [('Bucharest', 90)],
               'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
               'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
               'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
               'Iasi': [('Vaslui', 92), ('Neamt', 87)],
               'Eforie': [('Hirsova', 86)],
               'Neamt': [('Iasi',87)]}


def successors(city):
    "Return a list of successors of the city."
    return romania_map[city]

def breadth_first_remove(frontier):
    "Return the path with mininum breadth, and remove it from the frontier."
    return frontier.pop(0)

def depth_first_remove(frontier):
    "Return the path with max depth, and remove it from the frontier."
    depth_path = max(frontier, key=len)
    frontier.remove(depth_path)
    return depth_path

def cheapest_first_remove(frontier):
    "Return the path with cheapest cost, and remove it from the frontier."
    cheap_path = min(frontier, key=lambda p: p[-1][1])
    frontier.remove(cheap_path)
    return cheap_path

def search_agent(start, goal):
    "Return a path from start to goal, if it exists."
    checked, frontier = [], [[(start, 0)]]
    while frontier:
        path = depth_first_remove(frontier)
        last_city, last_cost = path[-1]
        if last_city == goal:
            print frontier
            return path
        checked.append(last_city)
        for next_city, next_cost in successors(last_city):
            if next_city not in checked:
                frontier.append(path+[(next_city, next_cost+last_cost)])
    return None

print search_agent('Arad', 'Bucharest')
