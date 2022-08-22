#use an algorithm to convert characters in a string into ASCII characters
#Add up the values of the string
#MOD by 100
#insert the value into an array at that position
#Don't worry about the clashes

def hashing(item, tablesize):
    total = 0
    for letter in item:
        total = total + ord(letter)
    return total%tablesize

print(hashing("massachussettes",10))
print(hashing("florida",10))
print(hashing("california",10))
print(hashing("alabama",10))
