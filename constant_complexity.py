"""
O(1)
"""

nums = [2, 4, 5, 56, 3, 99]


def get_num(lst):
    if lst[0] % 2 == 0:
        return 'Even'
    return 'Odd'


print(get_num(nums))
