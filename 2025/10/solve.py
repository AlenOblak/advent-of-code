from z3 import *

lines = open('input.txt').read().split('\n')

# part 1
machines = []
for l in lines:
    m = l.split(' ')
    indicator = m[0][1:-1]
    wiring = []
    for w in [a[1:-1] for a in m[1:-1]]:
        wiring.append(list(map(int, w.split(','))))
    joltage = m[-1][1:-1]
    joltage = list(map(int, joltage.split(',')))
    
    machines.append((indicator, wiring, joltage))

def generate_states(state, machine):
    result = []
    for buttons in machine[1]:
        new_state = ''
        for i in range(0, len(state)):
            if i in buttons:
                if state[i] == '.':
                    new_state += '#'
                else:
                    new_state += '.'
            else:
                new_state += state[i]
        result.append(new_state)
    return result

def solve_machine(machine):
    states = [['.' * len(machine[0]), 0]]
    while len(states) > 0:
        s = states.pop(0)
        new_states = generate_states(s[0], machine)
        for n in new_states:
            if n == machine[0]:
                return s[1] + 1
            exist = False
            for ex in states:
                if ex[0] == n:
                    exist = True
                    break
            if not exist:
                states.append([n, s[1] + 1])

print(sum([solve_machine(m) for m in machines]))

# part 2
def solve_machine_2(machine):
    keys = 'abcdefghijklm'

    num_buttons = len(machine[1])
    num_equations = len(machine[2])
    vars = [keys[ii] for ii in range(0, num_buttons)]
    ss = Solver()

    a, b, c, d, e, f, g, h, i, j, k, l, m = Ints('a b c d e f g h i j k l m')
    equations = ['' for _ in range(0, num_equations)] 
    for ii in range(0, num_buttons):
        for jj in machine[1][ii]:
            equations[jj] += f'{keys[ii]}+'
    for ii in range(0, num_equations):
        equations[ii] = equations[ii][:-1] + f'=={machine[2][ii]}'
    for x in keys:
        equations.append(f'{x}>=0')
    for ee in equations:
        ss.add(eval(ee))

    init_step = max(machine[2])
    ss.push()
    ss.add(eval('+'.join(vars) + '==' + str(init_step)))
    result = ss.check()
    while result != sat:
        ss.pop()
        init_step += 1
        ss.push()
        ss.add(eval('+'.join(vars) + '==' + str(init_step)))
        result = ss.check()
    model = ss.model()
    
    return(sum([int(model[mo].as_long()) for mo in model]))

print(sum([solve_machine_2(m) for m in machines]))