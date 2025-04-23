from copy import deepcopy as dc

with open(file='Day2/day2_data.txt', mode='r') as f1:
    lines = f1.readlines()

reports = [a.strip('\n').split() for a in lines]

# Task 1 - find the number of safe reports if all values either increase or decrease in the report by a value between 1 and 3
safe_reports = 0
for report in reports:
    temp_diff = []
    report = [int(a) for a in report]
    for i in range(len(report) - 1):
        temp_diff.append(report[i+1] - report[i])
    
    if all(0<i<4 for i in temp_diff):
        safe_reports += 1
    elif all(-4<i<0 for i in temp_diff):
        safe_reports += 1

print(safe_reports)


# Task 2 - find the number of safe reports if a max penalty of 1 is applied

def calc_diffs(report):
    temp_diff = []
    for i in range(len(report) - 1):
        temp_diff.append(report[i+1] - report[i])
    return temp_diff

safe_reports = 0
for i, report in enumerate(reports):
    print(f'Report num: {i}')
    report = [int(a) for a in report]
    temp_diff = calc_diffs(report)
    if all(0<i<4 for i in temp_diff):
        safe_reports += 1
    elif all(-4<i<0 for i in temp_diff):
        safe_reports += 1
    else:
        print(temp_diff)
        num_pos_diff = sum(x in range(1, 4) for x in temp_diff)
        num_neg_diff = sum(x in range(-3, 0) for x in temp_diff)
        if num_pos_diff > num_neg_diff:
            direction = 'U'
        elif num_neg_diff > num_pos_diff:
            direction = 'D'
        else:
            continue
        
        error = 0
        
        for j in range(len(report) - 1):
            if error == 0:
                diff = report[j+1] - report[j]

                if direction == 'U':
                    if diff<1 or diff>3:
                        error += 1
                elif direction == 'D':
                    if diff<-3 or diff>-1:
                        error += 1

                if error == 1:
                    for idx in range(j-1, j+2):
                        if not idx < 0 and not idx >= len(report):
                            test_report = dc(report)
                            del test_report[idx]
                            test_diff = calc_diffs(test_report)
                            if all(0<a<4 for a in test_diff):
                                safe_reports += 1
                                print(f'Idx removed: {idx+1}')
                                break
                            elif all(-4<a<0 for a in test_diff):
                                safe_reports += 1
                                print(f'Idx removed: {idx+1}')
                                break
                    break





print(safe_reports)