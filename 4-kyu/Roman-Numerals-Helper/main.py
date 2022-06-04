# Roman Numerals Helper

pairs = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)]

# Compose dictionary with all pairs (roman, ordinary_numbers)

# dct_to_roman = {j: i for i, j in pairs}

dct_from_roman = dict(pairs)

new_pairs = []

for i in range(10):
    pass

new_pairs = []
for i in range(100):
    for key in dct_from_roman:
        if i >= dct_from_roman[key]

    print("-----", res)


# print(dct_from_roman)
# print(dct_to_roman)

class RomanNumerals:

    @staticmethod
    def to_roman(number):
        text = ""
        str_number = str(number)
        size = len(str_number)

        for i in range(size):
            res = number % 10
            number //= 10
            print(res * 10 ** i)

        return text

    @staticmethod
    def from_roman(roman_num):
        return 0


RomanNumerals.to_roman(2008)
