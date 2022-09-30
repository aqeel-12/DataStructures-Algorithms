from collections import deque


s ="()[]{}"
def valid(s):
    stack=deque()
    for x in s:
        if x=='(' or x=='[' or x=='{':
            stack.append(x)
        if     