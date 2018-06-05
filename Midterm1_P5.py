# Midterm 1: Problem 5
# Henry Rybolt

# a should be in the form of [a0, a1,  ... an]
# ie lowest order coefficient first 
def polynomial(a, x):
	N = len(a)
	running_sum = 0
	for i in range(N):
		running_sum = running_sum + a[i]*x**i
	return running_sum

# example of the operation of the polynomial function
a = input("Enter list of poylnomial coefficiants from LOWEST to HIGHEST order: ")
x = input("Enter x: ")
print polynomial(a, x)
