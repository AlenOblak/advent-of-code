lines = open('input.txt').read().split('\n')

corners = [list(map(int, l.split(','))) for l in lines]

# part 1
max_area = 0
for i in range(0, len(corners) - 1):
    for j in range(i+1, len(corners)):
        area = (abs(corners[i][0] - corners[j][0]) + 1) * (abs(corners[i][1] - corners[j][1]) + 1)
        max_area = max(area, max_area)

print(max_area)

# part 2
def add_new_area(areas, x, y1, y2):
    ret_areas = []
    found = False
    while(len(areas)):
        a = areas.pop()
        if a[1] <= y1 <= a[2] and a[2] <= y2:
            ret_areas.append((a[0], a[1], y2))
            found = True
        elif y1 <= a[1] and a[1] <= y2 <= a[2]:
            ret_areas.append((a[0], y1, a[2]))
            found = True
        else:
            ret_areas.append((a[0], a[1], a[2]))
    if not found:
        ret_areas.append((x, y1, y2))

    return ret_areas

def get_rectangles(corners):
    corners = sorted(corners)
    prev_areas = []
    next_areas = []
    rectangles = []
    while(len(corners) > 0):
        prev_areas = next_areas
        next_areas = []
        # get all Y coordinates for this X
        y_coords = []
        x_coord = corners[0][0]
        while(len(corners) > 0 and corners[0][0] == x_coord):
            a = corners.pop(0)
            y_coords.append(a[1])
        if len(prev_areas) == 0:
            # if this is the first X coordinate
            for i in range(0, len(y_coords), 2):
                next_areas.append((x_coord, y_coords[i], y_coords[i + 1]))
        else:
            # if this is not the first X coordinate
            y_coord_to_remove = []
            while(len(prev_areas) > 0):
                area = prev_areas.pop()
                ay1 = area[1]
                ay2 = area[2]
                found = False
                add_area = False
                for i in range(0, len(y_coords), 2):
                    if ay1 == y_coords[i] and ay2 == y_coords[i + 1]:
                        found = True
                        y_coord_to_remove.append(y_coords[i])
                        y_coord_to_remove.append(y_coords[i+1])
                    elif ay1 == y_coords[i] and y_coords[i + 1] < ay2:
                        ay1 = y_coords[i + 1]
                        found = True
                        add_area = True
                        y_coord_to_remove.append(y_coords[i])
                        y_coord_to_remove.append(y_coords[i+1])
                    elif ay1 < y_coords[i] and y_coords[i + 1] == ay2:
                        ay2 = y_coords[i]
                        found = True
                        add_area = True
                        y_coord_to_remove.append(y_coords[i])
                        y_coord_to_remove.append(y_coords[i+1])
                    elif ay1 == y_coords[i + 1]:
                        ay1 = y_coords[i]
                        found = True
                        add_area = True
                        y_coord_to_remove.append(y_coords[i])
                        y_coord_to_remove.append(y_coords[i+1])
                    elif ay2 == y_coords[i]:
                        ay2 = y_coords[i + 1]
                        found = True
                        add_area = True
                        y_coord_to_remove.append(y_coords[i])
                        y_coord_to_remove.append(y_coords[i+1])
                    elif ay1 < y_coords[i] and y_coords[i + 1] < ay2:
                        found = True
                        add_area = False
                        next_areas.append((x_coord, ay1, y_coords[i]))
                        next_areas.append((x_coord, y_coords[i+1], ay2))
                        y_coord_to_remove.append(y_coords[i])
                        y_coord_to_remove.append(y_coords[i+1])

                if not found:
                    next_areas.append((area[0], area[1], area[2]))
                else:
                    rectangles.append((area[0], x_coord, area[1], area[2]))
                    if add_area:
                        next_areas = add_new_area(next_areas, x_coord, ay1, ay2)

            for y in y_coord_to_remove:
                if y in y_coords:
                    y_coords.remove(y)
            for i in range(0, len(y_coords), 2):
                next_areas.append((x_coord, y_coords[i], y_coords[i + 1]))
    
    return rectangles

def construct_map():
    map = [[0] * (x_points_num - 1) for i in range(y_points_num - 1)]
    for r in rectangles:
        x1, x2, y1, y2 = r
        x_min = x_max = 0
        y_min = y_max = 0
        for x in range(0, x_points_num - 1):
            if x_points[x] == x1:
                x_min = x
            if x_points[x] < x2:
                x_max = x
        for y in range(0, y_points_num - 1):
            if y_points[y] == y1:
                y_min = y
            if y_points[y] < y2:
                y_max = y
        for x in range(x_min, x_max+1):
            for y in range(y_min, y_max+1):
                map[y][x] = 1
    return map

def area_in_rectangles(x1, x2, y1, y2):
    if x1 > x2:
        tmp = x1
        x1 = x2
        x2 = tmp
    if y1 > y2:
        tmp = y1
        y1 = y2
        y2 = tmp
    
    x_min = x_max = 0
    y_min = y_max = 0
    for x in range(0, x_points_num):
        if x_points[x] == x1:
            x_min = x
        if x_points[x] < x2:
            x_max = x
    for y in range(0, y_points_num):
        if y_points[y] == y1:
            y_min = y
        if y_points[y] < y2:
            y_max = y
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            if map[y][x] == 0:
                return False
    return True

x_points = sorted(list(set([c[0] for c in corners])))
y_points = sorted(list(set([c[1] for c in corners])))
x_points_num = len(x_points)
y_points_num = len(y_points)

rectangles = get_rectangles(corners)
map = construct_map()

max_area = 0
for i in range(0, len(corners) - 1):
    for j in range(i+1, len(corners)):
        area = (abs(corners[i][0] - corners[j][0]) + 1) * (abs(corners[i][1] - corners[j][1]) + 1)
        if area > max_area:
            if area_in_rectangles(corners[i][0], corners[j][0], corners[i][1], corners[j][1]):
                max_area = area

print(max_area)