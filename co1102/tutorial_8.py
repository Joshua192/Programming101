# Task 1
A = set()
B = set()
for x in range(2,100):
    if x%11==0:
        A.add(x)
    if x%5==0 and x%3==0:
        B.add(x)
print(A)
print(B)

#Task 2
def  contains_happy_number(nums): 
    """ Inputs: a set of integers  
        Outputs: True/False if the given set of numbers is happy. A happy 
        set contains at least one number divisible by 7. """ 
    Flag = False
    for num in nums:
        if num % 7 == 0: 
            Flag = True 
        else:
            next
    print(Flag)
contains_happy_number((1,21,3,24,18))

# Task 3
'''1. Write a function letter_counter that takes in a word and returns a 
dictionary that contains all the letters in the given word and their frequencies 
(the number of times they appear in the word). The returned dictionary is a 
histogram – a set of counters or frequencies. '''

letterdictionary = {} 
def letter_counter(word):
    for a in word:
        b = word.count(a)
        letterdictionary[a] = b
    print(letterdictionary)

letter_counter("missisipi")

'''2. Write a function letter_count that takes in a dictionary wherein key is a 
letter and value is the frequency of that letter and returns the total number of 
occurrences for the letters in the dictionary.  '''

def letter_count(dictionary):
    for a in dictionary.keys():
         