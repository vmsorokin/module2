def get_matrix(n, m, value):
    matrix=[]
    for i in range(n):
        matrix1=[]
        matrix.append(matrix1)
        for j in range(m):
            # print(j)
            matrix1.append(value)
    return matrix


result1 = get_matrix(2,2,10)
result2 = get_matrix(3,5,42)
result3 = get_matrix(4,2,13)
print(result1)
print(result2)
print(result3)