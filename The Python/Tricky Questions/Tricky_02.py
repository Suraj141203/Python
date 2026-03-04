a = 10 
if a == 10.0:
    print("a is 10")
else:
    print("different")

# Output is a is 10 because == checks the value not the type

if a is 10.0:
    print("a is 10")
else:
    print("different")

# Output is different because is checks the type
