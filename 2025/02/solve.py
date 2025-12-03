file = open('input.txt')

line = file.readline()
id_list = line.split(',')

# part 1
invalid = 0
for ids in id_list:
    a, b = ids.split('-')
    for i in range(int(a), int(b) + 1):
        i_str = str(i)
        len_i = len(i_str)
        len_i_remain = len_i % 2
        if len_i_remain != 0:
            continue
        l = int(len_i / 2)
        if i_str[:l] == i_str[l:]:
            invalid += i

print(invalid)

# part 2
len_to_check = {1: [], 2: [1], 3: [1], 4:[1,2], 5:[1], 6:[1,2,3], 7:[1], 8:[1,2,4], 9:[1,3], 10:[1,2,5]}
invalid = 0

for ids in id_list:
    a, b = ids.split('-')
    for i in range(int(a), int(b) + 1):
        i_str = str(i)
        len_i = len(i_str)
        if len_i not in len_to_check:
            print(f'Please define lengths for {len_i}')
            exit()
        for l in len_to_check[len_i]:
            if len(set([i_str[i:i+l] for i in range(0, len(i_str), l)])) == 1:
                invalid += i
                break

print(invalid)