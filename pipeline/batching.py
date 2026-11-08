"""Split a list of orders into batches for bulk loading."""


def batch_orders(orders, size):
    """Return the orders as a list of batches (lists) of at most `size` orders."""
    # Slicing works the same on every Python version: take `size` orders at a time.
    return [list(orders[start:start + size]) for start in range(0, len(orders), size)]
