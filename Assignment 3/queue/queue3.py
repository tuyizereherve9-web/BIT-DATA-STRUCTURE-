# Algorithm for Canteen Food Ordering
#Start with an empty queue.
#As each student arrives, enqueue (add) them at the end of the queue.
#When food is served, dequeue (remove) the student at the front.
#Repeat step 3 until the queue is empty.
#End.

from collections import deque

print("QUEUE (FIFO) - Fair system in canteen")
canteen_queue = deque()
canteen_queue.append("Student1")
canteen_queue.append("Student2")
canteen_queue.append("Student3")
canteen_queue.append("Student4")
while canteen_queue:
    print("Served:", canteen_queue.popleft())
