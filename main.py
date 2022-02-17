import random
import math

def Generator(m=50,n=50,min_limit=-250,max_limit=1004):
    print("Generator: ")
    matrix=[]

    if min_limit > max_limit:
        min_limit, max_limit = max_limit, min_limit

    for i in range(m):
        matrix.append([0]*n)
        for j in range(n):
            matrix[i][j]=random.randint(min_limit,max_limit)

    return matrix

def Unification(matrix):
    massive=[]

    for i in matrix:
        for j in i:
            massive.append(j)

    return massive
def Divider(massive,M,N):
    matrix=[]
    k=0

    for i in range(M):
        matrix.append([0] * N)
        for j in range(N):
            matrix[i][j] = massive[k]
            k+=1
    return matrix

def Selection_sort(matrix,M,N):
    print("Selection sort:")
    nums=Unification(matrix)

    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return Divider(nums,M,N)

def Insertion_sort(matrix,M,N):
    print("Insertion sort:")
    nums = Unification(matrix)

    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    return Divider(nums,M,N)

def Heap_sort(matrix,M,N):
    print("Heap sort:")
    nums = Unification(matrix)
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

    return Divider(nums,M,N)
def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def Quick_sort(matrix,M,N):
    print("Quick sort:")
    nums=Unification(matrix)
    nums=for_quick_sort(nums)
    return Divider(nums,M,N)
def for_quick_sort(nums):
    less = []
    equal = []
    greater = []
    if len(nums) > 1:
        pivot = nums[0]
        for x in nums:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return for_quick_sort(less) + equal + for_quick_sort(greater)
    else:
        return nums

def Shell_Sort(matrix,M,N):
    print("Shell sort:")
    nums=Unification(matrix)

    n = len(nums)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = nums[i]
            j = i
            while j >= interval and nums[j - interval] > temp:
                nums[j] = nums[j - interval]
                j -= interval
            nums[j] = temp
        k -= 1
        interval = 2**k -1
    return Divider(nums,M,N)

def Bubble_sort(matrix,M,N):
    print("Bubble sort:")
    nums=Unification(matrix)

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return Divider(nums,M,N)

def Tournament_Sort(matrix,M,N):
    print("Tournament sort: ")
    arr= matrix.copy()

    for i in range(len(arr)):
        for_tournamentSort(arr[i])

    return arr
def for_tournamentSort(arr):
    tree = [None] * 2 * (len(arr) + len(arr) % 2)
    index = len(tree) - len(arr) - len(arr) % 2

    for i, v in enumerate(arr):
        tree[index + i] = (i, v)

    for j in range(len(arr)):
        n = len(arr)
        index = len(tree) - len(arr) - len(arr) % 2
        while index > -1:
            n = (n + 1) // 2
            for i in range(n):
                i = max(index + i * 2, 1)
                if tree[i] != None and tree[i + 1] != None:
                    if tree[i][1] < tree[i + 1][1]:
                        tree[i // 2] = tree[i]
                    else:
                        tree[i // 2] = tree[i + 1]
                else:
                    tree[i // 2] = tree[i] if tree[i] != None else tree[i + 1]
            index -= n

        index, x = tree[0]
        arr[j] = x
        tree[len(tree) - len(arr) - len(arr) % 2 + index] = None



s=input("Введите размер массива: ").split()
m,n=int(s[0]),int(s[1])

s=input("Введите диапазон генерации: ").split()
min_limit,max_limit=int(s[0]),int(s[1])

massive_sort_funtion=[Selection_sort,Insertion_sort,Heap_sort,Quick_sort,Shell_Sort,Bubble_sort,Tournament_Sort]

for func in massive_sort_funtion:
    matrix=Generator(m,n,min_limit,max_limit)
    print(*matrix,sep="\n")
    print()
    matrix=func(matrix,m,n)
    print(*matrix,sep="\n")
    print()

