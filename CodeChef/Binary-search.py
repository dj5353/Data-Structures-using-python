def binarySearch(a,n,searchValue):
    first = 0
    last = n-1
    while(first<last):
        mid = (first + last)//2
        if(searchValue<a[mid]):
            last = mid-1
        elif(searchValue>a[mid]):
            first = mid+1
        else:
            return mid
    return -1
n = int(input("Enter the number of elements you want to insert"))
a = [None]*n
for i in range(n):
    a[i] = int(input("Enter the element"))
searchValue = int(input("Enter the value you want to search"))
index = binarySearch(a,n,searchValue)
if(index == -1):
    print("The element {} is not present in the list".format(searchValue))
else:
    print("The element {} is present at index {} in the list".format(searchValue,index))
