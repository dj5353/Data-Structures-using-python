#for matrix 180 degree anticlockwise rotation
#reverse matrix all column wise and than rowwise
def matrix_rotate(m):
    l = []
    k = []
    for col in range(len(m)) :
        l = l + [(m[col][::-1])]
    for num in (l[::-1]):
        print(num)
matrix_rotate([[1,2,3],[4,5,6],[7,8,9]])
