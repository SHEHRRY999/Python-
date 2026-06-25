value1 = int(input("Enter A Value:"))
value2 = int(input("Enter A Value:"))
value3 = int(input("Enter A Value:"))
if(value1 > value2) and (value1 > value3):
    print("The Largest Value is:", value1)
elif(value2 > value1) and (value2 > value3):
    print("The Largest Value is:", value2)
else:
    print("The Largest Value is:", value3)
