class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = ""
        self.linked_rooms = {}
    
    def get_name(self):
        return self.name

    def set_description(self, room_description):
        self.description = room_description
    
    def get_description(self):
        return f"You are in the {self.get_name()} \n{self.description}"
    
    def describe(self):
        print(self.description)
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print(f"{self.name} linked rooms:  {repr(self.linked_rooms)}")     #prints the dictionary of linked rooms and the object linked rooms as

    def get_details(self):
        print(self.get_description())
        for x in self.linked_rooms:
            room = self.linked_rooms[x]
            print( f"The {room.get_name()} is {x}")
    
    def move(self, direction):
        if direction in self.linked_rooms[direction]:#problem is something to do with this code
            return self.linked_rooms[direction]     #Self.linked_rooms[direction], Room in general is not iterable
        else:
            print("Hey! You can't go that way!")
            return self