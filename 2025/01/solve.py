lines = open('input.txt').read().splitlines()

position = 50
prev_position = 50
at_zero = 0
passed_zero = 0

for line in lines:
    dir = line[:1]
    num = int(line[1:])
    passed_zero += num // 100
    num = num % 100

    if dir == 'L':
        position -= num
    elif dir == 'R':
        position += num

    if prev_position != 0:
        if position != position % 100 or position == 0:
            passed_zero += 1
    position = position % 100
    if position == 0:
        at_zero += 1
    prev_position = position

# part 1
print(at_zero)

# part 2
print(passed_zero)
