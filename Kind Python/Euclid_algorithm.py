def is_isolate(array,i,j):
    
    N = len(array)
    
    matrix = [[0] * (N + 2)] + [[0] + row[:] + [0] for row in array] + [[0] * (N + 2)]
    
    i+=1
    j+=1
    
    sum = 0
    for i_check in range(i-1,i+2):
        for j_check in range(j-1,j+2):
            sum+=matrix[i_check][j_check]
    
    result = True if sum==1 else False

    return result

def verify(matrix):
    
    result = True
    N = len(matrix)
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                if not is_isolate(matrix,i,j):
                    result = False
                    break
    
    return result

lines = ['1 0 0 0 0\n', '0 0 1 0 0\n', '0 0 0 0 0\n', '0 1 0 1 0\n', '0 0 0 0 0']
lst2D = []
for line in lines:
    line = line.rstrip('\n')
    lst2D.append(line.split())
N = len(lst2D)
for i in range(N):
    for j in range(N):
        lst2D[i][j] = int(lst2D[i][j])

print(verify(lst2D))
