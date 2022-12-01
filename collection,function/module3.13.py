# Write a Python program to select an item randomly from a list. 

import random

myList = [1, 2, 3, 45, 6, 8, 78, 23, 56, 7686, 123]
print("The list is:")
print(myList)
random_element = random.choice(myList)
print("The randomly selected element is:", random_element)