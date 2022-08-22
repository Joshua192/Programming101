# COLLATZ CONJECTURE
n = float(input("Input a positive number: "))

print("Collatz Conjecture")

while n != 1:
    if n % 2 == 0:
        n = n/2
        print(n)
    else:
        n = 3*n + 1
        print(n)

# FIND AND PRINT MAX VALUE
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def getMax():
    print(max(a))


getMax()
