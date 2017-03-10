from heapq import heappush, heappop

from defines import *

def astar(state, heuristics):
    goal = state.get_goal()
    fringe = []
    parents_dict = {}
    children_dict = {}
    costs_dict = {}
    heuristic_avg = 0.0
    for f in heuristics:
        heuristic_avg += f(state)
    heuristic_avg /= len(heuristics)
    heappush(fringe, (heuristic_avg, state))
    parents_dict[state] = None
    costs_dict[state] = 0
    iterations = 1
    while len(fringe) > 0:
        front = heappop(fringe)
        if front[1] == goal:
            s = front[1]
            path = []
            while s:
                path.append((costs_dict[s], s))
                s = parents_dict[s]
            return iterations, path[::-1]
        if iterations >= MAX_SEARCH_ITERATIONS:
            break
        in_closed = front[1] in children_dict
        if not in_closed:
            children_dict[front[1]] = front[1].get_adjacent_states()
            for s in children_dict[front[1]]:
                old_cost = float("inf") if s not in costs_dict else costs_dict[s]
                new_cost = costs_dict[front[1]] + front[1].get_transition_cost(s)
                parents_dict[s] = front[1] if s not in parents_dict or old_cost > new_cost else parents_dict[s]
                costs_dict[s] = new_cost if s not in costs_dict or old_cost > new_cost else costs_dict[s]
                in_fringe = -1
                for i, node in enumerate(fringe):
                    if s == node[1]:
                        in_fringe = i
                if in_fringe != -1:
                    if new_cost < old_cost:
                        fringe = fringe[:in_fringe] + fringe[in_fringe + 1:]
                        heuristic_avg = 0.0
                        for f in heuristics:
                            heuristic_avg += f(s)
                        heuristic_avg /= len(heuristics)
                        heappush(fringe, (costs_dict[s] + heuristic_avg, s))
                else:
                    if in_closed:
                        if new_cost < old_cost:
                            children_stack = children_dict[s][:]
                            closed_children = []
                            while len(children_stack) > 0:
                                ch = children_stack.pop()
                                if ch not in closed_children:
                                    closed_children.append(ch)
                                    if ch in costs_dict:
                                        costs_dict[ch] += (new_cost - old_cost)
                                        if ch in children_dict:
                                            children_stack += children_dict[ch][:]
                    else:
                        heuristic_avg = 0.0
                        for f in heuristics:
                            heuristic_avg += f(s)
                        heuristic_avg /= len(heuristics)
                        heappush(fringe, (costs_dict[s] + heuristic_avg, s))
        iterations += 1
    return iterations, None

def alphabeta(state, heuristics, depth=float("inf")):
    return maxvalue(state, heuristics, float("-inf"), float("inf"), depth)

def maxvalue(state, heuristics, a, b, depth):
    adjacent_states = state.get_adjacent_states()
    if depth < 1 or len(adjacent_states) < 1:
        heuristic_avg = 0.0
        for f in heuristics:
            heuristic_avg += f(state)
        return heuristic_avg
    for s in adjacent_states:
        a = max(a, minvalue(s, heuristics, a, b, depth - 1))
        if a >= b:
            return a
    return a

def minvalue(state, heuristics, a, b, depth):
    adjacent_states = state.get_adjacent_states()
    if depth < 1 or len(adjacent_states) < 1:
        heuristic_avg = 0.0
        for f in heuristics:
            heuristic_avg += f(state)
        return heuristic_avg
    for s in adjacent_states:
        b = min(b, maxvalue(s, heuristics, a, b, depth - 1))
        if b <= a:
            return b
    return b
