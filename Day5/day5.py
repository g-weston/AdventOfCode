from copy import deepcopy as dc
page_order = []
updates = []

with open(file='Day5/day5_data.txt', mode='r') as f1:
    for line in f1:
        if '|' in line:
            page_order.append(line.strip('\n').split('|'))
        elif ',' in line:
            updates.append(line.strip('\n').split(','))

def check_rules(update):
    passing = True
    out_rule = []
    for rule in page_order:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[1]) < update.index(rule[0]):
                passing = False
                out_rule = rule
                break
    return passing, out_rule

# Task 1 - find the lists which don't obey the ordering and return the sum of the middle numbers
def part_one():
    count = 0
    broken_updates = []
    for update in updates:
        if check_rules(update)[0]:
            count += int(update[int((len(update) - 1) / 2)])
        else:
            broken_updates.append(update)
    return count, broken_updates

print(part_one()[0])


# Task 2 - find the lists which don't obey the ordering, sort them correctly and return the middle number of these
def part_two():
    count = 0
    broken_updates = part_one()[1]
    for update in broken_updates:
        temp_update = update
        passing, rule = check_rules(temp_update)
        while not passing:
            pos_a = temp_update.index(rule[1])
            pos_b = temp_update.index(rule[0])
            temp_update[pos_a] = rule[0]
            temp_update[pos_b] = rule[1]
            passing, rule = check_rules(temp_update)
        count += int(temp_update[int((len(temp_update) - 1) / 2)])

    return count

print(part_two())
