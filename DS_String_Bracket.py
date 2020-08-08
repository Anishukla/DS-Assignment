def balanced_str(string):
    stack = []
    check = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    
    for char in string:
        if not stack:
            stack.append(char)  # Adding into empty stack    
            
        elif check[char] == stack[-1]:  
            stack.pop()         # Removing if top matches the it's closing bracket
            
        elif char not in check:
            stack.append(char)  # Adding other opening brackets
            
        else:
            stack.append(char)   
                    
    if stack:
        print("NO")
    else:
        print("YES")    

N = int(input())
for i in range(N):
    string = input()
    balanced_str(string)