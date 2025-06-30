def greet():
    print("Hi")


greet()
greet()
def addd(a,b):
    c=a+b
    print("addition=",c)
addd(4,6)     

def add(*numbers):
    c=0
    for i in numbers:
        c +=i
        print(f"sum  is {c}")

add(1,2,3,4)       