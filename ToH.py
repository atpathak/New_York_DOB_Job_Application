import copy
import itertools

#R = int(input())
R = 4
print("R = ",R)

#S = eval(input())
S = [0,1,1,0]
#S = [1,2,0,1,1,0,2,2,1,1,2,1,1,0,2]
#S = [1,2,0,1,1,0,2,2,1,1]
print("S = ",S)

assert type(S) == list
assert min(S) >= 0
assert max(S) <= R-1

def num_of_moves(current_state, target):
    total_disks = current_state[0] + current_state[1] + current_state[2]
    n = len(total_disks)
    if n == 0:
        return 0
    min_disk = min(total_disks)
    min_rod = None
    for k in range(3):
        if min_disk in current_state[k]:
            min_rod = k
    current_state[min_rod].pop(0)
    print(current_state)
    if min_rod == target:
        return num_of_moves(current_state, target)
    else:
        new_target = (0 + 1 + 2) - (target + min_rod)
        return num_of_moves(current_state, new_target) + 1 + (2**(n-1) - 1)

def top(stack):
    return stack[-1] if len(stack) != 0 else -1

def perform_bfs(initial_state):
    history = []
    states_to_explore = [(initial_state, 0)]
    while len(states_to_explore) != 0:
        current_state, current_depth = states_to_explore.pop(0)
        history.append(current_state)
        if len(current_state[0]) == len(S):
            return current_depth
        allowed_moves = [(i, j) for (i, j) in itertools.permutations(range(R), 2) if top(current_state[i]) > top(current_state[j])]
        for (i, j) in allowed_moves:
            next_state = copy.deepcopy(current_state)
            next_state[j].append(next_state[i].pop())
            if next_state not in history:
                states_to_explore.append((next_state, current_depth + 1))
    return None


d = {}
for r in range(R):
    d[r] = [i for (i, j) in enumerate(S) if j == r]

print("d = ",d)

dcopy=copy.deepcopy(d)

print("Guess = ",num_of_moves(d, 0))

d = dcopy
print("d = ",d)
print("Answer = ", perform_bfs(d))
