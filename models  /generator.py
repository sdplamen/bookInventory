def gen_password():
    from random import choice
    from string import ascii_letters, digits, punctuation
    return ''.join([choice(ascii_letters+digits+punctuation) for _ in range(20)])
