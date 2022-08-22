class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

Josh = Person('Joshua', 17, 'Male')


    # def greeting(self):
    #     return f'My name is {self.name} and I am {self.age} years old. My gender is {self.gender}.'

    # def birthday(self):
    #     self.age += 1
    #     return f'My name is {self.name} and I am turning {self.age} years old.'



# Object
# print(josh.greeting())
# print(josh.birthday())


class Customer(Person):
    # The 'Customer' class extends the 'Person' class.
    # Objects in the customer class can still call functions from the 'Person' class. Person is considered  "Superclass"
    # Constructor from the 'Person' class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    # def greeting(self):
    #     return f'My name is {self.name} and I am {self.age} years old. My gender is {self.gender} and my balance is {self.balance}.'


jade = Customer('Jade', 17, 'Female')
jade.set_balance(20000)

print(jade.greeting())
