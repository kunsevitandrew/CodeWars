# Permutations

# abcd (4! = 24): abdc, adbc, dabc, dacb, dcab, cdab, cdba, cbda, bcda, bcad, bacd --- BAD METHOD
# 1234: 1243, 1423, 1432,

def permutations(text):
    res = set()
    n = len(text)
    lst = list(text)
    used = [False] * (n + 1)

    def task(lst, used, n, text, index):
        nonlocal res
        if index == n:
            res.add("".join(lst))
        else:
            for i in range(n):
                if used[i]:
                    continue
                lst[index] = text[i]
                used[i] = True
                task(lst, used, n, text, index + 1)
                used[i] = False

    task(lst, used, n, text, 0)
    return res

# test
res = permutations("aabb")
print(res)

# other variants

# 1)
# import itertools
#
# def permutations(string):
#     return list("".join(p) for p in set(itertools.permutations(string)))

# 2)
# def permutations(string):
#     if len(string) == 1: return set(string)
#     first = string[0]
#     rest = permutations(string[1:])
#     result = set()
#     for i in range(0, len(string)):
#         for p in rest:
#             result.add(p[0:i] + first + p[i:])
#     return result
