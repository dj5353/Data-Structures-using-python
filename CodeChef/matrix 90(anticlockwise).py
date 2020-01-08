#for matrix 90 degree anticlockwise rotation
#and transpose the matrix
#reverse matrix all column wise

def matrix_rotate(m):
    print("Matrix before rotation")
    for i in (m):
        print(i)
    # Transpose matrix
    for row in range(len(m)):
        for col in range(row):
            m[row][col], m[col][row] = m[col][row], m[row][col]
    # Matrix reverse all columns
    m.reverse()
    print("matrix after rotation")
    for j in (m):
        print(j)
matrix_rotate([[1,2,3],[4,5,6],[7,8,9]])
