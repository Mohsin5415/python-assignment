# Write a Python function to check whether a number is in a given range

def ran_check(num,low,high):
    if num in range(low,high):
        print(num ,"is in a range")
    else:
        print(num ,"is out of the range")
ran_check(100,90,200)