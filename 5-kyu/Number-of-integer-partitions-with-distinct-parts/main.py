# Number of integer partitions with distinct parts

# 5 -> 3
# [5], [4,1], [3,2]

# 10 -> 10
# [10], [9, 1], [8, 2], [7, 3], [6, 4], [5, 5], [7, 2, 1], [6, 3, 1], [5, 4, 1], [5, 3, 2]


def search_combo(current_number, n, count):
    for i in range(n-1, 0, -1):
        if current_number + i == n:
            count += 1
        elif current_number + i < n:
            search_combo(current_number + i, n, count)


def partitions(n):
    """Number of integer partitions with distinct parts"""

    count = 0

    for i in range(n, 0, -1):
        search_combo(i, n, count)

    return count


res = partitions(10)
print(res)