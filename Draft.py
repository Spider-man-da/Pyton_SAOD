import random

def Divider(massive,m,n):
    matrix=[]
    k=0

    for i in range(m):
        matrix.append([0] * n)
        for j in range(n):
            matrix[i][j] = massive[k]
            k+=1
    return matrix

mas=[random.randint(0,9) for i in range(15)]
print(mas)

matrix=Divider(mas,3,5)

print(matrix)