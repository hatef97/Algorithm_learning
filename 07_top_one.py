"""
[1, 2, 3, 2, 4, 1] => [1, 2]
"""


def top(arr):
    values = {}
    result = []
    f_val = 0

    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1

    f_val = max(values.values())

    for i in values.keys():
        if values[i] == f_val:
            result.append(i)
        else:
            continue

    return result


print(top([1, 2, 3, 2, 4, 1]))
