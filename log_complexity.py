"""
O(log n)
"""

nums = [1, 3, 5, 8, 12, 34, 55, 99]


def get_num(lst, elm):
    for n in lst:
        if n == elm:
            return lst.index(n)


print(get_num(nums, 12))
