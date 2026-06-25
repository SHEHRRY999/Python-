with open("practice.txt", "w") as f:
    f.write("Hello Everyone\n")
    f.write("We are learning File IO\n")
    f.write("We like programming in Java\n")
    f.write("We like programming in Java\n")

with open("practice.txt", "r") as f2:
    content = f2.read()
    print(content)
    new_content = content.replace("Java", "Python")
    print("After replacing Java with Python:\n")
    print(new_content)
with open("practice.txt", "w") as f3:
    f3.write(new_content)
