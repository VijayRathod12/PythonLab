
#fibonacc series iterative

n =int(input("enter a number"))
f0=0
f1=1
for i in range(n-1):  
    next=f0+f1
    f0=f1
    f1=next
print("fibonacc series for ",n, "is:",next)


# recursive fibonacci series
def fibonacc(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibonacc(n-1)+fibonacc(n-2)
n=int(input("enter n"))
print(f"fibonacci series for {n} value  is {fibonacc(n)}")