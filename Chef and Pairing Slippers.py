t=int(input()) #the number of test cases
while t!=0:
    s=input().split() #string of three space-separated integers
    n=int(s[0]) #the total number of slippers
    l=int(s[1]) #the number of left slippers
    x=int(s[2]) #the price of a pair of slippers in rupees
    r=n-l
    if r>l:
        print(l*x) 
    else:
        print(r*x)
    t-=1
