n=int(input("enter frist value"))
m=int(input("enter second value"))
choice=int(input("enter 1 or 2"))
if choice==1:
    print("addition is :",n+m)
elif choice==2:
    print("subtraction is :",n-m)
else:
    print("enter number either 1 or 2 only")

# check even number
num=int(input("enter a number"))
if num%2==0:
    print("number is even") 
else:
    print("odd")

# conersion of height
height=int(input("enter height in cm"))
choice=int(input('enter 1 for meter ,2 for inches'))
if choice==1:
  meterheight=height/100
  print("height in meter",meterheight)
elif choice==2:
  cmheight=height/2.54
  print("height in cmheight",cmheight)

# leap year program
year=int(input("enter year"))
if year%4==0 and year%100!=0 or year%400==0:
     print("it is a leap year")
else:
   print(" not  a leap year")