year=int(input("Enter your year="))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("The given year is leap year")

        else:
             print("The given year is not leap year")
    else:
        print("The given year is  leap year")
else:
     print("The given year is not leap year")
