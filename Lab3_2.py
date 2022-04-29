import collections
from queue import PriorityQueue

test = collections.deque()
class Position:
    def __init__(self, position, start_distance,finish_distance):
        self.position = position
        self.start_distance = start_distance
        self.finish_distance = finish_distance

    def __str__(self):
        return '\n'.join((N*'{:3}').format(*[i%(N*N) for i in self.position[i:]]) for i in range(0, N*N, N))

    def __lt__(self, other):
        return self.start_distance+self.finish_distance < other.start_distance+other.finish_distance

N = 4

def shifts(position):
    start_position = position.index(0)
    i, j = divmod(start_position, N)
    changeloc = []
    if i > 0: changeloc.append(-N)
    if i < N - 1: changeloc.append(N)
    if j > 0: changeloc.append(-1)
    if j < N - 1: changeloc.append(1)
    for offset in changeloc:

        swap = start_position + offset

        yield tuple(position[swap]
        if x==start_position
        else position[start_position]
        if x==swap
        else position[x]
        for x in range(N*N))

def parity_pairs(state):
    countOfPairs = 0
    for i in range(len(state)-1):
        if state[i] > state[i+1]:
            countOfPairs +=1
    return countOfPairs % 2

def fifteen_game(start_state):
    state_terminal = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

    if parity_pairs(start_state)==0:
        print("Нет решений")
    else:

        start_state = tuple(start_state)
        p = Position(start_state, 0, 0)
        fieldStates = PriorityQueue()
        fieldStates.put(p)
        closePoints = set([p])
        parents = {p.position: None}

        while p.position != state_terminal:
            p = fieldStates.get()
            for k in shifts(p.position):
                count= 0
                if k not in closePoints:
                    for m in range(len(k)):
                        if k[m] != state_terminal[m]:
                            count+=1
                    fieldStates.put(Position(k, p.start_distance +1,p.finish_distance+count))
                    parents[k] = p
                    closePoints.add(k)

        path = []
        x = p
        prev = p

        while p.position != start_state:
            p = parents[p.position]
            number = p.position[prev.position.index(0)]
            path.append(number)
            prev = p
            test.append(p)
        path.reverse()

    if parity_pairs(start_state)!=0:
        for reverse_print in range(len(path)):
            print(f"\n{test.pop()}")
        print(f"\n{x}\n\n{path}\nStep count: {len(path)}")

data = [1,2,3,4,5,6,7,8,9,10,11,12,0,13,14,15]
data = [1, 2,  3,  0,5, 6,  7,  4,9, 10, 11, 8,13,14, 15, 12]
fifteen_game(data)