numbers=input("Enter list of numbers :")
numbers_list=numbers.split()
#11 23 55 89 
count = 0
for number in numbers_list:
    count+=1
print(f"lenght of string {count}")
#for i in range(0,len(numbers_list)):#This is using len function.
#    numbers_list[i]=int(numbers_list[i])
#print(numbers_list)
for i in range(0,count):
    numbers_list[i]=int(numbers_list[i])
#print(numbers_list)
maximum_number=numbers_list[0]
for number in numbers_list:
    if number > maximum_number:
        maximum_number=number
print(f"The maximum number is : {maximum_number}")  