import sys
def is_correct(string):
    stack = []
    for s in string:
        if s == "(" or s == "[":
            stack.append(s)

        if s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False

        if s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False

    if stack == []:
        return True
    return False

def getValue(string):
    stack = []
    for s in string:
        if s == "(" or s == "[":
            stack.append(s)

        if s == ")":
            if stack[-1] == "(":
                stack.pop()
                stack.append(2)
            else:
                temp_sum = stack.pop()
                a = stack[-1]
                while (type(a) == int):
                    temp_sum += stack.pop()
                    a = stack[-1]
                stack.pop()
                temp_sum *= 2
                stack.append(temp_sum)

        if s == "]":
            if stack[-1] == "[":
                stack.pop()
                stack.append(3)
            else:
                temp_sum = stack.pop()
                a = stack[-1]
                while (type(a) == int):
                    temp_sum += stack.pop()
                    a = stack[-1]
                stack.pop()
                temp_sum *= 3
                stack.append(temp_sum)
    return (sum(stack))

input_string = sys.stdin.readline().rstrip()
if is_correct(input_string):
    print(getValue(input_string))
else:
    print(0)