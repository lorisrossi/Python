from __future__ import division
from plotting import *

def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

@memo
def factorial(n): return 1 if n <= 1 else n * factorial(n-1)

def bin_coeff(n, k): return factorial(n) / (factorial(n-k) * factorial(k))


def binomial_distribution(n, p):
    "Print all values for K = 0, ..., n."
    values = [bin_coeff(n, i) * p**i * (1-p)**(n-i) for i in range(n+1)]
    return values


numbers = input('N, P: ')
distr = binomial_distribution(numbers[0], numbers[1])
for i in range(len(distr)):
    print 'K = %d\t%f' % (i, distr[i])

print
barchart(range(len(distr)), distr, len(distr))
