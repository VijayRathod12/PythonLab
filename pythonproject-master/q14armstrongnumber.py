n=int(input("enter a number"))
result=0
temp=n
a=len(str(n))
while n>0:
   digit=n%10
   result= result+digit**a
   n=n//10 
print(result)
if temp==result:
   print("number is armstrong")
else:
   print("not a armstrong")
   
"""
l=[3,6,1,5]
l2=[3,7,1,6]
x=[]
for i in l:
   for j in l2:
      if i==j:
        x.append(j)
print(x)
l3=[i  for i in l if i in l2]
print(l3)


def is_vowel(v):
   vowel=['a','e','i','o','u']
   return v in vowel
print(is_vowel('c'))


def check(str):
   vowel="aeiouAEIOU"
   count=0
   for i in str:
     for j in vowel:
        if i==j:
           count+=1
   return count
print(check("sddejfeurf"))
"""


# binary search 
def binarysearch(l,s,e,k):
   while s<=e:
     mid=s+e//2
     if l[mid]==k:
       return mid
     elif l[mid]>k:
        e=mid-1
     else:
        s=mid+1
   return -1
l=[2,3,5,8]

index=binarysearch(l,0,len(l)-1,8)
if index!=-1:
   print(index)
else:
   print("element not found")
