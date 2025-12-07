lines = open('input.txt').read().split('\n')

cols = len(lines[0])
beams = dict.fromkeys(range(cols), 0)
beams[lines[0].find('S')] = 1
split = 0
for l in range(1, len(lines) - 1):
    new_beams = dict.fromkeys(range(cols), 0)
    for b in range(0, cols):
        if lines[l][b] == '^' and beams[b] != 0:
            split = split + 1
            new_beams[b-1] = new_beams[b-1] + beams[b]
            new_beams[b+1] = new_beams[b+1] + beams[b]
        else:
            new_beams[b] = new_beams[b] + beams[b]
    beams = new_beams

# part 1
print(split)
# part 2   
print(sum(beams.values()))