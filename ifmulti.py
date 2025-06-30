height=float(input("Enter your height in feet :"))
bill=0
if(height>=3):
    print("You can ride")
    age=int(input("What is your age :"))
    if age<12:
        bill=150
        print("ticket price 200 rupees")
    elif age<=18:
        bill=250
        print("ticket price 250 rupee")   
    else:
        bill=500
        print("ticket price 300 rupees")  


    photo = input("Do you want photo yes or no:")     
    if(photo=='yes' or photo=='YES'):
          Note=print("You need to pay extra 40 rupees")
          Totalbill=bill+40
          print(f"Your Total bill is {Totalbill}")
else:
    print("You can  not ride")
print("Bye")                
