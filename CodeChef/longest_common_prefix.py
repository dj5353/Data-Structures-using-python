def longest_common_prefix(s):
    if not s:
        return ""
    z = sorted(s)
    for i in range(len(z[0])):
        for string in (z[1:]):
            if z[0][i] != string[i] or i >= len(string):
                return z[0][:i]
    return z[0]

        
    

print(longest_common_prefix(["flower","flight","flow"]))
print(longest_common_prefix(["rat","dog","dot"]))
print(longest_common_prefix(["aaa","aa","aaa"]))
