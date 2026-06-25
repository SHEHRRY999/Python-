tuple1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
num = int(input("Enter a number "))
i = 0
found = False
while i < len(tuple1):
    if(num == tuple1[i]):
        print("Found index", i)
        found = True
    i = i + 1
if(found == False):
    print("Not Found")