# decimal to binary

def binaryNo(num):
    if num==0:
        return 
    else:   
     binaryNo(num//2)
     print(num%2,end=" ")

n=int(input("enter num"))
binaryNo(n)
# decimal to octal
print()
def octalNo(num):
    if num==0:
        return 
    else:   
     octalNo(num//8)
     print(num%8,end=" ")

n=int(input("enter num"))
octalNo(n)

print()
#
def factorial(num):
   if num==0 or num==1:
      return 1
   else:
    return(num*factorial(num-1))
   

n=int(input("enter number"))
print("factorial of a given number is ",factorial(n))


# fibonacci series
def fibo(num):
   if num==1 or num==2:
    return num-1
   return fibo(num-1)+fibo(num-2)
print(fibo(5))

#geometric sum
