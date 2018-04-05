# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [1, 100,100]  # cost has 3 values, corresponding to making


# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):
    paths = []
    complete = []

    best_complete = 999

    paths.append([[0, init[2], init[0], init[1], 1]])

    while len(paths) > 0:

        path = paths.pop()
        current = path[len(path) - 1]
        current_score = current[0]
        current_a = current[1]
        current_x = current[2]
        current_y = current[3]

        if current_score > best_complete:
            continue

        for c in range(len(action)):

            change = action[c]
            a = change + current_a
            a %= 4
            move = forward[a]
            new_x = current_x + move[0]
            new_y = current_y + move[1]

            if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
                continue

            if grid[new_x][new_y] == 1:
                continue

            action_cost = cost[c]
            new_score = current_score + action_cost

            new_h = c
            new_h %= 3

            new_entry = [new_score, a, new_x, new_y, new_h]
            new_path = list(path)
            new_path.append(new_entry)

            if new_x == goal[0] and new_y == goal[1]:
                complete.append(new_path)
                complete.sort()
                best_complete = complete[0][-1][0]
                break

            paths.append(new_path)

    best = complete[0]
    route = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    for i in range(1, len(best)):
        step = best[i - 1]
        route[step[2]][step[3]] = action_name[best[i][4]]

    route[best[-1][2]][best[-1][3]] = '*'

    for line in route:
        print line

    return route


optimum_policy2D(grid, init, goal, cost)
