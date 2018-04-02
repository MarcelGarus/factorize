# factorize
A small prime factorization program that can be called with a number:

![python factorize.py 2595925957847039](https://github.com/marcelgarus/factorize/blob/master/factorize.gif?raw=true)

In case you're in the mood for extending this functionality, the file also offers two generators: `primes` and `factorize`.
```python
from factorize import primes, factorize
```

## primes
`primes` is a simple generator for creating prime numbers.
```python
for prime in primes():
    print(prime)
# prints 2, 3, 5, 7, ...
```
Optionally, you can provide a maximum number `n` of primes you want to get:
```python
print(list(primes(5)))
# prints [2, 3, 5, 7, 11]
```
Or declare a `limit` for the largest prime (`primes you get <= limit`):
```python
print(list(primes(limit=100)))
# prints [2, 3, ..., 89, 97]
```

## factorize
`factorize` is a generator that lets you factorize a number into its primes.
```python
for factor in factorize(2595925957847039):
    print(factor)
# prints 38047, 140281, and 486377 with a break between each number as it takes
# some time to calculate each factor
```
The generator yields factors as they become available.
