# Is my friend cheating?

# time error in CodeWars

def remov_nb(n):
    answer_lst = []
    sm = sum((i for i in range(1, n+1)))

    for i in range(1,n+1):
        for j in range(i, n+1):
            if sm - (i + j) == i*j:
                answer_lst.append((i, j))
                answer_lst.append((j, i))

    return sorted(answer_lst, key=lambda x: x[0])


# lst = [(1, 2), (12, 4), (4, 123), (2, 3), (-12, 44), (-100, 2)]
res = remov_nb(26)
print(res)
