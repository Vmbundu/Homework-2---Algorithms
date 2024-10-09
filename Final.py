import Misc
import Node
import MaxHeap
import time

priority = []

priority.append(Node.Node(1,'b'))
priority.append(Node.Node(6,'c'))
priority.append(Node.Node(5,'a'))
priority.append(Node.Node(3,'d'))
priority.append(Node.Node(4,'e'))
priority.append(Node.Node(7,'f'))
priority.append(Node.Node(8,'g'))
priority.append(Node.Node(9,'h'))
priority.append(Node.Node(10,'i'))
priority.append(Node.Node(11,'j'))
priority.append(Node.Node(12,'k'))
priority.append(Node.Node(13,'l'))
priority.append(Node.Node(14,'m'))
priority.append(Node.Node(15,'n'))
priority.append(Node.Node(16,'o'))
priority.append(Node.Node(17,'p'))
priority.append(Node.Node(18,'q'))
priority.append(Node.Node(19,'r'))
priority.append(Node.Node(20,'s'))
priority.append(Node.Node(21,'t'))
priority.append(Node.Node(22,'u'))
priority.append(Node.Node(32,'v'))
priority.append(Node.Node(25,'w'))
priority.append(Node.Node(24,'x'))
priority.append(Node.Node(33,'y'))
priority.append(Node.Node(29,'z'))

scale = priority
times = []

priority_heap = MaxHeap.MaxHeap()
priority_heap.create(priority)



internal_node = None

while len(priority_heap.heap) > 1:
    left_node = priority_heap.heap.pop()
    right_node = priority_heap.heap.pop()

    internal_node = Misc.combine(left_node, right_node)
    priority_heap.insert(internal_node)

Misc.traverse('', internal_node)
    #Misc.traverse('', internal_node)


'''
priority_heap = MaxHeap.MaxHeap()
priority_heap.create(priority)

for entry in priority_heap.heap:
    print(entry.freq)

internal_node = None

while len(priority_heap.heap) > 1:
    left_node = priority_heap.heap.pop()
    right_node = priority_heap.heap.pop()

    internal_node = Misc.combine(left_node, right_node)
    priority_heap.insert(internal_node)

Misc.traverse('', internal_node)
'''