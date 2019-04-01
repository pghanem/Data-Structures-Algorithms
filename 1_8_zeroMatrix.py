def zeroMatrix(matrix):
    if (len(matrix) == 0): return False
    rows = len(matrix)
    cols = len(matrix[0])
    print(rows, cols)

    zeros = []
    
    for x in range(0, rows):
        for y in range(0, cols):
            if matrix[x][y] == 0:
                zeros.append([x,y])

    for zero in zeros:
        for x in range(0, cols):
            matrix[zero[0]][x] = 0

    for zero in zeros:
        for x in range(0, rows):
            matrix[x][zero[1]] = 0
        
    print(matrix)

    # run with zeroMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])
