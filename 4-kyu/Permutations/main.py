# Permutations

# abcd (4! = 24): abdc, adbc, dabc, dacb, dcab, cdab, cdba, cbda, bcda, bcad, bacd --- BAD METHOD
# 1234: 1243, 1423, 1432,

def swap_symbols(text, index):
    return text[:index - 1] + text[index] + text[index - 1] + text[index+1:]


def permutations(text):
    lst_text=list(text)
    result = set()
    for i in range(len(text)):
        pass