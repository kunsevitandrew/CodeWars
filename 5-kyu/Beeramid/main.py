# Beeramid

def beeramid(bonus, price):
    count = bonus // price
    sum_sq = 1
    n = 1
    while sum_sq < count:
        n += 1
        sum_sq += n ** 2

    return n if sum_sq==count else n-1


res = beeramid(21, 1.5)
print(res)


# solutions from a genius (most likely an Indian)
# def beeramid(bonus, price):
#     k = bonus // price
#     d = (3 * (11664*k*k - 3) ** .5 + 324 * k) ** (1/3)
#     n = (d/3 + 1/d - 1) / 2
#     return k>0 and int(n.real+1e-12)