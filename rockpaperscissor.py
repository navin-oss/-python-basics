import random 
user_choice=int(input("Enter your choice: Type 0 for rock, Type 1 for paper,Type 2 for scissor :"))
computer_choice=random.randint(0,2)
print("Computer chose :" )
print(computer_choice)
if user_choice>=3 or user_choice<0:
    print("Invalid input")
else:
    if computer_choice==user_choice :
        print("It's a draw.")
    elif computer_choice==0 & user_choice==2:
        print("Computer win , you lose")
    elif user_choice==0 & computer_choice==2:
        print("YOU win,computer lose.")
    elif computer_choice>user_choice:
        print("Computer win ,you lose.")
    elif user_choice>computer_choice:
     print("You win, computer lose.")

