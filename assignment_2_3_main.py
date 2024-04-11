from random import randint

INF = float('inf')

class MinimumPriorityQueue:
    def __init__(self, queue=[]):
        self.queue = queue
        if len(queue):
            self.heapify()
    def get_parent(self, i):
        return (i - 1) // 2 if i else 0
    def heaping(self):
        i = len(self.queue) - 1
        while i > 0:
            parent_index = self.get_parent(i)
            parent_value = self.queue[parent_index]
            if parent_value > self.queue[i]:
                self.queue[i], self.queue[parent_index] = parent_value, self.queue[i]
            i = parent_index

    def get_left_side(self, i):
        return 2*i + 1
    def get_right_side(self, i):
        return 2*i + 2
    def push(self, x):
        self.queue.append(x)
        self.heaping()
    def pop(self, debug=False):
        if not len(self.queue):
            raise Exception
        returned_value = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self.pop_heapify()
        if debug:
            self.print_heap()
        return returned_value
    def pop_heapify(self):
        i = 0
        n = len(self.queue)
        while i < n:
            left_child_index, right_child_index = self.get_left_side(
                i), self.get_right_side(i)
            if left_child_index >= n or right_child_index >= n:
                break
            left_child_value, right_child_value = self.queue[left_child_index], self.queue[right_child_index]
            index = right_child_index
            if left_child_value < right_child_value:
                index = left_child_index
            if self.queue[i] > min(left_child_value, right_child_value):
                self.queue[i], self.queue[index] = self.queue[index], self.queue[i]
                i = index
            else:
                break
    def print_heap(self):
        print(*self.queue)

def prims(matrix):
    '''
    This function return the MST for a connected Graph.
    If there is Disconnected Graph then this algorithm returns one of the spanning tree present in that graph
    '''
    n = len(matrix)
    source = randint(0, n - 1)  # selecting random vertex
    # source = 0
    priority_queue = MinimumPriorityQueue()
    priority_queue.push((0, source, source))
    visited = set()
    tree = list()
    ret = 0
    while priority_queue.queue:
        cost, top, parent = priority_queue.pop()
        if top in visited:
            continue
        visited.add(top)
        tree.append((top, parent, cost))
        ret += cost
        for i in range(len(matrix[top])):
            if matrix[top][i] != 0 and matrix[top][i] != INF:
                # optimisation: Skipping the vertex which is already present in the tree.
                if i not in visited:
                    priority_queue.push((matrix[top][i], i, top))
    for child, parent, cost in tree:
        print(f'{parent} -> {child} = {cost}')
    return ret


def main():
    matrix = [
        [0, 4, INF, INF, INF, INF, INF, 8, INF],
        [4, 0, 8, INF, INF, INF, INF, 11, INF],
        [INF, 8, 0, 7, INF, 4, INF, INF, 2],
        [INF, INF, 7, 0, 9, 14, INF, INF, INF],
        [INF, INF, INF, 9, 0, 10, INF, INF, INF],
        [INF, INF, 4, 14, 10, 0, 2, INF, INF],
        [INF, INF, INF, INF, INF, 2, 0, 1, 6],
        [9, 11, INF, INF, INF, INF, 1, 0, 7],
        [INF, INF, 2, INF, INF, INF, 6, 7, 0],
    ]
    matrix = [
        [0, 2, INF, 1, 4, INF],
        [2, 0, 3, 3, INF, 7],
        [INF, 3, 0, 5, INF, 8],
        [1, 3, 5, 0, 9, INF],
        [4, INF, INF, 9, 0, INF],
        [INF, 7, 8, INF, INF, 0],
    ]
    matrix = [
        [0, 2, 4, 1, INF, INF, INF],
        [2, 0, 2, 3, INF, INF, INF],
        [4, 2, 0, 5, INF, INF, INF],
        [1, 3, 5, 0, INF, INF, INF],
        [INF, INF, INF, INF, 0, 1, 3],
        [INF, INF, INF, INF, 1, 0, 2],
        [INF, INF, INF, INF, 3, 2, 0],
    ]
    print(prims(matrix))
if __name__ == "__main__":
    main()
