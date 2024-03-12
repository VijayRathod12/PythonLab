#  to print following patterns
"""
*
**
***
****

"""
n=int(input("enter n"))
for i in range(n+1):
    for j in range(i):
      print("*",end=" ") 
    print()

"""
****
***
**
*
"""
n=int(input("enter n"))
for i in range(n,0,-1):
   for j in range(i):  
      print("*",end=" ")
   print()

   """
1
22
333
4444
   """
   
n=int(input("enter n"))
for i in range(n+1):
    for j in range(i):
      print(i,end=" ") 
    print()

"""
    *
   **
  ***
"""
n=int(input("enter n"))
for i in range(n+1):
   for j in range(n,-1,-1):
      if i>=j:
       print("*" ,end=" ")
      else:
         print(" ",end=" ")
   print()

"""
1
2 3
4 5 6
7 8 9 10


"""
x=1
n=int(input("enter n"))
for i in range(1,n+1):
  for j in range(i):
    print(x,end=" ")
    x+=1
  print()





"""
    *
  * * * 
* * * * *
"""

#pascal's triangle
def fact(i):
   if i>=1:
      f= i*fact(i-1)
      return f

def ncr(i,j):
   return int((fact(i)/(fact(j)*fact(i-j))))
n=int(input("enter n"))
for i in range(1,n+1):
    for j in range(n-i):
       print(" ",end=" ")
    for k in range(i):
       print(ncr(i,j),end=" ")
    print()
