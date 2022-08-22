list = [1,2,3,4,5,6,7,8,9]
print(list)
x = int(input("Insert a number you want to search for in the  list: "))
def linearsearch(x):
    for i in list:
        print(f"Current Value: {i}")
        if x == i:
            print("Found it")
            break
        else:
            print(f"Haven't found it yet!!!")
        if x!= i:
            print("value not in list")
linearsearch(x)