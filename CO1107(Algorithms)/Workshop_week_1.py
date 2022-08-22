### Task 1
def letter_counter(word):
    word = word.upper()
    letter_tracker = {}
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    output_tuple = tuple()
 
    for i in word:
        if i in letter_tracker:
            print(f"{i} is in the dictionary")
            letter_tracker[i] = letter_tracker[i]+1
            print(letter_tracker)
        else:
            print(f"{i} not in the dictionary yet")
            letter_tracker.update({i:1})
            print(letter_tracker)



letter_counter("abcdabbb")

#search, and not found
# then update to add a new letter and count

###  Task 2
def getProduct(text):
    product = text.split("*")
    b = 1
    for a in product:
        a = int(a)
        b *= a

getProduct("12*2*10")
    
#### Task 3
class Student():
    def __init__(self, name, IDnumber=999, age=0, marks=0):
        self.name = name
        self.IDnumber = IDnumber
        self.age = age
        self.marks = marks

    def get_marks(self):
        return self.marks

    def get_age(self):
        return self.age

    def get_IDnumber(self):
        return self.IDnumber

    def set_marks(self, x):
        self.marks = x

    def set_age(self,x):
        self.age = x


    def Display(name):  #Check that this is the proper method of display
        return name.get(name.IDnumber, name.age, name.marks)

test = Student("Josh",189,18,90)
Student.Display(test)