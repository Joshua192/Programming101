i = int(input("Starting number: "))
while i != 1:
    if i is i %2 == 0:
        i = i/2
        print(i)
    else:
        i = 3*i + 1
        print(i)