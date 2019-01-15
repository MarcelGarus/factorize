# -*- coding: utf-8 -*-
"""Python Factorization program ~ Marcel Garus

This program allows to factorize any number and see the progress.

Examples:
	$ python factorize.py 123
	$ python factorize.py 32137821738

Github project:
	https://github.com/marcelgarus/factorize/
"""

from sys import exit, argv # needed if called as a program
from math import sqrt, ceil # needed for upper bound of factors


def primes(n=-1, limit=-1):
	"""primes is a generator for creating prime numbers.

	If both arguments are provided, the first one to restrict the generator
	will take effect. If none is provided, the generator creates an infinite
	number of primes.

	Args:
		n (int, optional): The maximum number of primes to be generated.
		limit (int, optional): A limit for the largest prime.

	Yields:
		int: The next prime.

	Examples:
		>>> print(list(primes(5)))
		[2, 3, 5, 7, 11]
		>>> print(list(primes(limit=100)))
		[2, 3, ..., 89, 97]
	"""
	found = list() # all the found primes
	candidate = 2 # the current candidate

	# if n or limit is given, use that. if both are -1, this loop runs forever
	while (n < 0 or len(found) < n) and (limit < 0 or candidate <= limit):
		# check if it's a prime (can you divide it by any previous prime?)
		is_prime = True
		for prime in found:
			if candidate % prime == 0:
				is_prime = False
				break
			if prime > sqrt(candidate):
				break


		# if it's indeed a prime, add it to list of found primes and yield it
		if is_prime:
			found.append(candidate)
			yield candidate

		candidate += 1 # next candidate


# Generator for prime factors of the given number
def factorize(n, __output=False):
	"""factorize is a generator for factorizing a number into its primes.

	Args:
		n (int): The number to be factorized into primes.

	Yields:
		int: The next factor.

	Examples:
		>>> print(list(factorize(12)))
		[2, 2, 3]
	"""
	if __output:
		print(n)
		print('= %d (...)' % n, end='\r')

	operator = '=' # the operator to display. either '=' or '*'
	limit = ceil(sqrt(n))
	for prime in primes():
		if __output:
			print('%c %d (calculated primes up to %d ...)' %
					(operator, n, prime), end='\r')

		# divide n by the prime as often as possible and yield prime every time
		divided = True
		while divided:
			divided = False
			if n % prime == 0:
				n //= prime
				limit = ceil(sqrt(n))
				if __output:
					print('%c %d\033[K' % (operator, prime))
					print('* %d (dividing by primes ...)' % n, end='\r')
				divided = True
				operator = '*'
				yield prime

		if n == 1 or prime > limit:
			break

	if n != 1: # n itself is now a prime
		if __output:
			print('%c %d\033[K' % (operator, n))
		yield n


if __name__ == '__main__':
	"""Main program.
	"""
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
		for factor in factorize(n, __output=True):
			factors.add(factor)
	except (KeyboardInterrupt, EOFError):
		print('%c %d (aborted)\033[K' % ('=' if len(factors) == 0 else '*',
			n if len(factors) == 0 else n // sum(factors)))
