Stacksize = 16
Stack = []

def push(x):
    global Stack, Stacksize
    print(f"{Stack}, Stack Size:    {len(Stack)}")
    if len(Stack) == Stacksize:
        print("Stack Overflow!!!")
    else:
        Stack.append(x)

def pop():
    global Stack, Stacksize
    if len(Stack)==0:
        print("Stack Underflow!!!")
    else:
        Stack.pop()


for i in range(0,17):
    push(256)

pop()
pop()
print(Stack)