def sum(n):
    if(n == 1):
        return 1
    else:
        return n + sum(n - 1)
    
def main():
    number = 10
    print("The sum of first", number, "natural numbers is", sum(number))

main()