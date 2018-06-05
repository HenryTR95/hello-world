# Homework 2, Problem 3

# finds the largest odd number out of x, y, and z
def f1(x, y, z):
	order = [x, y, z]
	
	# sort order from largest to smallest
	for i in range(3):
		for j in range(2):
			if order[j] < order[i]:
				temp = order[j]
				order[j] = order[i]
				order[i] = temp
	# check order from front to back until a odd number is found
	# then return that odd number
	if order[0] % 2 == 1:
		return order[0]
	if order[1] % 2 == 1:
		return order[1]
	if order[2] % 2 == 1:
		return order[2]
	# if no odd numbers were found then say so
	return "none of these inputs are odd numbers"
