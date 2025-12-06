import math

lines = open('input.txt').read().split('\n')
rows = len(lines) - 1

# part 1
numbers = []
for l in lines:
    nums = l.split(' ')
    numbers.append([n for n in nums if n != ''])

result = 0
for i in range(0, len(numbers[0])):
    op = numbers[rows][i]
    current = int(numbers[0][i])
    for j in range(1, rows):
        if op == '*':
            current *= int(numbers[j][i])
        else:
            current += int(numbers[j][i])
    result += current

print(result)

# part 2
def calculate(op, numbers):
    if op == '*':
        return math.prod(numbers)
    elif op == '+':
        return sum(numbers)
    return 0

result = 0
op = ''
numbers = []
for i in range(0, len(lines[0])):
    if(lines[rows][i] != ' '):
        result += calculate(op, numbers)
        op = lines[rows][i]
        numbers = []

    number = ''
    for j in range(0, rows):
        number += lines[j][i]
    if number.strip() != '':
        numbers.append(int(number))    
result += calculate(op, numbers)

print(result)