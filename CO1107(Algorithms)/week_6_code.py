class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class linked_list:
    def __init__(self):
        self.head=None
        self.count=0

    def insertEnd(self, newNode):
        if self.head is None:# if list is empty, head points to new node
            self.head=newNode
        else:
            lastNode=self.head #else last node in list points to the head, circular linked list???
            while True:
                if lastNode.next is None: #if end of list, break
                    break
                lastNode=lastNode.next #otherwise, update lastnode to the next one in the list
            lastNode.next=newNode #next points to the new node

    def insertHead(self, newNode): # creates a head pointer and points it to a new node
        tempNode = self.head
        self.head = newNode         
        self.head.next = tempNode #head points to the temp node, i think that basically deletes it  
        #del tempNode


    def insertAt(self, newNode, position):#Insert node at specified position
        currentNode=self.head
        currentPosition=0
        while True:
            if currentPosition == position:
                previousNode.next=newNode
                newNode.next=currentNode
                break
            previousNode=currentNode
            currentNode=currentNode.next
            currentPosition += 1

    def deleteEnd(self):
        lastNode=self.head# last node starts at beginning of list, makes lastnode equal to what head is pointing at
        while lastNode.next is not None:#Traverse till the last element. identifying info of last element is that node.next = None.
            prevNode=lastNode #update prevNode to the current value as long as it isn't the last element
            lastNode=lastNode.next # increment lastnode
        prevNode.next=None #now make prevNode point to none, making it the last element in the list
            

    def isEmpty(self): # self-explanatory, checks if list is empty
        if self.head is None:
            return True
        else:
            return False

    def traversal(self): # prints all the data at each node as it traverses the list
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode=currentNode.next
    

    def deleteHead(self):
        if self.isEmpty() is False:
            prevHead=self.head # store current head
            self.head=self.head.next # update the value of head to point to the next element
            prevHead.next=None # same as the other deletion, ignored then made to point to none
            print("The first item is deleted successfully")
        else:
            print("Linked List is empty, Delete Failed")
##############################################################################      
    def nodeCounter(self):  #Task 1
        counter = 0
        currentNode=self.head
        while currentNode is not None:
            counter += 1
            currentNode=currentNode.next
        print(counter)


    def deleteAt(self, position):#Takes in a specific poistion to delete    #Task 2
        try:
            if self.head!=None:
                currentNode=self.head #Current node statrs at the beginning of list
                currentPosition=0 #var to track position in the list
                while True:
                    if currentPosition == position: #is current posn the one we're looking for?
                        prevNode.next=currentNode.next # update previous pointer to point to where current is pointing, effectively ignoring the current node
                        currentNode.next=None # update the pointer for the current to be none, not neccesary but should include. "has future proofing reasons"
                        print(f"Successfully deleted item at {position}")
                        break
                    prevNode=currentNode #update prevnode to current one
                    currentNode=currentNode.next #increment current node
                    currentPosition +=1 #increment position by one
            else:
                print("The linked list is empty")
        except:
            print("This number is invalid")

    def deleteAll(self):    #Task 3
        currentNode=self.head
        while currentNode is not None:
            tempNode = currentNode.next
            currentNode.next = None
            currentNode=tempNode
        self.head = None
    
    def delete_negative(self): # Store the previous node, point it to the node of the 
        currentNode=self.head
        prevNode = self.head
        prevNode.next = currentNode
        while currentNode is not None:
            tempPointer = currentNode.next
            if currentNode.data < 0:
                prevNode.next = currentNode.next
                currentNode.next = None 
                currentNode = tempPointer # Made temp node for the  purposse of incrementing currentNode
        
    def add_all(self): #task 5
        currentNode=self.head
        prevNode = self.head
        prevNode.next = currentNode
        while currentNode is not None:
            tempPointer = currentNode.next

mylist=linked_list()
FirstNode=Node(1)
mylist.insertHead(FirstNode)
SecondNode=Node(-2)
mylist.insertEnd(SecondNode)
ThirdNode=Node(-3)
mylist.insertEnd(ThirdNode)
LastNode=Node(4)
mylist.insertEnd(LastNode)

# mylist.deleteHead()
# mylist.traversal()
# mylist.nodeCounter()

mylist.deleteAt(7)
mylist.traversal()


