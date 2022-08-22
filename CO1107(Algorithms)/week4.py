# Task 1
def factorial(num):
    if num == 1:
        result = []
        result.append(1)
    else:
        result = factorial(num-1)
        result.append(num*result[num-2])

    return result


print(factorial(5))

# Task 2
a= [1,2,3,4,5,6,7]
def sum_calculator(a):
    if not a:
        return 0
    else:
        sum = a[0]
        a.pop(0)
        output = sum + sum_calculator(a)
    return output


print(sum_calculator(a))

# Task 3

def printToN(value):
    print(value)
    if value==1:
        exit
    else:
        printToN(value-1)
printToN(2)


def printToN(value):
    print(value*value) #squared 
    if value==1:
        exit
    else:
        printToN(value-1)
printToN(2)


# def sum_ofsquares(a):
#     # if not a:
#     #     return 0
#     # else:
#     #     sum = a[0]
#     #     a.pop(0)
#     #     output = sum + sum_calculator(a)
#     # return output


# print(sum_calculator(a))