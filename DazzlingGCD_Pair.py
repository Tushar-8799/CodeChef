# cook your dish here
for i in range(int(input())):
    a, b = map(int, input().split())
    if a % 2 == 0:
        if b-a >=2:
            print(str(a)+" "+str(a+2))
        else:
            print(-1)
    else:
        if b-a >= 3:
            if a % 3 ==0:
                print(str(a) + " " + str(a+3))
            else:
                print(str(a+1) +" "+ str(a+3))
        else:
            print(-1)
