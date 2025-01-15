lines = open('input.txt').read().split('\n')

# part 1
flipped_tiles = list()
def flip_tile(tile):
    global flipped_tiles
    x, y = position(tile) 
    if (x, y) in flipped_tiles:
        flipped_tiles.remove((x, y))
    else:
        flipped_tiles.append((x, y))

def position(tile):
    if tile == '':
        return 0.0, 0.0
    if tile[0] == 'e':
        x, y = position(tile[1:])
        return x - 1, y
    if tile[0] == 'w':
        x, y = position(tile[1:])
        return x + 1, y
    if tile[0:2] == 'se':
        x, y = position(tile[2:])
        return x - 0.5, y + 1
    if tile[0:2] == 'sw':
        x, y = position(tile[2:])
        return x + 0.5, y + 1
    if tile[0:2] == 'ne':
        x, y = position(tile[2:])
        return x - 0.5, y - 1
    if tile[0:2] == 'nw':
        x, y = position(tile[2:])
        return x + 0.5, y - 1
    
for line in lines:
    flip_tile(line)
print(len(flipped_tiles))

# part 2