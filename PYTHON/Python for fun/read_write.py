myFile = open('mytext.txt', 'r')


myFile = open('mytext.txt', 'r+')
print_statement = myFile.read(9999)
print(print_statement)


# print('Name:',myFile.name)
# print('Is closed:',myFile.closed)
# print('Opening Mode:',myFile.mode)