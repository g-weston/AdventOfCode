import re

with open(file='Day4/day4_data.txt', mode='r') as f1:
    lines = f1.readlines()
matrix = [list(line.strip('\n')) for line in lines]

# Task 1 - word search to find XMAS
def part1():
    hits = 0
    for a, line in enumerate(matrix):
        for b, letter in enumerate(line):
            if letter == 'X':
                curr_pos = [a, b]

                # north
                if b >= 3:
                    test_string = matrix[a][b] + matrix[a][b-1] + matrix[a][b-2] + matrix[a][b-3]
                    if test_string == 'XMAS':
                        hits += 1

                # north east
                if b >= 3 and (a <= len(line) - 4):
                    test_string = matrix[a][b] + matrix[a+1][b-1] + matrix[a+2][b-2] + matrix[a+3][b-3]
                    if test_string == 'XMAS':
                        hits += 1

                # east
                if a <= len(line) - 4:
                    test_string = matrix[a][b] + matrix[a+1][b] + matrix[a+2][b] + matrix[a+3][b]
                    if test_string == 'XMAS':
                        hits += 1

                # south east
                if (a <= len(line) - 4) and (b <= len(matrix) - 4):
                    test_string = matrix[a][b] + matrix[a+1][b+1] + matrix[a+2][b+2] + matrix[a+3][b+3]
                    if test_string == 'XMAS':
                        hits += 1

                # south
                if (b <= len(matrix) - 4):
                    test_string = matrix[a][b] + matrix[a][b+1] + matrix[a][b+2] + matrix[a][b+3]
                    if test_string == 'XMAS' or test_string =='SAMX':
                        hits += 1

                # south west
                if (b <= len(matrix) - 4) and a >= 3:
                    test_string = matrix[a][b] + matrix[a-1][b+1] + matrix[a-2][b+2] + matrix[a-3][b+3]
                    if test_string == 'XMAS':
                        hits += 1

                # west
                if a >= 3:
                    test_string = matrix[a][b] + matrix[a-1][b] + matrix[a-2][b] + matrix[a-3][b]
                    if test_string == 'XMAS':
                        hits += 1

                # north west
                if a >= 3 and b >= 3:
                    test_string = matrix[a][b] + matrix[a-1][b-1] + matrix[a-2][b-2] + matrix[a-3][b-3]
                    if test_string == 'XMAS':
                        hits += 1
    
    return hits

# Task 2 - identify X-MAS crosses ie M.M/.A./S.S
def part2():
    hits = 0
    for a, line in enumerate(matrix):
        for b, letter in enumerate(line):
            if letter == 'A' and (0<a<len(matrix)-1) and (0<b<len(line)-1):
                test_string = matrix[a-1][b-1] + matrix[a-1][b+1] + matrix[a+1][b-1] + matrix[a+1][b+1]
                hits += len(re.findall(r'MSMS|SMSM|MMSS|SSMM', test_string))
    return hits


print(part1())
print(part2())
