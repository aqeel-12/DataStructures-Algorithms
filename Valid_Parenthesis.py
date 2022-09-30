s = "()[]{}"
def isValid(s):
    stack=[]
    matching={
        '}':'{',
        ']':'[',
        ')':'('
    }
    for x in s:
        if x in matching:
            if stack and stack[-1]==matching[x]:
                stack.pop()
            else:
                return False
        else:
            stack.append(x)    
    return True if not stack else False            
print(isValid(s))