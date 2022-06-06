# Number of integer partitions

def task(result, lst, n):
    last_lst = lst
    while 1 in last_lst:
        ind = lst.index(1)
        lst[ind] -= 1
        for i in range(n - 1, ind, -1):
            lst[i] += 1
            sort_lst = tuple(lst)
            if sort_lst not in result:
                result.add(sort_lst)
                result |= task(result, sorted(lst), n)
            lst[i] -= 1

    return result


def partitions(n):
    """define a function which returns the number of integer partitions of n"""
    res = task(set(), [1] * n, n)
    return len(res) + 1


res = partitions(5)
print(res)
