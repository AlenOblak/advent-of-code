from copy import deepcopy

lines = open('input.txt').read().split('\n')

max_x = len(lines[0])
max_y = len(lines)
map = []

for line in lines:
    map.append([c for c in line])

def num_around(x, y):
    result = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i >= 0 and i < max_x and j >= 0 and j < max_y and (x != i or y != j) and map[i][j] == '@':
                result += 1
    return result

def new_map(map):
    new_m = deepcopy(map)
    changes = 0
    for j in range(0, max_y):
        for i in range(0, max_x):
            if map[i][j] == '@':
                around = num_around(i, j)
                if around < 4:
                    new_m[i][j] = '.'
                    changes += 1
    return new_m, changes

result = 0
changes = 1
step = 0
while changes > 0:
    map, changes = new_map(map)
    result += changes
    step += 1
    if step == 1:
        # part 1
        print(result)

# part 2
print(result)