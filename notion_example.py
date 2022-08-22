empID = input("Enter your employee ID: ")
empID = empID.upper()
if len(empID) > 6 or empID[0] == "E":
    print("Missed input, this ID is invalid")
# daysWorked = int(input("How many days have you worked?: ")) 
# ~This method can work but I'm using a longer method because 
# I want to include a simple error check
daysWorked = input("How many days have you worked?: ")
if daysWorked.isdigit()==False:
    print("Days worked is an invalid input.")
print("End Program.")