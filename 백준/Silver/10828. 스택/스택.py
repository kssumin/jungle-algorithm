import sys

n = int(sys.stdin.readline())
stack = []


def isEmpty(stack):
    return len(stack) == 0

for _ in range(0, n):
    command = sys.stdin.readline().strip().split(" ")
    if(command[0] == "push"):
        stack.append(command[1])
    if (command[0] == "top"):
        if isEmpty(stack):
            print(-1)
        else:
            print(stack[-1])
    if(command[0] == "size"):
        print(len(stack))
    if(command[0] == "empty"):
        if isEmpty(stack):
            print(1)
        else:
            print(0)
    if(command[0] == "pop"):
        if isEmpty(stack):
            print(-1)
        else:
            print(stack.pop())