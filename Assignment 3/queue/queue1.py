from collections import deque
queue = deque([1,2,3,4,5,6,7,8,9])
print("Initial queue:", list(queue))
for _ in range(6):
    queue.popleft()

print("Queue after serving 6 citizens:", list(queue))
print("Front of the queue:", queue[0])
