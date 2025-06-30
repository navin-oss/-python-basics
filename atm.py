chances=3
balance=25000
while chances>=0:
    password=int(input("enter password :"))
    if password==1234:
        print("Press 1 or balance enquiry :")
        print("Press 2 or balance withdrawl :")
        print("Press 3 or balance cash deposite :")
        butt=int(input("Pres  key button :"))
        if butt==1:
            print(balance)
        elif butt==2:
          withdrawl=int(input("enter amout for withdrawl :"))
          balance=balance-withdrawl
          print(balance)
        elif butt==3:
            dep=int(input("Enter amout of cash for deposite"))
            balance=balance+dep
            print(balance)
    elif password!=1234:
        print("Invalid password ")
        