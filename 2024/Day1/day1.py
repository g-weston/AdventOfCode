with open(file='Day1/task1_data.txt', mode='r') as f1:
    lines = f1.readlines()

list_one = []
list_two = []
for line in lines:
    line.replace('\n', '')
    parts = line.split()
    list_one.append(int(parts[0]))
    list_two.append(int(parts[1]))

# Task 1 - find the total difference between sorted lists

list_one.sort()
list_two.sort()
tot_dist = 0

for a, b in zip(list_one, list_two):
    print(a,  b)
    tot_dist += abs((a - b))

print(tot_dist)


# Task 2 - find a similarity score based on how many times a variable comes up in each list

tot_sim = 0

for a in list_one:
    hits = 0
    for b in list_two:
        if a == b:
            hits += 1
    
    tot_sim += a * hits

print(tot_sim)