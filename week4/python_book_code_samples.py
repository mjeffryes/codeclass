# Code samples curated from The Python Cookbook
# https://github.com/dabeaz/python-cookbook

thenewlist = map(lambda x: x + 23, theoldlist)

############

thenewlist = [x + 23 for x in theoldlist]

############

thenewlist = filter(lambda x: x > 5, theoldlist)

############

thenewlist = [x for x in theoldlist if x > 5]

############

thenewlist = map(lambda x: x+23, filter(lambda x: x>5, theoldlist))

############

thenewlist = [x + 23 for x in theoldlist if x > 5]

arr = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

############

print([[r[col] for r in arr] for col in range(len(arr[0]))])

multilist = [[0 for col in range(5)] for row in range(10)]

############

[0] * 5

############

multi = [[0] * 5] * 3
print(multi)

############

row = [0] * 5          # a list with five references to 0
multi = [row] * 3      # a list with three references to the row object
d = {'key':'value'}

############

temp = a
a = b
b = c
c = temp

############

a, b, c = b, c, a

############

if d.has_key('key'):     # or, in Python 2.2 or later: if 'key' in d:
  print(d['key'])
else:
  print('not found')

############

print(d.get('key', 'not found'))
def deal_with_a_cat():
    print("meow")

def deal_with_a_dog():
    print("bark")

def deal_with_a_bear():
    print("watch out for the *HUG*!")

tokenDict = {
    "cat": deal_with_a_cat,
    "dog": deal_with_a_dog,
    "bear": deal_with_a_bear,
    }

# Simulate, say, some words read from a file
words = ["cat", "bear", "cat", "dog"]

for word in words:
    # Look up the function to call for each word, then call it
    functionToCall = tokenDict[word]
    functionToCall()
    # You could also do it in one step, tokenDict[word]()
some_dict = { 'zope':'zzz', 'python':'rocks' }
another_dict = { 'python':'rocks', 'perl':'$' }

############

print("Intersects:", [k for k in some_dict if k in another_dict])

############

print("Intersects:", filter(another_dict.has_key, some_dict.keys()))
def sortedDictValues1(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]

############

def sortedDictValues2(adict):
    keys = adict.keys()
    keys.sort()
    return [adict[key] for key in keys]

############

def sortedDictValues3(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)
def qsort(L):
    if len(L) <= 1: return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1] + \
           qsort([ge for ge in L[1:] if ge >= L[0]])

############

def qs_test(length):
    import random
    joe = range(length)
    random.shuffle(joe)
    qsJoe = qsort(joe)
    for i in range(len(qsJoe)):
        assert qsJoe[i] == i, 'qsort is broken at %d!'%i

############

def qsort(L):
    if not L: return L
    pivot = L[0]
    def lt(x, pivot=pivot): return x<pivot
    def ge(x, pivot=pivot): return x>=pivot
    return qsort(filter(lt, L[1:]))+[pivot]+qsort(filter(ge, L[1:]))

import string

star_list = ['Elizabeth Taylor', 'Bette Davis', 'Hugh Grant', 'C. Grant']

star_list.sort(lambda x,y: (
   cmp(string.split(x)[-1], string.split(y)[-1]) or  # Sort by last name...
   cmp(x, y)))                                       # ...then by first name

print("Sorted list of stars:")
for name in star_list:
    print(name)

############

def sorting_criterion_1(data):
    return string.split(data)[-1]   # This is again the last name

def sorting_criterion_2(data):
    return len(data)                # This is some fancy sorting criterion

# Pack an auxiliary list:
aux_list = map(lambda x: (x,
                          sorting_criterion_1(x),
                          sorting_criterion_2(x)),
               star_list)

# Sort:
aux_list.sort(lambda x,y: (
   cmp(x[1], y[1])  or       # Sort by criteria 1 (last name)...
   cmp(y[2], x[2])  or       # ...then by criteria 2 (in reverse order)...
   cmp(x, y)))               # ...then by the value in the main list

# Unpack the resulting list:
star_list = map(lambda x: x[0], aux_list)

print("Another sorted list of stars:")
for name in star_list:
    print(name)

############

# Pack a better-ordered auxiliary list:
aux_list = map(lambda x: (sorting_criterion_1(x),
                          sorting_criterion_2(x),
                          x),
               star_list)

# Sort in a much simpler and faster way:
aux_list.sort()

# Unpack the resulting list:
star_list = map(lambda x: x[-1], aux_list)

############

# Pack a better-ordered auxiliary list yielding the desired order:
aux_list = map(lambda x: (sorting_criterion_1(x),
                          -sorting_criterion_2(x),
                          x),
               star_list)

############

import string
all_characters = string.maketrans('','')
all_characters_list = list(all_characters)
all_characters_list.reverse()
rev_characters = ''.join(all_characters_list)
rev_trans = string.maketrans(all_characters, rev_characters)

############

# Pack a better-ordered and corrected auxiliary list:
aux_list = map(lambda x: (string.translate(sorting_criterion_1(x), rev_trans),
                          sorting_criterion_2(x),
                          x),
               star_list)

# Sort in a much simpler and faster way AND get just the desired result:
aux_list.sort()

