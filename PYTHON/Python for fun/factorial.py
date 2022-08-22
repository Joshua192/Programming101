def factorial(n):
    result=1
    for k in range(1,n+1):
        result = result*k
    return result
def factrecur(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
print(factorial(6))
print(factrecur(6))