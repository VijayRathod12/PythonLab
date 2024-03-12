
# to find all the numbers of a list that are divisible by particular element
n=int(input("enter a particular number"))
lst=[3,6,1,22,12,45,8]
lst1=[]
for i in lst:
    if i%n==0:
        lst1.append(i)
print(lst1)

