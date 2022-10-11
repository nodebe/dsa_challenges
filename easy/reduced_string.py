def superReducedString(s):
    # Write your code here
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
            continue

        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if len(stack) == 0:
        return "Empty String"
    
    stack = ''.join(stack)
        
    return stack