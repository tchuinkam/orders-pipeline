"""Split a list of orders into batches for bulk loading."""
from itertools import batched


def batch_orders(orders, size):
    """Return the orders as a list of batches (lists) of at most `size` orders."""
    # batched() groups an iterable into tuples of up to `size` items; we turn each into a list.
    return [list(batch) for batch in batched(orders, size)]
