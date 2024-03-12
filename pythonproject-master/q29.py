#to print table of 10 until user choice using list comprehension and lambda function
n=int(input("enter n"))
res=[i*10 for i in range(1,n+1)]
for i in res:
 print(i) 