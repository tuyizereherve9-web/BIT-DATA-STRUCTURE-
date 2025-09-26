#Algorithm to reverse "QUEUEFIFO"

#Create an empty stack.

#Push each character of "QUEUEFIFO" onto the stack.

#Pop each character from the stack and append to a new string.

#Resulting string is reversed.

x = "QUEUEFIFO"
stack = []
for char in x:
    stack.append(char)
reversed_x = ""
while stack:
    reversed_x += stack.pop()

print("Original string:", x)
print("Reversed string:", reversed_x)
