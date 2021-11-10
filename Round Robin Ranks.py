# cook your dish here
t=int(input()) #number of testcase
while t!=0:
    nums=input().split() #string of two space-separated integers
    n=int(nums[0])
    k=int(nums[1])
    print(2*((2*n-k-1)//2))
    t-=1
