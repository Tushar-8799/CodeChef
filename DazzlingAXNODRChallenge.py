# cook your dish here
for i in range(int(input())):
    n= int(input())
    b=1
    if n % 4 == 3 or n % 4 == 2:
        print(3)
    elif n % 4 == 0:
        print(n+3)
    elif n % 4 ==1:
        print(n)
