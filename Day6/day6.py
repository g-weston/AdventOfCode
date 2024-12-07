
dataset = []
with open(file='Day6/day6_data.txt', mode='r') as f1:
    for line in f1:
        dataset.append(list(line.strip('\n')))


visited_positions = []

def move(curr_pos, cursor):
    end = False
    #cursor = dataset[curr_pos[0], curr_pos[1]]
    match cursor:
        case '^':
            if curr_pos[0] - 1 < 0:
                end = True
            elif dataset[curr_pos[0] - 1][curr_pos[1]] == '#':
                cursor = '>'
            else:
                curr_pos = [curr_pos[0] - 1, curr_pos[1]]

        case '>':
            if curr_pos[1] + 1 > len(dataset[0]) - 1:
                end = True
            elif dataset[curr_pos[0]][curr_pos[1] + 1] == '#':
                cursor = '~'
            else:
                curr_pos = [curr_pos[0], curr_pos[1] + 1]

        case '<':
            if curr_pos[1] - 1 < 0:
                end = True
            elif dataset[curr_pos[0]][curr_pos[1] - 1] == '#':
                cursor = '^'
            else:
                curr_pos = [curr_pos[0], curr_pos[1] - 1]

        case '~':
            if curr_pos[0] + 1 > len(dataset) - 1:
                end = True
            elif dataset[curr_pos[0] + 1][curr_pos[1]] == '#':
                cursor = '<'
            else:
                curr_pos = [curr_pos[0] + 1, curr_pos[1]]
    
    if curr_pos not in visited_positions:
        visited_positions.append(curr_pos)

    return end, cursor, curr_pos


for i, line in enumerate(dataset):
    if '^' in line:
        curr_pos = [i, line.index('^')]
        visited_positions.append(curr_pos)
        break


end, cursor, curr_pos = move(curr_pos, cursor='^')
while not end:
    end, cursor, curr_pos = move(curr_pos, cursor=cursor)
    print(curr_pos)

print(len(visited_positions))

