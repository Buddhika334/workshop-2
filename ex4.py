def find_mark(a,b):
    if(a>b):
        return a
    else:
        return b

num1=int(input("enter first number "))
num2=int(input("enter second number "))

max=find_mark(num1,num2)
print("maximum number:",max)