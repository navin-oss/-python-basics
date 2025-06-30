bold = "\033[1m"
reset = "\033[0m"
title="WELCOME TO PIZZA SHOP"
print(bold + title.center(80) + reset)
size =input("What size of pizza you want (s/m/l)?")
bill=0
if size=='s':
    bill +=100
    print("Small pizza price is 100 Rs.")
elif size=='m':
    bill +=200
    print("Medium pizza price is 200 Rs.")
else:
    bill +=300    
    print("Large pizza price is 300 Rs.")

pepporoni=input("Do you want to pepporoni(y/n)?")
if pepporoni=='y' or pepporoni=='Y':
    if size=='s' or size=='S':
        bill +=30
    else:
        bill += 50

cheese=input("Do you want extra cheese(y/n)?")
if cheese=='y' or cheese=='Y':
    bill+=20
print(f"Your final bill is {bill}.")    
