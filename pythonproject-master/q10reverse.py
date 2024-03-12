reverse=0
n=int(input("enter a number"))
while(n>0):
    r=n%10
    reverse=reverse*10+r
    n=n//10
print(reverse)