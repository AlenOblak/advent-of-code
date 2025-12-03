lines = open('input.txt').read().split('\n')

def max_jolt(battery, length):
    if length == 1:
        return max(battery)

    max_num = max(battery[:-(length-1)])
    pos = battery.find(max_num)
    return max_num + max_jolt(battery[pos+1:], length - 1)
    
num_1 = 0
num_2 = 0
for bat in lines:
    num_1 += int(max_jolt(bat, 2))
    num_2 += int(max_jolt(bat, 12))

print(num_1)
print(num_2)