"""

How will you remove last object from a list
Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

----> Python provides us with an array of methods, using which we can achieve our target

1) Using list.pop() function : The simplest approuch is to use the list's pop([i]) function,which removes an element present at
the specified position in the list.if we don't specify any index,pop() removes and returns the last element in the list.

2) Using slicing : we can use slicing to remove the last element from a list.the idea is to obtain a sublist containing
all elements of the list except the last one.since slice operation returns a new list,we have to assign the new list to
the original list.this can be done using the expression l = l[:-1]

3) Using del statement : another way to remove an element from a list using its index is the del statement.it
differs from the pop() function as it does not return the removed element.unlike the slicing function,this 
doesn't create a new list


----> list1 is [2, 33, 222, 14, and 25]  : Here negative indexing starts from right end that means the index of 25 is -1
"""