n=int(input())
t=n
r=0
while(n>0):
    d=n%10
    r=r+d**3
    n=n//10
if(t!=r):
    print("no")
else:
    print("yes")
