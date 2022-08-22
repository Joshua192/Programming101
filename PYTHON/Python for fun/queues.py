Qsize = 16
Queue = [None] * Qsize
tail = 0
head = 0
i = 0
print(f"Queue:  {Queue}")
#Circular Queue

def enqueue(item):
    global Queue, tail, head
    Queue.append(item)
    Queue[tail%Qsize] = item    #Changes the value of the item to a value 
    tail += 1
    if item == 0:
        tail = 0

def dequeue():
    global Queue, tail, head
    Queue[head % Qsize]
    head += 1


def printqueue():
    global Queue, tail, head
    out = ""
    for i in range(head,tail):
        out += str(Queue[i])+""
    print(out)

enqueue(5)
enqueue(10)
dequeue()
printqueue()

#OOP Queue
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None # pop from here
        self.back=None # Add from here
    
    def enqueue(self, data):
        newNode=Node(data)
        if self.back==None:
            self.front = newNode
        else:
            self.back.next=newNode
        self.back=newNode
    
    def dequeue(self):
        if self.front!=None:
            pop=self.front.data
            print(pop)
            self.front=self.front.next

    def printqueue(self):
        out = []
        if self.front!=None:
            curr=self.front
            last=self.back
            while last!=curr:
                out.append(curr.data)
                curr=curr.next
            out.append(curr.data)
        print(out)

a = Queue()

a.enqueue(5)
a.printqueue()

a.enqueue(23)
a.printqueue()

a.enqueue(2)
a.printqueue()

#Go study the Diagrams and explanation for a linked list // Queue