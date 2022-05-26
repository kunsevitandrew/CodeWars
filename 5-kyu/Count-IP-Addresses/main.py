# Count IP Addresses

def ips_between(start, end):
    # TODO
    arr1 = list(map(int, start.split(".")))
    arr2 = list(map(int, end.split(".")))
    sum1 = 0
    sum2 = 0
    for i in [3, 2, 1, 0]:
        sum1 += arr1[i] * 256 ** (3 - i)
        sum2 += arr2[i] * 256 ** (3 - i)

    return sum2 - sum1


res = ips_between("20.0.0.10", "20.0.1.0")
print(res)

# Solutions from site:

# var-1
# from ipaddress import ip_address
#
# def ips_between(start, end):
#     return int(ip_address(end)) - int(ip_address(start))

# var-2
# def ips_between(start, end):
#     return sum((int(b) - int(a)) * 256 ** i for i, (b, a) in enumerate(reversed(zip(end.split('.'), start.split('.')))))