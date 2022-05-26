# Fibo akin

def length_sup_u_k(n, k):
    # u[i]=u[u[i-1]]+u[u[i0-2]]
    u = [1, 1, 1]
    for i in range(3, n + 1):
        u.append(u[i - u[i - 1]] + u[i - u[i - 2]])

    count = 0
    for i in range(0, n+1):
        if u[i] >= k:
            count += 1

    return count


def comp(n):
    count = 0
    u = [1, 1, 1]
    for i in range(3, n + 1):
        u.append(u[i - u[i - 1]] + u[i - u[i - 2]])

    for i in range(3, n + 1):
        if u[i] < u[i - 1]:
            count += 1
    return count


# res1 = length_sup_u_k(20, 2)
# res2 = comp(23)
# print(res1)
# print(res2)

# library
# import itertools
