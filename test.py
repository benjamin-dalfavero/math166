from roots import newton

# test newton's method function

# declare funcctions for test
f = lambda x: (x + 2) ** 2
df = lambda x: 2 * (x + 2)

init = 0.0 # initial guess for x
bound = 0.001 # error bound

print(newton(f, df, init, bound))
