import random
import math
import time

def Generator(length=50,min_limit=-250,max_limit=1004):

    if min_limit > max_limit:
        min_limit, max_limit = max_limit, min_limit

    massive=[random.randint(min_limit,max_limit) for _ in range(length)]

    return sorted(massive)

def Binary_search(massive, value):
    print("Binary_search")
    left = 0
    right = len(massive) - 1
    result = -1
    while (left <= right) and (result == -1):
        middle = (left+right)//2
        if massive[middle] == value:
            result = middle
        else:
            if value<massive[middle]:
                right = middle -1
            else:
                left = middle +1
    return result

def Fibonacci_search(massive, value):
    print("Fibonacci_search")
    length = len(massive)

    start = -1

    f0 = 0
    f1 = 1
    f2 = 1
    while (f2 < length):
        f0 = f1
        f1 = f2
        f2 = f1 + f0

    while (f2 > 1):
        index = min(start + f0, length - 1)
        if massive[index] < value:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif massive[index] > value:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (massive[length - 1] == value):
        return length - 1
    return -1

def Interpolation_search(massive, value):
    print("Interpolation_search")
    left = 0
    right = len(massive) - 1
    while left <= right and value >= massive[left] and value <= massive[right]:
        index = left + int(((float(right - left) / (massive[right] - massive[left])) * (value - massive[left])))
        if massive[index] == value:
            return index
        if massive[index] < value:
            left = index + 1
        else:
            right = index - 1
    return -1


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
class Tree:
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root
    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)
    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)
    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None
    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)
    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)
#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(0)
tree.add(2)
tree.printTree()
print()
print(tree.find(3).v)
print(tree.find(10))
tree.deleteTree()
tree.printTree()

def delete(massive,i):
    del massive[i]

def insert(massive,value,i):
    massive.insert(i,value)


length=int(input("Введите размер массива: "))

s=input("Введите диапазон генерации: ").split()
min_limit,max_limit=int(s[0]),int(s[1])

value=int(input("Какое значение ищем: "))

massive_search_function=[Binary_search, Fibonacci_search,Interpolation_search]
time_massive=[]

massive=Generator(length,min_limit,max_limit)

for func in massive_search_function:
    print(*[str(massive[i])+" ["+str(i)+"]" for i in range(len(massive))])

    time0=time.time()
    result=func(massive,value)
    time1=time.time()-time0
    time_massive.append(time1)

    print("Результат: " ,result)
    print("Время выполенения: ",'%.2f' %time1," c.")
    print()