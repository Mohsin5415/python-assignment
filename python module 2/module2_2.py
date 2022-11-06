# Write a Python program to get the Factorial number of given number

fact =1
num = int(input("enter the number : "))
org = num
while num > 0:
    fact = fact * num
    num = num - 1
print("the factorial of ",org,"is",fact)