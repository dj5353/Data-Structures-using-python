
''''
def spiral_matrix(matrix):
    col_end = len(matrix[0])-1
    row_end = len(matrix)-1
    col_begin = 0
    row_begin = 0
    while (row_begin <= row_end and col_begin <= col_end):
        for i in range(col_begin,col_end+1):
            print(matrix[row_begin][i])
        row_begin += 1
        for i in range(row_begin,row_end+1):
            print(matrix[i][col_end])
        col_end -= 1
        if(row_begin <= row_end):
            for i in range(col_end,col_begin-1,-1):
                print(matrix[row_end][i])
            row_end -= 1
        
        if (col_end <= col_begin):
            for i in range(row_end,row_begin-1,-1):
                print(matrix[col_begin][i])
            col_begin += 1
            
        

spiral_matrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

l = [[1,2,3,4,5],[4,5,6,4,5],[7,8,9,4,5]]


'''
def spiral_matrix_2(matrix):
    row_begin = 0
    col_begin = 0
    row_end = len(matrix)-1 
    col_end = len(matrix[0])-1
    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin,col_end+1):
            print(matrix[row_begin][i])
        row_begin += 1
        for j in range(row_begin,row_end+1):
            print(matrix[j][col_end])
        col_end -= 1
        if (row_begin <= row_end):
            for i in range(col_end,col_begin-1,-1):
                print(matrix[row_end][i])
        row_end -= 1
        if (col_begin <= col_end):
            for i in range(row_end,row_begin-1,-1):
                print(matrix[col_begin][i])
        col_begin += 1

spiral_matrix_2([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])