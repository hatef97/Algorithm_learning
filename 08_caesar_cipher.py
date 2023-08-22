from string import ascii_letters

word = input('Type your word:\n')
code = int(input('Type num:\n'))


def encrypt(string, key):
    alpha = ascii_letters
    result = ''

    for ch in string:
        if ch not in alpha:
            pass
        else:
            new_key = (alpha.index(ch) + key) % len(alpha)
            result += alpha[new_key]

    return result.lower()


def decrypt(string, key):
    key *= -1
    return encrypt(string, key)


word_code = encrypt(string=word, key=code)


def brute_force(string=word_code):
    alpha = ascii_letters
    key = 1
    brute_force_data = {}

    while key <= len(alpha):
        result = decrypt(string, key)
        brute_force_data[key] = result
        key += 1

    return brute_force_data


dycode = input(f"Your code is: '{word_code}'\n"
               f" Do you want to Hack the code?\n Type 'yes' or 'no':\n")
if dycode == 'yes':
    result_data = brute_force()

    for key, result in result_data.items():
        print(f"Key {key}: {result}")
        if result == word:
            print(f"Your word is: {result}")
            break

else:
    pass
