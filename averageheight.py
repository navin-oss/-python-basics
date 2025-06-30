height=input("Enter all heights separated by space:")
heightlist=height.split( )
count=0
for height in heightlist:
    count=count+1
#print(count)125 145 155 169 1844 
for i  in range(0,count):
    heightlist[i]=int(heightlist[i])
print(heightlist)

sum=0
for k in heightlist:
    sum=sum+k
print("Sum of heights = ",(sum))
avg=sum/count
print("Avg is = ",round(avg))