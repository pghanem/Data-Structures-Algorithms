def rotatematrix(matrix):
    #for testing
    print(matrix)

    #if empty or not symmetrical return 
    if (len(matrix) == 0 or len(matrix) != len(matrix[0])): return False

    n = len(matrix)
    
    for layer in range (0, n//2):
        first = layer
        last = n - 1 - layer
        print('layer is: ' + str(layer))
        print('first is: ' + str(first))
        print('last is: ' + str(last))
        
        for i in range (first, last):
            offset = i - first
            print('i is: ' + str(i))
            print('offset is: ' + str(offset))
            
            # save the top
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last-offset][first]
            print(matrix)
            
            # bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]
            print(matrix)
            
            # right -> bottom
            matrix[last][last-offset] = matrix[i][last]
            print(matrix)
            
            # saved top -> right
            matrix[i][last] = top
            print(matrix)
            
    return True

# run rotatematrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
