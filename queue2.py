from collections import deque
queue = deque(["Bus1","Bus2","Bus3","Bus4","Bus5","Bus6","Bus7","Bus8"])
print("Initial queue:", list(queue))
departed = queue.popleft()
print("Departed bus:", departed)
print("Queue now:", list(queue))
