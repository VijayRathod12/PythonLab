n =int(input("enter a number"))
temp=n
reverse=0
while n>0:
    r=n%10
    reverse=reverse*10+r
    n=n//10
#print(reverse)
if temp==reverse:
    print("given nubmer is palindrome")
else:
    print("number is not palindrome")



