# Hamming Numbers


def generation_humming(n):
    """Generating list of humming numbers while len(lst) <= n"""
    lst = [1]
    for i in lst:
        for j in [2, 3, 5]:
            numb = i * j
            if numb not in lst:
                lst.append(numb)

        if len(lst) >= n:
            break

    return sorted(lst)

lst = generation_humming(1000)

# def hamming(n):
#     """Returns the nth hamming number"""
#     return lst[n - 1]


# # test
# res = hamming(95)
# print(res)

# other solutions
def hamming(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]

# test
res = hamming(95)
print(res)
