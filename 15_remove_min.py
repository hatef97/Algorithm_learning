"""
    [4, 5, 2, 7, -2, 8, 1] => -2
"""


def remove_min(stack):
    storage_stack = []
    if len(stack) == 0:
        return stack

    min_list = stack.pop()
    stack.append(min_list)
    for i in range(len(stack)):
        val = stack.pop()
        if val <= min_list:
            min_list = val
        storage_stack.append(val)

    for i in range(len(storage_stack)):
        val = storage_stack.pop()
        if val != min_list:
            stack.append(val)

    return min_list


print(remove_min([4, 5, 2, 7, -2, 8, 1]))
