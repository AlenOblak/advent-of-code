lines = open('input.txt').read().split('\n')

# part 1
devices = {}
for l in lines:
    a, b = l.split(': ') 
    b = b.split(' ')
    devices[a] = b

memory = {}
def num_paths(device, to):

    if device in memory:
        return memory[device]
    if device == to:
        return 1

    result = 0
    if device in devices:
        for d in devices[device]:
            result += num_paths(d, to)
    memory[device] = result
    return result

print(num_paths('you', 'out'))

# part 2
memory = {}
num1 = num_paths('svr', 'fft')

memory = {}
num2 = num_paths('fft', 'dac')

memory = {}
num3 = num_paths('dac', 'out')

print(num1 * num2 * num3)