# Sum of Intervals

def sum_of_intervals(intervals):
    mx = max(intervals, key=lambda x: x[1])[1]
    mn = min(intervals)[0]

    new_intervals = [(i + mn, j + mn) for i, j in intervals]
    lst = [0] * (mx + abs(mn) + mx)

    for i, j in new_intervals:
        for ind in range(i, j):
            lst[ind] = 1

    return sum(lst)


data = [(1, 4), (7, 10), (3, 5)]
res = sum_of_intervals(data)
print(res)

# other variants:

# def sum_of_intervals(intervals):
#     result = set()
#     for start, stop in intervals:
#         for x in range(start, stop):
#             result.add(x)
#
#     return len(result)
