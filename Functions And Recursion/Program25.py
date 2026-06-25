def elements(items, index):
    if index == len(items):
        return
    print(items[index], end=" ")
    elements(items, index + 1)
    
def main():
    my_list = [1, 2, 3, 4, 5]
    elements(my_list, 0)

main()