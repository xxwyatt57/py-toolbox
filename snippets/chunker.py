"""
chunk an iterable into fixed-size lists.
stolen from the more_itertools recipe, kept here to avoid the dep.
"""

from itertools import islice


def chunks(iterable, size):
    """yield lists of length `size` from `iterable`, last may be shorter."""
    it = iter(iterable)
    while True:
        batch = list(islice(it, size))
        if not batch:
            return
        yield batch


if __name__ == "__main__":
    for c in chunks(range(10), 3):
        print(c)
