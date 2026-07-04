x = int(input("Enter A Number : "))
match x:
    case 1:
        print("You Entered One")
    case 3:
        print("You Entered Three")
    case _ if x > 3:
        print("You Entered A Number Greater Than Three")
    case _ if x < 1:
        print("You Entered A Number Less Than One")