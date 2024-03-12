isprime=True
n=int(input("enter a number"))
for i in range(2,n//2):
    if n%i==0:
          isprime=False
          #print("given number is  a prime number")
          break
    
if isprime==True:
     print("given number is prime number ")
     
else:
     print("number is not a prime number")


"""
find  sum of frist  n natural number
 factorial of given number 
find sum of digit of given n digit number
reverse of a given number
given number is plaindrome or not
 given number is armstrong number or not 
fibonacc series 
PRINT ALL the even numbers in range 100 -200
first 50 odd number
print all the 3 digit prime numbers 
all the 3 digit armstrong number

"""


