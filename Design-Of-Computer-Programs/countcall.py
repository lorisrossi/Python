# copialo nel codice, perche devi usare c.starts e c.items
# come variabili globali. Inoltre ricordati di modificare tutte
# le funzioni chiamate con c(...)

def c(sequence):
    """Generate items in sequence; keeping counts as we go. c.starts is the
    number of sequences started; c.items is number of items generated."""
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item

def instrument_fn(fn, *args):
    c.starts, c.items = 0, 0
    result = fn(*args)
    print '%s got %s with %5d iters over %7d items' % (
        fn.__name__, result, c.starts, c.items)
