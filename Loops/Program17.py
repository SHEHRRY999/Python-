list = [1,2,3,4,5,6,7,8,9,10]
num = 19
found = False
for t in list:
    if(t == num):
        print("Found index", list.index(t))
        found = True
if not found:
    print("Not found")
