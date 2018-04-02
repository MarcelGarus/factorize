# prime factorization

from sys import exit, argv
from math import sqrt, ceil

# Generator for prime numbers. Optionally, one can provide how many primes to
# get or a limit for the biggest prime yielded
def primes(n=-1, limit=-1):
	found = set()
	candidate = 2

	while (n < 0 or len(found) < n) and (limit < 0 or candidate <= limit):
		# check if it's a prime
		is_prime = True
		for prime in found:
			if candidate % prime == 0:
				is_prime = False
				break

		# if it's indeed a prime, add to list of primes and yield it
		if is_prime:
			found.add(candidate)
			yield candidate

		candidate += 1 # next candidate


# Generator for prime factors of the given number
def factorize(n, output=False):
	if output:
		print(n)
		print('= %d (...)' % n, end='\r')

	first_factor = True
	limit = ceil(sqrt(n))
	for prime in primes():
		if output:
			print('%c %d (calculated primes up to %d ...)' %
					('=' if first_factor else '*', n, prime), end='\r')

		# divide by the prime as often as possible
		divided = True
		while divided:
			divided = False
			if n % prime == 0:
				n //= prime
				limit = ceil(sqrt(n))
				if output:
					print('%c %d\033[K' % ('=' if first_factor else '*', prime))
					print('* %d (dividing by primes ...)' % n, end='\r')
				divided = True
				first_factor = False
				yield prime

		if n == 1 or prime > limit:
			break

	if n != 1: # n itself is a prime
		if output:
			print('%c %d\033[K' % ('=' if first_factor else '*', prime))
		yield n


# main code
if __name__ == '__main__':
	# get argument or ask for number, example number: 2595925957847039
	n = argv[1] if len(argv) > 1 else input('Positive integer number > ')
	try:
		n = int(n)
		if n <= 0:
			raise ValueError('Too small.')
	except ValueError:
		print('Error. Provide a truly positive integer number instead of: ' + n)
		exit(-1)

	factors = set()
	try:
		for factor in factorize(n, output=True):
			factors.add(factor)
	except (KeyboardInterrupt, EOFError):
		print('%c %d (aborted)\033[K' % ('=' if len(factors) == 0 else '*',
			n if len(factors) == 0 else n // sum(factors)))
