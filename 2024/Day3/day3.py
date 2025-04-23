import re

with open(file='Day3/day3_data.txt') as f1:
    lines = str(f1.readlines())


# Task 1 - find all the mul(x,y) statements and sum the output

test_lines = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

#mul(\d+,\d+)
hits = re.findall(pattern=r'mul\(\d+\,\d+\)', string=lines)

count = 0
for hit in hits:
    digits = re.findall(pattern=r'\d+', string=hit)
    count += int(digits[0]) * int(digits[1])

print(count)


# Task 2 - account for the do() and dont() statements

test_lines = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

hits = re.findall(pattern=r'do\(\)|don\'t\(\)|mul\(\d+\,\d+\)', string=lines)

task_two_count = 0

on = True
for i, hit in enumerate(hits):
    if hit == 'do()':
        on = True
    elif hit == 'don\'t()':
        on = False
    
    if on:
        if 'mul' in hit:
            digits = re.findall(pattern=r'\d+', string=hit)
            task_two_count += int(digits[0]) * int(digits[1])

print(task_two_count)