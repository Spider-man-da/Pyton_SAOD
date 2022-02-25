import random

def task1():
    m = [int(i) for i in input().split()]

    m.sort(reverse=True)

    max_sum=0

    for i in range(len(m)):
        for j in range(i+1,len(m)):
            for k in range(j+1,len(m)):
                m2=sorted([m[i],m[j],m[k]])
                if m2[0]+m2[1]>m2[2]:
                    max_sum=sum(m2)
                    break
            if max_sum!=0: break
        if max_sum!=0: break

    print(max_sum)

def task2():
    m = [i for i in input().split()]

    max_m=max([len(i) for i in m])

    m2=[]

    for el in m:
        n=max_m//len(el)
        s_el=el*n

        for i in range(max_m%len(el)):
            s_el+=el[i]
        m2.append(s_el)

    m3=list(zip(m,m2))


    m4=sorted(m3,key=lambda x: x[1],reverse=True)

    result=""

    for i in m4:
        result+=i[0]

    print(result)

def task3():
    s = input().split()
    m,n=int(s[0]),int(s[1])
    matrix=[]

    for i in range(m):
        matrix.append([0]*n)
        for j in range(n):
            matrix[i][j]=random.randint(0,9)
            print(matrix[i][j],end=" ")
        print()

    i=m-2
    j=0

    while not (i==0 and j==n-1):
        a,b=i,j
        mas=[]
        mas.append(matrix[a][b])

        while a+1<m and b+1<n:
            a+=1
            b+=1
            mas.append(matrix[a][b])

        mas.sort()
        a,b,k=i,j,0
        matrix[a][b]=mas[k]

        while a+1<m and b+1<n:
            a+=1
            b+=1
            k+=1
            matrix[a][b]=mas[k]

        if i!=0: i-=1
        else: j+=1

    print()

    for i in range(m):
        for j in range(n):
            print(str(matrix[i][j]).ljust(2),end='')
        print()

