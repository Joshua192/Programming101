Stacksize = 16
Stack = []

def push(x):
    global Stack, Stacksize
    if len(Stack) == Stacksize:
        return "Stack Overflow!!!"
    else:
        Stack.append(x)

def pop():
    global Stack, Stacksize
    if len(Stack) == Stacksize:
        return "Stack Overflow"
    elif len(Stack)==0:
        return "Stack Underflow!!!"
    else:
        Stack.pop()
        
for i in range(0,17):
    Stack.append(256)