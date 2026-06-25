with open("numbers.txt", "w") as f:
    f.write("1, 2, 45, 65, 76")
number_list = None
with open("numbers.txt", "r") as f2:
    content = f2.read()
    number_list = content.split(", ")
count = 0
for number in number_list:
    if(int(number) % 2 == 0):
        count = count + 1

print("The count of even numbers in the file is:", count)
