# How Do You Handle Exceptions With Try/Except/Finally In Python?


def divide(x, y):
	try:
		result = x // y
		print("Yeah ! Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")

divide(3, 2)
divide(3, 0)



def divide(x, y):
	try:
	
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
	else:
		print("Yeah ! Your answer is :", result)
divide(3, 2)
divide(3, 0)
