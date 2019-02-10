def newton(f, df, x0, bound):
	'''
	solve for roots of a function by newton's method
	f: function to find roots
	df: derivative of f
	x0: initial guess
	bound: error bound
	'''
	x = x0 # current guess of root
	x_n = x - f(x) / df(x) # assign new guess
	while abs(x_n - x) > bound:
		x = x_n # reassign previous guess
		x_n = x - f(x) / df(x) # assign new guess
	return x_n
