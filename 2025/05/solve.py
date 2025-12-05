lines = open('input.txt').read().split('\n\n')

fresh = []
for l in lines[0].split('\n'):
    a, b = l.split('-')
    fresh.append([int(a), int(b)])
ingredients = [int(l) for l in lines[1].split('\n')]

# part 1
result = 0
for i in ingredients:
    for f in fresh:
        if i >= f[0] and i <= f[1]:
            result += 1
            break

print(result)

# part 2
def pair_to_merge(fresh):
    for i in range(0, len(fresh)-1):
        for j in range(i + 1, len(fresh)):
            if fresh[i][0] <= fresh[j][0] and fresh[i][1] >= fresh[j][0]:
                return True, i, j
            if fresh[i][0] >= fresh[j][0] and fresh[i][1] <= fresh[j][1]:
                return True, i, j
            if fresh[i][0] >= fresh[j][0] and fresh[i][0] <= fresh[j][1]:
                return True, i, j
    return False, 0, 0

need_merge = True
while need_merge:
    need_merge, i, j = pair_to_merge(fresh)
    if need_merge:
        a = fresh.pop(i)
        b = fresh.pop(j-1)
        fresh.append([min(a[0], b[0]), max(a[1], b[1])])

result = sum([f[1]-f[0]+1 for f in fresh])

print(result)