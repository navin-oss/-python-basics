import random
names=input("Enter everybodys's names seperated by comma :")
names_list=names.split(",") 
#print(names_list)
#a=len(names_list)
#choice=random.randint(0,a-1)
#a=random.choice(names_list)
print(f"{random.choice(names_list)} will pay the bill.")
