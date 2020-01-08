def even_number(arr):
    dict1 = {}
    for i,val in enumerate(arr):
        dict1[i] = len(str(val))
    cnt = 0
    for i in dict1:
        if(dict1[i]%2 == 0):
            cnt += 1
    return cnt 
print(even_number([12,23,345,123,45]))