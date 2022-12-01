# Write a Python function that takes two lists and returns true if they have
# at least one common member. 
def common(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x==y:
             result=True
            return result
print(common([1,2,3,4],[9,5,6,7]))
print(common([1,2,3,4],[4,6,7,8]))