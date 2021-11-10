t=int(input()) #number of testcases
while t!=0:
    l1=input().split() #string of two space seperated integers
    # print(l1)
    x=int(l1[0])
    k=int(l1[1])
    y=x*k
    min=x*2
    max=y*(y-1)
    print(min,max)
    
    t-=1
