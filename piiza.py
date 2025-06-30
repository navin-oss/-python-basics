bold = "\033[1m"
reset = "\033[0m"
title="WELCOME TO PIZZA SHOP"
print(bold + title.center(80) + reset)
print("costs of pizzas: ")
print("Small Pizza = 100 rupees \n Medium Pizza = 200 rupees \n Large Pizza = 300 rupees.")
sp=int(input("Enter quantity of Small Pizza:"))
mp=int(input("Enter quantity of Medium Pizza:"))
lp=int(input("Enter quantity of Large Pizza:"))
print("If you want preponi for Small Pizza = 30 rupees \nIf you want preponi for Medium and Large Pizza = 50 rupees ")
p=int(input("Enter quantity for preponi for small pizza:"))
pl=int(input("Enter quantity for preponi for Medium and Large pizza: "))
print("For extra cheese for any size  of pizza = 20 rupees.")
ch=int(input("Do you want extra cheese type 1 if you want or type 2 if you donot want:"))
if ch == 1:
    bill = sp * 100 + mp * 200 + lp * 300 + p * 30 + pl * 50 + ch * 20
    print(f"Your total bill is {bill}.")
else:
    bill = sp * 100 + mp * 200 + lp * 300 + p * 30 + pl * 50
    print(f"Your total bill is {bill}.")
