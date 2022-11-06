# Write python program that swap two number with temp variable and without temp variable. 

# with temp variable
num1 = int(input("enter a number num1 : "))
num2 = int(input("enter a number num2 : "))

temp = num1
num1 = num2
num2 = temp

print("after swapping\n")
print("num1 = ",num1)
print("num2 = ",num2)

# without temp variable
num1 = int(input("enter a number num1 : "))
num2 = int(input("enter a number num2 : "))

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("after swapping\n")
print("num1 = ",num1)
print("num2 = ",num2)

