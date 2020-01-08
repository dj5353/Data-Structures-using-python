#for matrix 180 degree anticlockwise rotation
#reverse matrix all column wise and than rowwise

def matrix_rotate(m):
    l = []
    for _ in range(len(m)):
        l = l + [m[_][::-1]]
    l.reverse()
    for i in l:
        print(i)
matrix_rotate([[1,2,3],[4,5,6],[7,8,9]])
