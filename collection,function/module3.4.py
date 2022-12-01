# Write a Python function to get the largest number, smallest num and sum
# of all from a list. 


mylist=[20,100,20,1,10]
mylist.sort()
print(mylist)
total=sum(mylist)

print("smallest element is : ",mylist[0])
print("largest element is : ",mylist[-1])
print("sum of all elements in given list : ",total)