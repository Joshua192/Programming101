x = "abc.dss"
y = x.find(".")
x = x[y+1:len(x)].upper()
print(x)
