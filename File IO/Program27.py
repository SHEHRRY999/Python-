with open("practice.txt", "r") as file:
    content = file.read()
    print(content)
    if content.find("learning") != -1:
        print("The word 'learning' is present in the file.")
    else:
        print("The word 'learning' is not present in the file.")
        