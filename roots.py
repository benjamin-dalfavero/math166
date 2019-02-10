'''
'''

def newton(f, df, x0, bound):
	'''
	solve for roots of a function by newton's method
	f: function to find roots
	df: derivative of f
	x0: initial guess
	bound: error bound
	'''
	x = x0 # current guess of root
	fx = f(x) # assign function value to variable so you don't need to evaluate again.
	dfx = df(x)
	x_n = x - fx / dfx # assign new guess
	fx_n = f(x_n)
	dfx_n = df(x_n)
	while abs(x_n - x) > bound:
		x = x_n # reassign previous guess
		fx = fx_n
		dfx = dfx_n
		x_n = x - fx / dfx # assign new guess
		fx_n = f(x_n)
		dfx_n = df(x_n)
	return x_n
