from functools import reduce  # forward compatibility for Python 3
import operator


def get_by_path(root, items):
    """Access a nested object in root by item sequence."""
    return dict(reduce(operator.getitem, items, root))


def set_by_path(root, items, value):
    """Set a value in a nested object in root by item sequence."""
    get_by_path(root, items[:-1])[items[-1]] = value


def del_by_path(root, items):
    """Delete a key-value in a nested object in root by item sequence."""
    del get_by_path(root, items[:-1])[items[-1]]
