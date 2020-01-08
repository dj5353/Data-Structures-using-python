import collections
def Anagrams(strs):
    sort = []
    for i in strs:
        a = (sorted(i))
        b = "".join(map(str,a))
        sort.append(b)
    dict1 = collections.Counter(sort)
    return dict1


print(Anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
a = ['s','v']
b = " ".join(map(str, a))
print(b)
