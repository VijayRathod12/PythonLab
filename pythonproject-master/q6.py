#leap year 
year=int(input("enter year"))
if (year%400==0 and year%100==0) or(year%4==0 and year%100!=0):
    print("year is leap year")