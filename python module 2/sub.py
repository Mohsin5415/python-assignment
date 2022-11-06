# Write a Python program to sum of three given integers. However, if
# two values are equal sum will be zero

a=int(input("enter a first value : "))
b=int(input("enter a second value : "))
c=int(input("enter a third value : "))

if a==b or b==c or c==a:
    print("sum is: ",0)
else:
    print("sum is : ",a+b+c)  