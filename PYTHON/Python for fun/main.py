from gameroom import Room

kitchen = Room("Kitchen")
dining = Room("Dining Hall")
court = Room("Basketball Court")
kitchen.set_description("A place where food is made with loving care.")
court.set_description("A place where Steven goes to feel like Luka Doncic")
dining.set_description("You consume.")

kitchen.link_room(dining, "south")
court.link_room(dining, "west")
dining.link_room(court,"east")
dining.link_room(kitchen,"north")

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    movement = input("ENTER MOVEMENT \n> ")
    movement.lower()
    current_room.move(movement)