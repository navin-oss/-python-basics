height=float(input("Enter your height in feet :"))
if(height>=3):
    print("You can ride")
    age=int(input("What is your age :"))
    if age<12:
        print("pay 200 rupees")
    elif age<=18:
        print("pay 250 rupees")   
    else:
        print("pay 300 rupees")         
else:
    print("You can  not ride")
print("Bye")                
