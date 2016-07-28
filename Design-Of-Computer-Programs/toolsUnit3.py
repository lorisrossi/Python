from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

# Alternativa di decorator
# def decorator(d):
#   return lambda fn: update_wrapper(d(fn), fn)

@decorator
def n_ary(f):
    """Given binary function f(x,y), return an n_ary function such that
    f(x, y, z) = f(x, (f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f


@n_ary
def seq(x, y): return ('seq', x, y)



@decorator
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

@decorator
def countcalls(f):
    "Decorator that makes the function count calls to it, in callcounts[f]."
    def _f(*args):
        callcounts[_f] += 1
        return f(*args)
    callcounts[_f] = 0
    return _f



@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print '%s--> %s' % (trace.level*indent, signature)
        trace.level += 1
        try:
            result = f(*args)
            print '%s<-- %s === %s' % ((trace.level-1)*indent,
                                        signature, result)
        finally:
            trace.level -= 1
        return result
    trace.level = 0
    return _f

def disabled(f): return f # toglie un decoratore, i.e. "trace = disabled"

@trace
@memo
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)

#fib(10)
