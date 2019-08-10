## Filter, Map, Reduce, Count and Sort

Today’s reading introduced some very useful “higher-order functions”: `map`, `reduce` and `filter`. In today’s exercise, we will implement these functions for ourselves and practice using them. At the end you’ll also master a classic technical coding interview question: sorting a list.


### Filter, map and reduce

For each function we’ve provided a description and a few test cases you can use. (Remember that a “predicate” is just a function that returns a boolean(True or False)):


```
    def filter(pred, l):
        """ Accepts a predicate (pred) and a list (l).
            Returns a new list containing only the items from l
            where pred(l) matches (returns true).
        """

    assert filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]
    assert filter(lambda x: x % 3 != 0, [1, 2, 3, 4, 5]) == [1, 2, 4, 5]

    def map(func, l):
        """ Accepts a function (func) and a list (l).
            Returns a new list that is the result of applying func
            to every element of l.
        """

    assert map(lambda x: x * 2, [1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]
    assert map(len, ['hello', 'bob']) == [5, 3]

    def reduce(func, l, init):
        """ Accepts a function of two arguments (func), a list (l) and an
            initial value. Applies func cumulatively to the items of l
            from left to right, starting with the value in init,
            so as to reduce the list to a single value.
        """

    assert reduce(lambda x, y: x + y , [1, 2, 3, 4, 5], 0) == 15
    assert reduce(lambda x, y: x * y , [1, 2, 3, 4, 5], 1) == 120
    assert reduce(lambda x, y: x + ' ' + y , ['hello', 'bob'], '') == ' hello bob'
```



### Counting

With recursion, `map/reduce/filter `and list comprehensions at our disposal we can make a new function, `count`, to count how many items in a list match what we’re looking for.


```
    def count(pred, l):
            """ Accepts a predicate (pred) and a list (l).
            Returns the number of items in l where pred(l) matches (returns true).
        """

    assert count(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == 2
    assert count(lambda x: x % 3 != 0, [1, 2, 3, 4, 5]) == 4
```


Lets implement `count` a few different ways and compare them:



1. Just using recursion
2. Using `filter`
3. Using `map` and `reduce`
4. Using a list comprehension

[N.b.](https://en.wikipedia.org/wiki/Nota_bene) Python doesn’t mind if you define the same function multiple times in the same file, it will just always use the most recent definition. Eg. this python file:


```
    def foo(x):
        return x+1

    print foo(10)

    def foo(x):
        return x*2

    print foo(10)
```


Prints the following:


```
11
20
```



### Sorting a binary list

Design and write a function named blsort(L), which will accept a list `L `and should return a list with the same elements as` L`, but in ascending order. (Note: the second character is an "ell" for "list", not a 1 or an "i"!) blsort *ONLY NEEDS TO HANDLE LISTS OF BINARY DIGITS*, that is, this function can and should assume that L will always be a list containing only 0s and 1s. Eg:


```
    blsort([1, 0, 1]) == [0, 1, 1]
    blsort([0, 1, 1, 0, 1, 0]) == [0, 0, 0, 1, 1, 1]
```


You may not call Python's built-in sort function to solve this problem! Also, you should not use your own sort (asked in a question below), but you may use any other technique to implement `blsort`. In particular, you might want to think about how to take advantage of the constraint that the argument will be a binary list—this is a considerable restriction! (Hint: the `count` function you just wrote could come in handy.) Remember to document and test your function.


### Sorting any list

A classic programming interview question you might be asked is to write a function to sort a list. It’s not a particularly good question since the “correct” solution is widely published all over the internet and it is something you’d never do in your day job since pretty much every language has an efficient sort method built in. However, people still ask it, and it’s pretty easy to implement a fairly efficient recursive solution. The algorithm we’ll implement is called “merge sort” and it works like this:



1. If the list has 1 or fewer elements, it’s already sorted. (ie. the base case)
2. Otherwise, divide the list roughly in half, and sort each half. (ie. recurse)
3. Finally, merge the two sorted lists into a single sorted list to return. (Use another recursive function here as a helper function.)

Remember, the best place to start is defining the function, writing the doc string and a few test cases.


### Bonus

If you get done early feel free to try some of the other problems here:

[https://www.cs.hmc.edu/twiki/bin/view/CS5/CaesarCipherGold](https://www.cs.hmc.edu/twiki/bin/view/CS5/CaesarCipherGold)

