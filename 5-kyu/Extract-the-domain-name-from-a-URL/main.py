# Extract the domain name from a URL

# text-variant:
#
# import re
#
# def domain_name(url):
#     match = re.search(r"([htps/:]*?)w{,3}[.]*?(?P<site_url>[-\w]+)", url)
#     return match["site_url"]

def domain_name(arr):
    lst = arr.split("/")
    for word in lst:
        if word[:4] != "http" and word != "":
            if word[:4]=="www.":
                word = word[4:]

            return word.split(".")[0]


# text = "https://youtube.com"
text= "www.xakep.ru"
# text = "hyphen-site"

res = domain_name(text)

print(res)

# solutions from site:
# 1)
#
# def domain_name(url):
#     return url.split("//")[-1].split("www.")[-1].split(".")[0]

# 2)
# import re
# def domain_name(url):
#     return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

# 3)
# def domain_name(url):
#     url = url.replace('www.','')
#     url = url.replace('https://','')
#     url = url.replace('http://','')
#
#     return url[0:url.find('.')]

# 3)
# def domain_name(url):
#     from re import findall, VERBOSE
#
#     try:
#         url = findall("""\A
#                         (?: http
#                         s?
#                         ://)?         # matches http:// or https:// or nothing
#
#                         (?: www.)?    # matches www. or nothing
#
#                         ([- a-z]+)    # matches a sequence of letters and dashes
#
#                         (?: .com|.ru)     # matches either .com or .ru
#                         (?: [/ a-z]+)?    # matches a sequence or letters and slashes
#                         \Z""", url, VERBOSE)
#         return url[0]
#     except:
#         return "Invalid URL."