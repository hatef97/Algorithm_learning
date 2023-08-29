"""
    foo, bar => False
    foo, bee => True
"""


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    dict = {}
    set_val = set()
    for i in range(len(s)):
        if s[i] not in dict:
            if t[i] in set_val:
                return False
            dict[s[i]] = t[i]
            set_val.add(t[i])
        else:
            if dict[s[i]] != t[i]:
                return False
    return True


print(is_isomorphic('good', 'mood'))
