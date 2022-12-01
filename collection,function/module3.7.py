# Write a Python program to remove duplicates from a list.

n=int(input("enter the total no of element you want inside your list : "))
l=[]
for i in range(n):
    ele=input("enter the element")
    l.append(ele)
print("my list",l)
non_duplicate_value=set(l)
print(non_duplicate_value)