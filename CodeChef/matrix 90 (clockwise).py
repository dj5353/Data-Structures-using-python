#for matrix 90 degree clockwise rotation
#reverse matrix all column wise
#and transpose the matrix
def matrix_rotate(m):
    print("matrix before rotation")
    for i in m:
        print(i)
    #matrix reverse all columns
    m.reverse()
    #transpose of matrix
    for row in range(len(m)):
        for col in range(row):
            m[row][col],m[col][row] = m[col][row],m[row][col]
    print("Matrix after rotation")
    for j in m:
        print(j)
matrix_rotate([[1,2,3], [4,5,6],[7,8,9]])