"""
Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,ādā:400}
Sample output: Counter ({'a': 400, 'b': 400,ādā: 400, 'c': 300}). 
"""
from collections import Counter  
dict1 = {'a': 100, 'b': 200, 'c':300}  
dict2 = {'a': 300, 'b': 200, 'd':400}  
new_dict = Counter(dict1) + Counter(dict2)  
print("The new  dict is:", new_dict)  