def selectionSort(a,n):
    for i in range(len(a)-1):
        minindex = i
        for j in range(i+1,len(a)):
            if(a[minindex]>a[j]):
                minindex=j
        if(i!=minindex):
            a[i],a[minindex] = a[minindex],a[i]
                
n = int(input("Enter the number of elements you want to insert"))
a = [None]*n
for i in range(n):
    a[i] = int(input("Enter the next element"))
selectionSort(a,n)
print(a)

