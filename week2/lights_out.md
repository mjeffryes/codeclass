## **Evolving Lists and Lights Out!**

**The bird's-eye view**

The end goal of this lab is to build a game called "Lights On" or "Lights Out," the goal of which is to get all of a grid of (initially random) lights to be on (or off). Each time the user selects a light, that light toggles from 0 to 1 or from 1 to 0. The challenge is that **_the neighboring light(s) ALSO toggle_**. That is, the one, two, three or four lights directly to the N, S, E and W of the selected light also change state (either on to off, or off to on). In our game, the lights do **_not_** "wrap around": e.g., the leftmost light is **not** a neighbor to the rightmost light.

You can play a 2d version of Lights Out here: [http://www.logicgamesonline.com/lightsout/](http://www.logicgamesonline.com/lightsout/)

You'll implement a 1d version in this exercise…

This exercise will guide you in developing several Python functions that will allow you to implement this game.


### **Planning and Setup—starting files for download**

You may have noticed that this task (programming Lights On) is bigger than what we've asked you to do so far. This program will require more than one function, and you will have to do some planning about how to organize the data the game needs to keep track of and how the functions interact and modify this data.

   [Here is a link to the starter files for this lab.](http://www.cs.hmc.edu/~cs5grad/hw3pr1.zip)

To start, download from the above link, copy the file into your codeclass directory and open it with your editor. You'll see a standard header and two initial functions:


```
    #
    # Lights out in 1D
    #

    import time           # provides time.sleep(0.5)
    from random import *  # provides choice([0,1]), etc.
    import sys            # larger recursive stack
    sys.setrecursionlimit(10000) # 10000 stack frames available

    def mutate(i, oldL):
        """ Accepts an index (i) and an old list (oldL).
            mutate returns the ith element of a NEW list!
            * Note that mutate returns ONLY the ith element
              mutate thus needs to be called many times in evolve.
        """
        new_ith_element = 1 + oldL[i]
        return new_ith_element

    def evolve(oldL, curgen = 0):
        """ This function should evolve oldL (a list)
            it starts at curgen, the "current" generation
            and it ends at generation #5 (for now)


            It works by calling mutate at each index i.
        """
        print oldL,                    # print the old list, L
        print "  (gen: " + str(curgen) + ")"  # and its gen.
        time.sleep(0.25)


        if curgen == 5:  # we're done!
            return       # no return value... yet
        else:
            newL = [ mutate(i, oldL) for i in range(len(oldL)) ]
            return evolve(newL, curgen + 1)
```



#### **Try it out…**

Although the lab will lead you through the decomposition of this problem and composition of its solution, it's a good idea to run the provided code and read it through to gain an intuitive understanding of its structure.

Try out the call:


```
>>> evolve([1,2,3], 0)
[1, 2, 3]  (g: 0)
[2, 3, 4]  (g: 1)
[3, 4, 5]  (g: 2)
[4, 5, 6]  (g: 3)
[5, 6, 7]  (g: 4)
[6, 7, 8]  (g: 5)
```


and read through both the evolve function and the mutate function so that this behavior makes sense!

Note that we abbreviated gen with g in the printing above—certainly feel free to adapt the printing to be as you'd like it!

Next, try out the same call to evolve **_without_** its second argument:


```
>>> evolve([1,2,3])   # notice this has only one argument
[1, 2, 3] (g: 0)
[2, 3, 4] (g: 1)
[3, 4, 5] (g: 2)
[4, 5, 6] (g: 3)
[5, 6, 7] (g: 4)
[6, 7, 8] (g: 5)
```


Here, you are seeing Python's ability to use _default argument values_. A function can include a default value when it is declared:


```
def evolve(oldL, curgen=0):
```


and, when no argument is provided, it will use that default value. Note that the default values have to be _later_ in the list of arguments than the non-default values. Otherwise Python won't know where to put the arguments provided!


### First steps: new version of mutate

You may have noticed that the `mutate` function is “hard-coded” into the implementation of `evolve`. For each of the following questions we’re going to define a new function to mutate the list, so we need to modify `evolve` to add a new parameter for the mutate method: change line 20 like this:


```
def evolve(oldL, mutate, curgen = 0):
```


And change line 35 like this:


```
evolve(newL, mutate, curgen + 1)
```


Now you can call the `evolve` method like this:


```
    >>> evolve([1,2,3], mutate)
    [1, 2, 3] (g: 0)
    [2, 3, 4] (g: 1)
    [3, 4, 5] (g: 2)
    [4, 5, 6] (g: 3)
    [5, 6, 7] (g: 4)
    [6, 7, 8] (g: 5)
```


**Question 0**

Write a `timesTwo` function that yields the following behavior. Note that we're still calling `evolve`, but it's `timesTwo` that you're writing

```
>>> evolve([1,2,3], timesTwo)
[1, 2, 3] (g: 0)
[2, 4, 6] (g: 1)
[4, 8, 12] (g: 2)
[8, 16, 24] (g: 3)
[16, 32, 48] (g: 4)
[32, 64, 96] (g: 5)
```

**Answer to Question 0**

The idea here is that each element in the return value from `timesTwo` is double the corresponding element in the original argument. Thus, the code is the following, simply cut, pasted, and modified from the old mutate:

```
def timesTwo(i, oldL):

    """ Accepts an index (i) and an old list (oldL).

        mutate returns the ith element of a NEW list!

        * Note that mutate returns ONLY the ith element

          mutate thus needs to be called many times in evolve.

    """

    new_ith_element = 2 * oldL[i]

    return new_ith_element
```

**Question 1**

Write a `sqr` function that yields the following behavior:

```
>>> evolve([1,2,3], sqr)
[1, 2, 3] (g: 0)
[1, 4, 9] (g: 1)
[1, 16, 81] (g: 2)
[1, 256, 6561] (g: 3)
[1, 65536, 43046721] (g: 4)
[1, 4294967296L, 1853020188851841L] (g: 5)
```

**Hint**: notice that each element is the _square_ of the one above it…

**Question 2**

This example uses a slightly longer initial list. Write a rot function that yields the following behavior:

```
>>> evolve([1,2,3,42], rot)
[1, 2, 3, 42] (g: 0)
[42, 1, 2, 3] (g: 1)
[3, 42, 1, 2] (g: 2)
[2, 3, 42, 1] (g: 3)
[1, 2, 3, 42] (g: 4)
[42, 1, 2, 3] (g: 5)
```

**Hint**: each of `rot`’s returned values is the value from the old list, `oldL` that is located one index to the left (lower) than the current index. Thus, the return line will be

`return oldL[ SOMETHING ]`

where SOMETHING is a very short expression involving `i` and `1`.

**Question 3: A _random_ list generator…**

Write a rand function that yields a random list of 0s and 1s with each generation. It completely ignores the argument list! For example (and lots of other output behaviors could occur, as well):

```
>>> evolve( [1,2,3,42], rand )  # this argument list is ignored!
[1, 2, 3, 42] (g: 0)
[1, 0, 0, 0] (g: 1)
[0, 1, 1, 1] (g: 2)
[0, 1, 1, 1] (g: 3)
[1, 0, 0, 0] (g: 4)
[1, 0, 0, 1] (g: 5)
```

**Reminder**: the function that chooses an element randomly from a list is called as follows:

```choice([0, 1])```

That's all you'll need! (_No need to create lists or list comprehensions here!_ Keep in mind that evolve already does that for you, and your function produces **_only one element at a time_**—namely, element `i`.)

The next part of the lab will build on this randomly-evolving behavior.


### **Lab 3 Part 1: Counting generations**

At the moment, your different mutate functions have directed evolve to change its argument lists in a number of ways, but it so far has not evolved them for any concrete purpose or to achieve any particular result.

In the game of Lights On, the goal is to evolve the list so that all of its values are "on". Throughout the rest of the lab, we will use 1 to indicate that a cell is "on" and 0 to indicate that it is "off". In this portion of the lab, we will experiment with several strategies for evolving a list into a same-length list of all 1s. From now on, our initial lists will consist only of 0s and 1s.


##### **Detecting when we've reached our goal**

In your `hw3pr1.py` file, write a function named `allOnes(L)` that accepts a list of numbers `L`, returns `True` if all of `L`'s elements are 1, and returns `False` otherwise. Raw recursion is one good way to do this, though not the only one. Notice that the empty list vacuously satisfies the all-ones criterion, because it has no elements at all! Here are some examples to check:

```
>>> allOnes([1,1,1])
True

>>> allOnes([])
True

>>> allOnes([ 0, 0, 2, 2 ])     # this should be False!
False    # but be careful... if you use sum(L) == len(L), this will be True

>>> allOnes([ 1, 1, 0 ])
False
```

**Hint**: if you use recursion, a natural base case would be to handle the empty list `[]`. Note that `allOnes([])` is `True`!

**Caution about True/False!**

Especially if you use recursion, you may want to use the line

`return True`

somewhere in your code, as well as the line

`return False`

Be **sure** to return (and not print) these values!

Also, watch out that you're returning the _values_ True and False.

You **DON'T** want to return the strings "True" and "False"!


##### **An improved evolve function**

Now that you have a function for testing whether a list is all ones, improve your evolve function in two ways:



*   First, change the base case condition so that it stops when the argument list is all 1s. Use your `allOnes` function!
*   Second, change evolve so that it **_returns_** the number of generations that were needed to evolve the argument into all 1s.

**Suggestions**:

*   Leave the print and time.sleep lines _before_ the check to see if the all-ones base case has been reached. That way they will run both when it's the base case and when it's the recursive case.


##### **Trying it out**

First, you might want to reduce (or remove) pause produced by the line `time.sleep(0.25)`. A value of a twentieth of a second (or zero) might be better for these trials.

Then, try your new evolve function and your random-number-generating mutate functions on argument lists of different lengths—after all, their elements are not being used yet. Here are two examples:

```
>>> evolve( [0,0,0,0,1], rand )
[0, 0, 0, 0, 0]
[1, 0, 1, 1, 1]
[1, 1, 0, 0, 0]
[1, 0, 1, 0, 1]
[1, 0, 0, 0, 1]
[1, 1, 1, 1, 0]
[0, 1, 1, 0, 0]
[1, 1, 0, 1, 0]
[0, 0, 1, 1, 0]
[0, 1, 1, 1, 1]
[1, 1, 1, 0, 0]
[1, 1, 0, 1, 0]
[1, 1, 1, 1, 1]
12
```

```
>>> evolve( [0,1,0,1], rand )
[0, 1, 0, 1]
[0, 0, 0, 0]
[0, 1, 0, 1]
[1, 1, 0, 1]
[1, 1, 1, 1]
4
```

It's worth mentioning that it can take _much_ longer for a 5-element list to randomly come up all-1s. One test we ran took 93 steps….

As a thought experiment, how many steps would you _expect_—over many trials—for a 5-element list to randomly generate all 1s?

**Please add a short comment answering this question at this point in your code.**


#### **Lab 3 Part 2: User input**

At the moment, your evolver for lists does not use any _human_ input. This section adds your input to the game—first by toggling each light individually and then to toggle a light and all of its neighbors simultaneously. This will implement the full game of _Lights On_!


##### **Evolving lists _with user input_**

The approach to evolving lists thus far is, well, a bit too random. This section will enable the user to guide the process by choosing an element from the list.

First, copy this `turn_on_one` function:

```
def turn_on_one(i, oldL, target = 0):

    """ Accepts an index (i), an old list (oldL) and the index to turn on (target).

        turn_on_one returns the ith element of a NEW list!

        * Note that turn_on_one returns ONLY the ith element

          turn_on_one thus needs to be called many times in evolve.

    """

    if i == target:

        new_ith_element = 1       # this makes the game easy!

    else:

        new_ith_element = oldL[i] # the new is the same as the old

    return new_ith_element
```

This function takes a third argument, named `on_index`. This third argument will be the index the user chooses. Note that this new function changes AT MOST the single element that matches the argument named `on_index`. All other returned values are simply the old values `oldL[i]`.

Next, change the line in evolve that reads

```newL = [ mutate(i,oldL) for i in range(len(oldL)) ]```

and replace it with these two lines in its place:

```
user = int(input("Index? "))
newL = [ mutate(i,oldL,user) for i in range(len(oldL)) ]
```

which asks the user for an index value, puts the user's input into the variable name user, and then passes that variable into the mutate function as its third argument.

Try running evolve( [0,0,0,0], turn_on_one ). Now, the execution should pause and wait for you to enter the index of one of the list items.

Here is an example run of ours:

```
>>> evolve( [0,0,0,0], turn_on_one )
[0, 0, 0, 0] (g: 0)
Index? 3
[0, 0, 0, 1] (g: 1)
Index? 2
[0, 0, 1, 1] (g: 2)
Index? 1
[0, 1, 1, 1] (g: 3)
Index? 0
[1, 1, 1, 1] (g: 4)
4
```

It's clear we need to add some additional challenge to this game!


#### **Toggling the lights**

**Change the above **turn_on_one** function** into a toggle function so that when the user chooses a light, then that light will _toggle_ from 0 to 1 or from 1 to 0, as appropriate.

**Hint**: if the old value of the light is oldL[i], what will you get if you subtract that value from 1?

Be sure to test your code by running something like this:

```
>>> evolve( [1,0,1,1], toggle )
[1, 0, 1, 1] (g: 0)
Index? 2
[1, 0, 0, 1] (g: 1)
Index? 3
[1, 0, 0, 0] (g: 2)
Index? 1
[1, 1, 0, 0] (g: 3)
Index? 2
[1, 1, 1, 0] (g: 4)
Index? 3
[1, 1, 1, 1] (g: 5)
5
```

**Hint**: In your toggle function you will want to use an if and an else. Consider testing whether i is the same value as target, that is, i == target

At this point, it's a game, it's still not really a challenge to win. You'll fix that next…


#### **Toggling neighboring lights, too**

**Finishing the game**

Now, you are finally ready to implement the full 1D version of "Lights On".

Modify the toggle function's code so that the game play is as it should be—that is, when you toggle one light, the lights next to it also toggle.

**Suggestions**: Only toggle needs to change. Remember that toggle only returns the ith element—there’s no way to change that (with our current design). However, you can make the test for when to toggle the lights more inclusive!

For example, above you allowed the light to toggle ONLY when i == target. Now, you'll want to have a test with some other possibilities as well—that is,

`if i == target or    ...     :`

For what other values of i would we want to toggle the lights?

Try your game from a known starting position to test it out:

```
>>> evolve( [1,0,0,1,0,0,1,1], toggle )
[1, 0, 0, 1, 0, 0, 1, 1] (g: 0)
Index? 4
[1, 0, 0, 0, 1, 1, 1, 1] (g: 1)
Index? 2
[1, 1, 1, 1, 1, 1, 1, 1] (g: 2)
2
```

```
>>> evolve( [0,0,0,0,0,0,0,0], toggle )
[0, 0, 0, 0, 0, 0, 0, 0] (g: 0)
Index? 0
[1, 1, 0, 0, 0, 0, 0, 0] (g: 1)
Index? 3
[1, 1, 1, 1, 1, 0, 0, 0] (g: 2)
Index? 7
[1, 1, 1, 1, 1, 0, 1, 1] (g: 3)
Index? 6
[1, 1, 1, 1, 1, 1, 0, 0] (g: 4)
Index? 7
[1, 1, 1, 1, 1, 1, 1, 1] (g: 5)
5
```

We still need a random starting point—that's next!


#### **Starting from a random binary list**

Create a function which will output a random binary list (a random list of N zeros and ones):

`randBL(N)`

The function randBL should take in a nonnegative integer, N and should return a list of length N, in which each element is randomly either a 0 or a 1.

Raw recursion is one way to handle this; list comprehensions are another. **Warning**: One thing that _won't_ work is the following:

```return [ choice([0,1]) ] * N   # won't work!!```

The reason is that the above line only returns a list of N zeros or N ones.

Here are two examples of randBL in action—be sure to test your function, though the outputs are likely to be different:

```
>>> randBL( 5 )
[1, 0, 1, 1, 0]

>>> randBL( 9 )
[0, 0, 1, 1, 1, 0, 1, 1, 0]

```

This randBL function makes it easy to start a new, random game.

Also, you should feel free to change the formatting of your printed output to make the game easier to play. For example, you might:



*   Print a list of the indices above the current game state
*   Let the Index? question come at the end of the previous line

or any other formatting you might like. Here's what ours turned out to be:

```
>>> evolve(randBL(8), toggle)
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 1, 0, 1, 1, 0, 0] (g: 0) Index? 1

[0, 1, 2, 3, 4, 5, 6, 7]
[1, 0, 0, 0, 1, 1, 0, 0] (g: 1) Index? 2

[0, 1, 2, 3, 4, 5, 6, 7]
[1, 1, 1, 1, 1, 1, 0, 0] (g: 2) Index? 7

[0, 1, 2, 3, 4, 5, 6, 7]
[1, 1, 1, 1, 1, 1, 1, 1] (g: 3)

3
```

#### **Let the computer play!?**

To finish things up, write a new version of evolve so that the computer gets to play! That is, have the computer choose (randomly) one of the possible indices in place of the line that currently lets the user (human) provide input. Hint: rather than calling input directly inside evolve, we could add a new parameter to evolve, that returns a target index when it is called.

That's it—once you make the switch from human choice of a square to a computer-made, random choice, the machine should play the game (making random selections) until it's solved.

**Warning**: one-sixth of all binary lists are dead ends! That is, there is **no** combination of toggled lights that will end up at the all-ones list. So, if the computer (or you) seems unable to solve one of the starting configurations, hit Control-C and try again!

**Congratulations!**

