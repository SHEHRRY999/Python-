def calculate_length(list):
    return len(list)
def elements(list):
    for i in range(len(list)):
        print(list[i], end=" ")
def main():
    my_list = [1, 2, 3, 4, 5]
    print(calculate_length(my_list))
    elements(my_list)

main()