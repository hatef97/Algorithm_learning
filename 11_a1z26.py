"""
    amir <==> [1, 13, 9, 18]
"""


def encode(plain):
    return [ord(elm) - 96 for elm in plain]


def decode(encode):
    return "".join(chr(elm + 96) for elm in encode)
