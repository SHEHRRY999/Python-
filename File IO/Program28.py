def checking_line():
    with open("practice.txt", "r") as f:
        data = True
        line_number = 1
        while data:
            data = f.readline()
            if(data.find("like") != -1):
                print("The word 'like' is present in the file at line:", line_number)
                return
            line_number += 1
        
    return -1
checking_line()    