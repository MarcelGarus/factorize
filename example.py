from factorize import primes, factorize

print(list(primes(5)))
# prints [2, 3, 5, 7, 11]

print(list(primes(limit=100)))
# prints [2, 3, ..., 89, 97]

start = time()
for factor in factorize(2595925957847039):
	print(factor, time() - start)
# prints something like this:
# 38047 0.641836404800415
# 140281 6.760272264480591
# 486377 6.760589838027954
# Factors are generated on the fly, so it takes some time until each of them is
# ready to process
