num = int(input("Enter a number "))
fact = 1
for el in range(num, 1, -1):
    fact *= el
print("The factorial of", num, "is", fact)