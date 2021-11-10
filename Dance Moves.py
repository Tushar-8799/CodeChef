# cook your dish here
t=int(input()) #number of testcases
while t!=0:
    l=[]
    count=0 #initialize the minimum number of moves
    l=input().split()
    x=int(l[0]) #position of Chef 
    y=int(l[1]) #position of his dance partner
    # print(x,y)
    if x>y:
        print(x-y)
    elif x==y:
        print(0)
    else:
        if (y-x)%2==0:
            count=(y-x)//2
            print(count)
        else:
            count=(y-x)//2
            print(count+2)     
    t-=1
