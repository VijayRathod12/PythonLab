#using function write a python script for :
# find whether given number is palindrome or not
def palindrome(n):
    t=n
    reverse=0
    while n>0:
       r=n%10
       reverse=reverse*10+r
       n=n//10

    if t==reverse:
        print("given nubmer is palindrome")
    else:
       print("number is not palindrome")
num=int(input("enter number"))
palindrome(num)

# find sum of frist n natural number
def sum_of_num(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
num=int(input("enter  natural number"))
res=sum_of_num(num)
print(res)