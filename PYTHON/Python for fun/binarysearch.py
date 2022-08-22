list = [1,2,3,4,5,6,7,8,9]
list.sort()
print(list)
found = False
divider = len(list)//2
print(divider)
beginning = list[0]
end = len(list)-1
x = int(input("Insert a number you want to search for in the  list:"))

def binarysearch(x):
    global list,found,divider,beginning,end;
    print("search starting")
    while found == False and beginning<= end:
        if divider == x:
            found = True
            print(x)
        elif divider < list.find(x):#Error found here, the issue is between the divider value and the fact that list has no method find()
            list=list[divider:end]
            print(x)
        else:
            list=list[beginning:divider]
            print(x)
binarysearch(x)

#list eeds to hvae divider equal the midpoint
#begining equal the start
#end equal the end of the list
# x is the value to be found
#if the value at the position "divider" is equal to "x" print found it and stop the program
# if the value  
