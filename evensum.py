total=0
for i in range(0,101,2):
    #if we can't use range third k part then we use if i%2==0 condition
    total=total+i
print(f"The sum  of even numbers is {total}")