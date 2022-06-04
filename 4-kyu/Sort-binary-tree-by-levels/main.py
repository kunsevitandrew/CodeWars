# Sort binary tree by levels

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def left_order(node, dct, level=0):
    if node is not None:
        if level not in dct.keys():
            dct[level] = []
        dct[level].append(node.value)
        left_order(node.left, dct, level + 1)
        left_order(node.right, dct, level + 1)


def tree_by_levels(node):
    # I'm realize dict of lists
    dct = {i: [] for i in range(1000)}
    lst = []
    i = 0

    left_order(node, dct)

    while dct[i] != []:
        for elem in dct[i]:
            lst.append(elem)
        i += 1

    return lst


nd_test = Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)
res = tree_by_levels(nd_test)
print(res)

# other variants:

# 1)
# from collections import deque
#
# def tree_by_levels(node):
#     if not node:
#         return []
#     res, queue = [], deque([node,])
#     while queue:
#         n = queue.popleft()
#         res.append(n.value)
#         if n.left is not None:
#             queue.append(n.left)
#         if n.right is not None:
#             queue.append(n.right)
#     return res

# 2)
# def tree_by_levels(node):
#     p, q = [], [node]
#     while q:
#         v = q.pop(0)
#         if v is not None:
#             p.append(v.value)
#             q += [v.left,v.right]
#     return p if not node is None else []
