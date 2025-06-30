                        bold = "\033[1m"
reset = "\033[0m"
title="LOVE CALCULATOR "
name1=input("What is your name?")
name2=input("What is his/her name?")
combine_string = name1 + name2
lower_case_string = combine_string.lower()

t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")
true = t  + r + u + e

l =lower_case_string.count("l")
o =lower_case_string.count("o")
v =lower_case_string.count("v")
e =lower_case_string.count("e")
love = l + o + v + e

Love_score = int(str(true) + str(love))
if Love_score<10 or Love_score>90:
    print(f"Your score is {Love_score} and you go toghether loke coke and mentos ,you both are made for each  other.")
elif Love_score>=40 and Love_score<=50:
    print(f"Your love score is {Love_score} and you are alright together.")
else:
    print(f"Your love score is {Love_score} and you are friends.")
