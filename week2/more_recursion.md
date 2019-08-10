##More recursion

**Number of digits in a number**: We can determine how many digits a positive integer has by repeatedly dividing by 10 (without keeping the remainder) until the number is less than 10, consisting of only 1 digit. We add 1 to this value for each time we divided by 10. Implement this recursive algorithm in Python and test it using a main function that calls this with the values 15, 105, and 15105.

**Max in list**: Write a recursive Python function that has a parameter representing a list of integers and returns the maximum stored in the list. Thinking recursively, the maximum is either the first value in the list or the maximum of the rest of the list, whichever is larger. If the list only has 1 integer, then its maximum is this single value, naturally.

**isPalindrome**: Write a recursive function that determines if a string is a palindrome

**Eat Chocolate**: https://www.geeksforgeeks.org/program-chocolate-wrapper-puzzle/.

**Find files with python**: We just learned about the `find` command on Saturday, which is used to find files with specific characters in their names. Can you do the same thing in python? (Hint: checkout the `listdir` function in the `os` module (https://docs.python.org/3/library/os.html)

