"""
O(n)
"""

nums = [3, 4, 2, 55, 33, 765, 21]


def get_num(lst):
    max_num = lst[0]
    for n in lst:
        if n > max_num:
            max_num = n
    return max_num


print(get_num(nums))

