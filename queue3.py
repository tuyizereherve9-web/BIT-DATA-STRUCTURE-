#Initialize an empty queue to represent the line of students.
#Add students to the queue in the order they arrive (enqueue).
#While the queue is not empty:
#Remove the student at the front of the queue (dequeue).
#Serve the student.
#Record the student in a served list for verification.
#Repeat until all students are served.
#Output the order of serving to confirm fairness.

from collections import deque
queue = deque(["Student1","Student2","Student3","Student4"])
print("Initial queue:", list(queue))
served_students = []
while queue:
    served_students.append(queue.popleft())

print("Order of serving (FIFO):", served_students)
