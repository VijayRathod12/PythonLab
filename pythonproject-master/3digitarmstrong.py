"""
result=0
for i in range(100,1000):
    temp=i
    while i>0:
     digit=i%10
     result=result+digit**3
     i=i//10
     if temp==result:
        print(i)
"""
 

 #using function
print("using function ")
def is_armstrong(n):
   result=0
   while n>0:
       digit=n%10
       result=result+digit**3
       n=n//10
       print(result)
       return result==n
#def armstrong(s,e):
for i in range(100,999):
    if is_armstrong(i):
        print(i)
#armstrong(100,999)