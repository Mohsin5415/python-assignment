# Write a Python function that takes a list of words and returns the length
# of the longest one.


na=input("Enter line of string : ")
n=na.split()
longest=len(n[0])
for i in n:
    if len(i)>longest:
        longest=len(i)
print("longest string length = ",longest)