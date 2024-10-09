class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self.heapifyUp(len(self.heap) - 1)

    def heapifyUp(self, i):
        while i != 0 and self.heap[self.parent(i)].freq < self.heap[i].freq:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extractMax(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return root

    def heapifyDown(self, i):
        largest = i
        left = self.leftChild(i)
        right = self.rightChild(i)

        if left < len(self.heap) and self.heap[left].freq > self.heap[largest].freq:
            largest = left

        if right < len(self.heap) and self.heap[right].freq > self.heap[largest].freq:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapifyDown(largest)

    def create(self,list):
        for entry in list:
            self.insert(entry)
        return self.heap