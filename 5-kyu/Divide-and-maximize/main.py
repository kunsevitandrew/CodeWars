# Divide and maximize

def divide_and_multiply(arr):
    size = len(arr)
    degree = 0
    while True:
        d1 = degree
        for i in range(size):
            if arr[i] % 2 == 0:
                arr[i] //= 2
                degree += 1

        if d1 == degree:
            break

    max_number_index = arr.index(max(arr))
    arr[max_number_index] *= 2 ** degree

    return sum(arr) % 1000000007


res = divide_and_multiply([8, 123, 23])

print(res)

# variant from site:
# 1)
# def divide_and_multiply(n):
#     m = max((x for x in n if x%2), default=max(n))
#     n.remove(m)
#     s = 0
#     for x in n:
#         while x % 2 == 0:
#             x //= 2
#             m += m
#         s += x
#     return (s+m)%1_000_000_007
#
#
# 2)
# def divide_and_multiply(xs):
#     l2 = lambda m: len(bin(m).split('1')[-1])
#     ys = [n>>l2(n) for n in xs]
#     return ( sum(ys) + (max(ys)<<sum(map(l2, xs))) - max(ys) ) % (10 ** 9 + 7)
