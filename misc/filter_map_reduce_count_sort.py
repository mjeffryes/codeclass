def filter(pred, l):
    """ Accepts a predicate (pred) and a list (l).
        Returns a new list containing only the items from li
        where pred(l) matches (returns true).
    """
    # base case
    if l == []:
        return l
    # recursive step
    tail = filter(pred, l[1:])
    if pred(l[0]):
        return [l[0]] + tail
    else:
        return tail

assert filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]
assert filter(lambda x: x % 3 != 0, [1, 2, 3, 4, 5]) == [1, 2, 4, 5]

def map(func, l):
    """ Accepts a function (func) and a list (l).
        Returns a new list that is the result of applying func
        to every element of l.
    """
    # base case
    if l == []:
        return l
    # recursive step
    tail = map(func, l[1:])
    return [func(l[0])] + tail

assert map(lambda x: x * 2, [1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]
assert map(len, ['hello', 'bob']) == [5, 3]

def reduce(func, l, init):
    """ Accepts a function of two arguments (func), a list (l) and an
        initial value. Applies func cumulatively to the items of l 
        from left to right, starting with the value in init, 
        so as to reduce the list to a single value.
    """
    # base case
    if l == []:
        return init
    # recursive step
    return reduce(func, l[1:], func(init, l[0]))

assert reduce(lambda x, y: x + y , [1, 2, 3, 4, 5], 0) == 15
assert reduce(lambda x, y: x * y , [1, 2, 3, 4, 5], 1) == 120
assert reduce(lambda x, y: x + ' ' + y , ['hello', 'bob'], '') == ' hello bob'


def count(pred, l):
        """ Accepts a predicate (pred) and a list (l).
        Returns the number of items in l where pred(l) matches (returns true).
    """
    # base case
    if l == []:
        return 0
    # recursive step
    remainder = count(pred, l[1:])
    if pred(l[0]):
        return 1 + remainder
    else:
        return remainder

assert count(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == 2
assert count(lambda x: x % 3 != 0, [1, 2, 3, 4, 5]) == 4


