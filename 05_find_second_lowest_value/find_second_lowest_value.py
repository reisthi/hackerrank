students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

report = dict(students)

# get second lowest grade
second_lowest_key = sorted(report, key=report.get, reverse=False)[1:2]
second_lowest_value = report.get(''.join(second_lowest_key))

# make sure return multiple names if min values are the same

mult_values_list = list()
# for row in students:
# if row[1] == second_lowest_value:
# mult_values_list.append(row[0])  # appending names with same min value


for k, v in report.items():
    if v == second_lowest_value:
        mult_values_list.append(k)

# print name in alphabetical order
print(sorted(mult_values_list))


def sol(x):
    x = dict(x)
    sec_lowest_scores = list()

    low = sorted(x.values(), reverse=False)[1]

    for key, value in x.items():
        if value == low:
            sec_lowest_scores.append(key)
    return sec_lowest_scores
