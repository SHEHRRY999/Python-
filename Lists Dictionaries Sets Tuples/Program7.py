list = []
val1 = int(input("Enter the First Value:"))
list.append(val1)
val2 = int(input("Enter the Second Value:"))
list.append(val2)
val3 = int(input("Enter the Third Value:"))
list.append(val3)
list.reverse()
list2 = list.copy()
if(list[0] == list2[2] and list[1] == list2[1] and list[2] == list2[0]):
    print("The List is Palindrome")
else:
    print("The List is not Palindrome")