# Unpack the resulting list:
star_list = map(lambda x: x[-1], aux_list)
thelist.sort()
item_insert_point = bisect.bisect(thelist, theitem)
is_present = thelist[item_insert_point-1:item_insert_point] == [theitem]

############

is_present = thelist[item_insert_point-1] == theitem

############

somelist[x:x+1] == [somelist[x]]

############

is_present = thelist and thelist[item_insert_point-1] == theitem
import random

# an example of a processing function
def process(datum): print(datum)
# an example of a set of data to process
data = range(10000)

def process_all():
    random.shuffle(data)
    for elem in data: process(elem)

# or, if you need to preserve the data list's original ordering:
def process_all_preserved():
    aux = list(data)
    random.shuffle(aux)
    for elem in aux: process(elem)
thelist = list(thestring)

############

for c in thestring:
    do_something_with(c)

############

map(do_something_with, thestring)

chars = list(theline)

############

cuts = [8,14,20,26,30]
pieces = [ theline[i:j] for i, j in zip([0]+cuts, cuts+[sys.maxint]) ]

import string
def reindent(s, numSpaces):
    s = string.split(s, '\n')
    s = [(numSpaces * ' ') + string.lstrip(line) for line in s]
    s = string.join(s, '\n')
    return s

############

x = """line one
line two
and line three
"""

print(x)

print(reindent(x, 8))

############

def addSpaces(s, numAdd):
    white = " "*numAdd
    return white + white.join(s.splitlines(1))

def delSpaces(s, numDel):
    def aux(line, numDel=numDel, white=" "*numDel):
        if line[:numDel] != white:
            raise ValueError, "removing more spaces than there are!"
        return line[numDel:]
    return ''.join(map(aux, s.splitlines(1)))

def numSpaces(s):
    return [len(line)-len(line.lstrip()) for line in s.splitlines()]

############

def unIndentBlock(s):
    return delSpaces(s, min(numSpaces(s)))

############

print(ord('a'))
print(chr(97))

############

print(map(ord, 'ciao'))

############

print(''.join(map(chr, range(97, 100))))

############

largeString = small1 + small2 + ' something ' + small3 + ' yet more'

############

import operator
largeString = reduce(operator.add, pieces, '')

############

largeString = ''.join(pieces)
def containsAny(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    return 1 in [c in str for c in set]

def containsAll(str, set):
    """ Check whether sequence str contains ALL of the items in set. """
    return 0 not in [c in str for c in set]

############

[c in str for c in set]

############

1 in [c in str for c in set]

############

0 not in [c in str for c in set]

############

if __name__ == "__main__":
    # unit tests, must print("OK!" when run)
    assert containsAny('*.py', '*?[]')
    assert not containsAny('file.txt', '*?[]')
    assert containsAll('43221', '123')
    assert not containsAll('134', '123')
    print("OK!")

############

def containsAny(str, set):
    for c in set:
        if c in str: return 1
    return 0

def containsAll(str, set):
    for c in set:
        if c not in str: return 0
    return 1

############

big = little.upper()
little = big.lower()

############

print('one two three'.capitalize())
print('one two three'.title())

############

def iscapitalized(s):
    return s[:1].isupper() and s[1:].islower()

############

def iscapitalized(s):
    return s == s.capitalize()

############

'this is a literal string'
"this is another string"

############

'isn\'t that grand'
"isn't that grand"

############

big = "This is a long string\
that spans two lines."

############

big = "This is a long string\n\
that prints on two lines."

############
bigger = """
This is an even
bigger string that
spans three lines.
"""

############
big = r"This is a long string\
with a backslash and a newline in it"

############

mystr = "my string"
mystr[0]
mystr[-2]

############

mystr[1:4]
mystr[3:]
mystr[-3:]

############

list(mystr)

############

mystr+'oid'

############

'xo'*3

############

list_of_lines = one_large_string.splitlines()

############

one_large_string = '\n'.join(list_of_lines)

############

import random

def dice(num, sides):
    return reduce(lambda x, y, s=sides: x + random.randrange(s),
        range(num+1)) + num

############

def dice(num, sides):
    def accumulate(x, y, s=sides): return x + random.randrange(s)
    return reduce(accumulate, range(num+1)) + num

############

def dice(num, sides):
    return reduce(operator.add,
        [random.randrange(sides) for i in range(num)]) + num

############

def dice(num, sides):
    return reduce(operator.add, map(random.randrange, num*[sides])) + num

############

def every (pred, seq):
    """ true if pred(x) is true for all x in seq, else false """
    for x in seq:
        if not pred(x): return 0
    return 1

def any (pred, seq):
    """ false if pred(x) is false for all x in seq, else true """
    for x in seq:
        if pred(x): return 1
    return 0

############

every(lambda c: c > 5, (6, 7, 8, 9))
every(lambda c: c > 5, (6, 4, 8, 9))
any(lambda c: c > 5, (6, 7, 8, 9))
any(lambda c: c < 5, (6, 7, 8, 9))

############

def every(pred, seq): return len(seq) == len(filter(pred, seq))
def any(pred, seq): return len(filter(pred, seq))

############

import operator
def every(pred, seq):
    return reduce(operator.and_, map(pred, seq))
def any(pred, seq):
    return reduce(operator.or_, map(pred, seq))
