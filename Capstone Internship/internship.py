from multiprocessing.dummy import Array
from math import *

def closestNumbers(numbers):
    # Write your code here
    # Your taking in i and i+1, then storing a value for the difference between them. you loop through the array, replacing this lowestVal until you have gotten the lowest val(1 loop).
    # Then, you search the array for any pair that matches this in value and then store the pairs in a new array called pairArr. then sort them by first value into a ordered arr. (see if sort works on this thing)
    # print the ordered arr
    # numbers is an array!
    pairArray = []
    # print(pairArray)
    orderedArray = []
    lowestVal = 9999
    i = 0
    j = i+1
    while i < len(numbers)-2:
        currentDiff =  numbers[i] - numbers[j]#change this to only work for positive ints.
        if currentDiff <0:
            currentDiff = numbers[j] - numbers[i]
            print("CASE 1")
        
        if currentDiff < lowestVal:
            lowestVal = currentDiff
            print("CASE 2")
        i+=1
    print("CASE 3")
    x = 0
    while x < len(numbers)-1:
        while x < len(numbers)-2:
            currentDiff2 =  numbers[i] - numbers[j]
            if currentDiff2 <0:
                currentDiff2 = numbers[j] - numbers[i]
            if lowestVal == currentDiff2:
                pairArray.append((numbers[i],numbers[j]))
            x+=1
        print("CASE 4")
        print(pairArray)


arrayd = [2,4,6,5,3,8]
closestNumbers(arrayd)
