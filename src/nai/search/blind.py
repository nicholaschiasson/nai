from collections import deque

from defines import *

def bfs(state):
    goal = state.get_goal()
    fringe = deque()
    fringe.append((None, state))
    closed = []
    iterations = 1
    while len(fringe) > 0:
        front = fringe.popleft()
        if front[1] == goal:
            s = front
            path = []
            while s:
                path.append(s[1])
                s = s[0]
            path = path[::-1]
            for i in range(len(path)):
                if i > 0:
                    path[i] = (path[i - 1][0] + path[i - 1][1].get_transition_cost(path[i]), path[i])
                else:
                    path[i] = (0, path[i])
            return iterations, path
        if iterations >= MAX_SEARCH_ITERATIONS:
            break
        if front[1] not in closed:
            closed.append(front[1])
            for s in front[1].get_adjacent_states():
                fringe.append((front, s))
        iterations += 1
    return iterations, None

def dfs(state):
    goal = state.get_goal()
    fringe = [(None, state)]
    closed = []
    iterations = 1
    while len(fringe) > 0:
        front = fringe.pop()
        if front[1] == goal:
            s = front
            path = []
            while s:
                path.append(s[1])
                s = s[0]
            path = path[::-1]
            for i in range(len(path)):
                if i > 0:
                    path[i] = (path[i - 1][0] + path[i - 1][1].get_transition_cost(path[i]), path[i])
                else:
                    path[i] = (0, path[i])
            return iterations, path
        if iterations >= MAX_SEARCH_ITERATIONS:
            break
        if front[1] not in closed:
            closed.append(front[1])
            for s in front[1].get_adjacent_states()[::-1]:
                fringe.append((front, s))
        iterations += 1
    return iterations, None
