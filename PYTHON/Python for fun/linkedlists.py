class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,data):
        newnode=Node(data)#Figure out where to point ot, but first determine if list is empty
        currentposition=self.head
        if currentposition==None: #If statement to check empty ll
            newnode.next = None #Pointer points to None because pointer at the end of a list always points to none
            self.head=newnode
            #is data to be added at the beginning of the ll
            print("NEW")
        elif currentposition.data>= newnode.data:#if checking if the new valus is before or after the first item in the ll
            self.head=newnode # if current item is bigger than new item, the make "head" pointer -> new item
            newnode.next=currentposition #Pointer "newnode.next" ->  "current position" item
            #Need to make a while loop that checks if its reached the end,
            # THEN keep comparing new item to items in the list till it finds one its smaller than then change pointers to point to it.
        else:
            while currentposition.next is not None and currentposition.next.data < newnode.data:# While the pointer of the current item looking at is not -> None, 
            #   AND the item of the next value* (*the data of the node current is pointing at) is smaller than the new data
                currentposition = currentposition.next
            newnode.next = currentposition.next         #While the next data value is smaller than the new one, increment the current pointer by 1 each loop 
            currentposition.next = newnode              #UNTIL it reaches a value bigger than it, then insert the new value inbetween them by changing previous pointer and making new
            print("Inserting")                          #new pointer -> to the next data value
    def delete(self, data):
        current = self.head
        if data == current.data:
            self.head = current.next
        else:
            while current!=None and data!=current.data:
                previous = current
                current=current.next
            previous.next = current.next # making the pointer of the previous node point to the next node. Essentialy pointing around the value you wnat to delete.
    def printlink(self):
        outlist = []
        current=self.head
        while current is not None:
            outlist.append(current.data)
            current = current.next
        print(outlist)



ll = linkedlist()
items = [5,2,7,4,8,3,9]
for i in items:
    ll.insert(i)
    ll.printlink()
ll.delete(5)
ll.printlink()