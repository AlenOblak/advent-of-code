import math

lines = open('input.txt').read().split('\n')
boxes = [list(map(int, l.split(','))) for l in lines]

def calc_distance(box_a, box_b):
    return math.sqrt((boxes[box_a][0]-boxes[box_b][0])**2 + (boxes[box_a][1]-boxes[box_b][1])**2 + (boxes[box_a][2]-boxes[box_b][2])**2)

def connect(a, b):
    a_in = False
    b_in = False
    for j in junctions:
        if a in j:
            a_in = j
        if b in j:
            b_in = j
    if a_in == False and b_in == False:
        junctions.append([a, b])
    if a_in == False and b_in != False:
        b_in.append(a)
    if a_in != False and b_in == False:
        a_in.append(b)
    if a_in != False and b_in != False and a_in != b_in:
        for b in b_in:
            a_in.append(b)
        junctions.remove(b_in)

# part 1
distances = sorted([(calc_distance(i, j), i, j) for i in range(0, len(boxes) - 1) for j in range(i+1, len(boxes))])
junctions = []
for i in range(0, 1000):
    connect(distances[i][1], distances[i][2])
lengths = sorted([len(j) for j in junctions], reverse=True)
print(math.prod(lengths[0:3]))

# part 2
i = 1000
while(True):
    connect(distances[i][1], distances[i][2])
    if len(junctions) == 1 and len(junctions[0]) == len(boxes):
        print(boxes[distances[i][1]][0] * boxes[distances[i][2]][0])
        break
    i = i + 1
