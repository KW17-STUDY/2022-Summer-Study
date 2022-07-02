def solution(s):
    stack = []
    for i in s:
        if len(stack)==0 or stack[-1]!=i:
            stack.append(i)
        else:
            stack.pop()
    
    return 0 if len(stack)!=0 else 1