"""
    [4, 7, 9, 2, 3, 6, 7] => [2, 3, 4, 6, 7, 7, 9]
"""


def bead_sort(seq):
    if any(not isinstance(x, int) or x < 0 for x in seq):
        raise TypeError("sequence must be list of non-negative integers")

    for _ in range(len(seq)):
        for i, (rod_upper, rod_lower) in enumerate(zip(seq, seq[1:])):
            if rod_upper > rod_lower:
                seq[i] -= rod_upper - rod_lower
                seq[i + 1] += rod_upper - rod_lower

    return seq


print(bead_sort([4, 7, 9, 2, 3, 6, 7]))
