dict1 = {}
for ind,val in enumerate("ab"):
    if(val in dict1):
        dict1[val] += 1
    else:
        dict1[val] = 1
print(dict1)