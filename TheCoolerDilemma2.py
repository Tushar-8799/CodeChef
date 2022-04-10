# cook your dish here
for i in range(int(input())):
    x,y = map(int, input().split(" "))
    if y%x != 0:
        print(y//x)
    else:
        print(y//x-1)
