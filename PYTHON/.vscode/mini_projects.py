sentence = "I saw a wolf in the forest. A lonely wolf."
print(sentence)
word = input("Enter the word to find: ")
position = sentence.find(word)
if position == -1:
    print("Unable to find word")
else:
    print("The word", word, "is at character position", position)


# Simple counting program
import random
i = random.randint(85,100)
print(f'the values of i is {i}')
while i <= 100:
    print(i)
    i += 1 

# Name Separator using Len and word.find
full_name = str(input("Enter Forename followed by surname:"))
print(full_name)
space_finder = full_name.find(" ")
print(space_finder)
first_name = full_name[0:space_finder]
last_name = full_name[space_finder:99]
print("First name:", first_name)
print("Last name:", last_name)

# Other Random bit of code
print("Begin")
Forename = str("joshua")
Surname = str("oyekunle")

Initial = Forename[0]
upperInitial = Initial.upper()
upperSurname = Surname.upper()
print(upperInitial, upperSurname)

    # removing the first and last letter of string
fort = len(Forename) - 1
Nickname = Forename[1:fort]
print(Nickname)

x = Surname[-12:] # why did I make this?
y = Surname[:10]
print(x)
print(y)

#use of .index() method to find a str or int in a list
def fruitFinder(finder_input):
    s = ['apple','pear','banana','pineapple']
    print(f'The fruit you entered can be found at {s.index(finder_input)}')

fruitFinder('banana')

# Removing words from sentences
x = str("The quick brown fox jumped over the lazy sleeping dog")
print(x)
word = str(input("Type a word you wish to remove from that sentence:"))
e = x.find(word)
y = e - 1
w = x[:y]
t = len(word)
u = e + t
o = x[u:]
print(w, o)# check if it'd be faster to conv str -> list. pop word. list -> str

# rolling die to get random numbers
r = int(input("Choose a dice type you wish to roll:"))
if r == 4:
    random_number = random.randint(1, 4)
    print("you rolled a", random_number)
elif r == 6:
    random_number = random.randint(1, 6)
    print("you rolled a", random_number)
elif r == 12:
    random_number = random.randint(1, 12)
    print("you rolled a", random_number)

# Find a way to refactor this and make it more concise
    x = int(input("input month number:"))
if x == 1:
    print("January")
elif x == 2:
    print("February")
elif x == 3:
    print("March")
elif x == 4:
    print("April")
elif x == 5:
    print("May")
elif x == 6:
    print("June")
elif x == 7:
    print("July")
elif x == 8:
    print("August")
elif x == 9:
    print("September")
elif x == 10:
    print("October")
elif x == 11:
    print("November")
elif x == 12:
    print("December")
else:
    print("This is outside of range of months")

# list methods
myList = []
myList.append()	#Adds an element at the end of the list
myList.clear()	#Removes all the elements from the list
myList.copy()	#Returns a copy of the list
myList.count()	#Returns the number of elements with the specified value
myList.extend()	#Add the elements of a list (or any iterable), to the end of the current list
myList.index()	#Returns the index of the first element with the specified value
myList.insert()	#Adds an element at the specified position
myList.pop()	#Removes the element at the specified position
myList.remove()	#Removes the first item with the specified value
myList.reverse() #Reverses the order of the list
myList.sort()	#Sorts the list

# counting from a specified number to 100
i = int(input("input a starting number:"))
for i in range(i, 10):
    print(i)
    i += 1

# Dictionaries. also include list, tuples, and sets.

# print(person['last_name'])
print(person.get('last_name'))

personal = person.copy()

person['phone_no'] = '079-XXXXXXXX'
# print(personal.keys())
# print(personal.items())

# del(person['Age'])
# person.clear()
# print(len(person))

# List Dictionary
people = [
    {'first_name': 'John',
     'last_name': 'Doe',
     'Age': 17
     },
    {'first_name': 'Martha',
     'last_name': 'Kent',
     'Age': 32
     }
]
print(people[1])
# Dictionaries have many of the same methods as lists


# this is a litlle side thing i made with methods and interpolation
def nameCase(name=''):
    return name.upper()


name = str(
    input("Enter name: ")
)
nameCase(name)

if name == '':
    print('ERROR, Please give a name')
else:
    print(f'HELLO {nameCase(name)}! NICE TO MEET YOU')

#core modules
from datetime import date
from time import time
date = date.today()
timestamp = time()
print(date, timestamp)

 #Custom module created in module.py, Email validator
from module import validate_email
email = 'test@test.com'
if validate_email(email):
    print(f'Email, {email} is vaild')
else:
    print(f'Email, {email} is invalid')

#Using a recursion to calculate factorials
def getFactorial(n):
    if n < 2:
        return 1
    else:
        return n * getFactorial(n-1)

print("FACTORIAL CALCULATOR")
n = int(input("Input a positive integer n: "))

print(getFactorial(n))

# Pyhton Programming Companion Problem
x = 5
y = 5

if x == 0 or y == 0:
    print('ERROR! one or more number are equal to zero')
else:
    if x < y: #this statement is TRUE if x SMALLER than y.
        if y % x == 0: # if statement to evaluate y divided by x.
            print(f'{y} is exactly divisible by {x}.')
        else:
            print(f'{y} is not divisible by {x}. The remainder is {y % x}')
    else: #in the case where x is LARGER than y.
        if x % y == 0: #if statement to evaluate x divided by y.
            print(f'{x} is exactly divisible by {y}.')
        else:
            print(f'{x} is not divisible by {y}. The remainder is {x % y}')

#Fibonacci Sequence
# Add term with the previous term
terms = [0,1]
x = 1
for b in range(0,10):
    y = x - 1
    i = terms[x] + terms[y]
    x += 1
    terms.append(i)
    print(terms)
    