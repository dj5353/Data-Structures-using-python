def linearSearch(a,n,search_value):
    for i in range(n):
        if a[i] == search_value:
            return i
    return -1


n = int(input("Enter the number of elements you want to insert"))
a = [None]*n
for i in range(n):
    a[i] = int(input("Enter the next element")) 
search_value = int(input("Enter the next element you want to search"))
index = linearSearch(a,n,search_value)
if(index == -1):
    print("Element {} is not present in the list".format(search_value))
else:
    print("Element {} is present at location  {} ".format(search_value,index))