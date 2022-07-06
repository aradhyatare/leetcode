


# tokens = ["2","1","+","3","*"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] 
# tokens = ["4","13","5","/","+"]

# print(int(6/-132))

stack = []
operations = ['+', '-', '*', '/']
for token in tokens:
    # while stack:
    if token not in operations:
        stack.append(token)
    else:
        first = int(stack.pop())
        second = int(stack.pop())
        # print(token)
        # print(first)
        # print(second)
        if token == '+':
            result = second + first
        elif token == '-':
            result = second - first
        elif token == '*':
            result = second * first 
        elif token == '/':
            result = int(second / first)
        stack.append(result)
print(stack[0])


            

# 9 + 3 => 12 
# tokens1 = ["10","6","12","-11","*","/","*","17","+","5","+"] 
#  12 * -11 => -132
#  
# tokens1 = ["10","6","-132","/","*","17","+","5","+"] 
