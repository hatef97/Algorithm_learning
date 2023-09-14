"""
    rotate("hello", 2) => "llohe"
    rotate("hello", 5) => "hello"
    rotate("hello", 6) => "elloh"
    rotate("hello", 7) => "llohe"
"""


def rotate(string, num):
    new_str = string + string
    if num <= len(string):
        return new_str[num:num + len(string)]
    else:
        return new_str[num - len(string):num]


print(rotate("hello", 2))
print(rotate("hello", 5))
print(rotate("hello", 6))
print(rotate("hello", 7))
