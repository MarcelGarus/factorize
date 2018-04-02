# factorize
a simple prime factorization module

This small, simple file provides two generators: `primes` and `factorize`:
```python
from factorize import primes, factorize
```
Or you can just call it with a number to let it be factorized:
```shell
python factorize.py 2595925957847039
```

## primes
`primes` is a simple generator for creating prime numbers.
```python
for prime in primes():
    print(prime)
# prints 2, 3, 5, 7, ...
```
Optionally, you can provide a number of primes you want to get:
```python
print(list(primes(5)))
# prints [2, 3, 5, 7, 11]
```
Or even a limit for the largest prime (inclusive):
```python
print(list(primes(limit=100)))
# prints [2, 3, ..., 89, 97]
```

## factorize
`factorize` is a simple generator for factorizing a number into its primes.
```python
for factor in factorize(2595925957847039):
    print(factor)
# prints 38047, 140281, and 486377 with a break between each number as it takes
# some time to calculate them
```
The generator yields factors as they become available.
