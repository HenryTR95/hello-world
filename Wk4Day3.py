def f(a):
	N = len(a)

	for i in range(0, N):
		a[i] += ' ' + a[i] + '\n'
		print(a[i])

f(['yo', 'hi', 'how are you today'])
