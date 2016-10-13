# python encoding: latin-1
import random

BOARD = [1,2,3,4,5,6,7,8,' ']
random.shuffle(BOARD)


def show_board(board):
    "Print the board."
    print '---------'
    print '|       |'
    print '|',
    for i in range(len(board)):
        if i!=0 and i%3 == 0:
            print '|'; print'|',
        print board[i],
    print '|'
    print '|       |'
    print '---------'

def swap(board, x, y):
    board[x], board[y] = board[y], board[x]

def successors(board):
    "Return all the possible moves from the input board."
    blank = board.index(' ')
    new_boards = [list(board), list(board)]
    up_left_corner, up_edge, up_right_corner = 0, 1, 2
    mid_left_edge, center, mid_right_edge = 3, 4, 5
    down_left_corner, down_edge, down_right_corner = 6, 7, 8
    if blank == up_left_corner:
        swap(new_boards[0], 0, 3)
        swap(new_boards[1], 0, 1)
    elif blank == up_edge:
        new_boards += [list(board)]
        swap(new_boards[0], 1, 0)
        swap(new_boards[1], 1, 2)
        swap(new_boards[2], 1, 4)
    elif blank == up_right_corner:
        swap(new_boards[0], 2, 1)
        swap(new_boards[1], 2, 5)
    elif blank == mid_left_edge:
        new_boards += [list(board)]
        swap(new_boards[0], 3, 0)
        swap(new_boards[1], 3, 4)
        swap(new_boards[2], 3, 6)
    elif blank == center:
        new_boards += [list(board), list(board)]
        swap(new_boards[0], 4, 1)
        swap(new_boards[1], 4, 3)
        swap(new_boards[2], 4, 5)
        swap(new_boards[3], 4, 7)
    elif blank == mid_right_edge:
        new_boards += [list(board)]
        swap(new_boards[0], 5, 2)
        swap(new_boards[1], 5, 4)
        swap(new_boards[2], 5, 8)
    elif blank == down_left_corner:
        swap(new_boards[0], 6, 3)
        swap(new_boards[1], 6, 7)
    elif blank == down_edge:
        new_boards += [list(board)]
        swap(new_boards[0], 7, 6)
        swap(new_boards[1], 7, 4)
        swap(new_boards[2], 7, 8)
    elif blank == down_right_corner:
        swap(new_boards[0], 8, 7)
        swap(new_boards[1], 8, 5)
    return new_boards

def puzzle_problem(start, goal=(1,2,3,4,5,6,7,8,' ')):
    "Return a solution, if it exists."
    frontier, explored = [[start]], set()
    while frontier:
        path = frontier.pop(0)
        state = path[-1]
        if state == goal:
            return path
        explored.add(state)
        for successor in successors(state):
            if tuple(successor) not in explored:
                frontier.append(path + [tuple(successor)])
    return None


show_board(BOARD)
solution = puzzle_problem(tuple(BOARD))
print solution
if solution: print 'Moves:', len(solution)
