# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0]]

goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']

open = []


def optimum_policy(grid, goal, cost):
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    value[goal[0]][goal[1]] = 0

    done = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    done[goal[0]][goal[1]] = 1

    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    policy[goal[0]][goal[1]] = '*'

    goal_scored = [0, goal[0], goal[1]]

    open.append(goal_scored)

    while len(open) > 0:

        open.sort()
        open.reverse()
        next = open.pop()

        for i in range(len(delta)):

            x1 = next[1]
            y1 = next[2]

            x2 = x1 - delta[i][0]
            y2 = y1 - delta[i][1]

            if 0 <= x2 < len(grid) and len(grid[0]) > y2 >= 0 == done[x2][y2]:

                if grid[x2][y2] == 1:
                    value[x2][y2] = 99
                else:
                    value[x2][y2] = value[x1][y1] + cost
                    open.append([value[x2][y2], x2, y2])
                    policy[x2][y2] = delta_name[i]

                done[x2][y2] = 1

    for line in policy:
        print line

    return policy


optimum_policy(grid, goal, cost)
