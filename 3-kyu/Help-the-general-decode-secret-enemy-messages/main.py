# Help the general decode secret enemy messages.

# input data: atC5kcOuKAr! -> Hello World!

def encode(text):
    lst = []
    return lst


def decode(s):
    print(encode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(encode("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(encode("!@#$%^&*()_+-"))
    a, b, c = "", "", ""
    for w in "abcdefghijklmnopqrstuvwxyz":
        a += encode("" + w)[0]
        b += encode("_" + w)[1]
        c += encode("__" + w)[2]
    print(a)
    print(b)
    print(c)
    return s

