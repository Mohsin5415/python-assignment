# Write a Python program to find whether a given number is even or odd,
# print out an appropriate message to the user

number=int(input("enter a number : "))
reminder=number%2
if(reminder==0):
    print(number,"is an even number")
else:
    print(number,"is an odd number")