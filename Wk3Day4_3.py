# Henry Rybolt

# This code outputs all the prime numbers that are 
# less than N

N = input("Please enter a number as an upper limit: ")
N = int(N)

for i in range(2, N):
	check_var = True # assume i is prime
	for k in range(2, i):
		if (i%k) == 0: # if i divisable by any number less than itself
					   # it cannot be prime
			check_var = False
	if check_var:
		print(i) # print the prime numbers
