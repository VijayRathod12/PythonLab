#factorial of a given number
n=int(input("enter n"))
fact=1
for i in range(n,1,-1):
    fact=fact*i
    i=i-1
print(fact)