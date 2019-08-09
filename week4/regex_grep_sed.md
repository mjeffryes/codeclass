# Regular expressions, grep and sed

## Introduction

A regular expression, often called a **pattern**, is an expression used to specify a set of strings required for a particular purpose. A simple way to specify a finite set of strings is to list its elements or members. However, there are often more concise ways to specify the desired set of strings. For example, the set containing the three strings "Handel", "Händel", and "Haendel" can be specified by the **pattern** `H(ä|ae?)ndel`; we say that this pattern **matches** each of the three strings. (wikipedia)

Today we’ll be practicing using regular expressions, sometimes shortened to “regex” to find and replace text using python and the common command line tools `grep` and `sed.`

## Problem 0: Regular expression basics

Follow the tutorial on [https://regexone.com](https://regexone.com/) to learn basic regular expression syntax. Try to complete some of the practise problems too. (But don’t get stuck on any one problem for too long, we’ve got other things to do as well.)

## Problem 1: Using regular expressions in Python

Now we’re going to try to use regular expressions in Python to find phone numbers in a file and print them neatly.


First, [download the data files](https://github.com/mjeffryes/codeclass/releases/download/phone_chellenge_data/phone_number_challenge_data.zip).  In that archive you will find several text files. These files each have many phone numbers embedded in their text. The phone numbers may be written in a variety of different formats eg.  +44 (123) 456-7890, 1-123-456-7890, 123.456.7890. (Note: there are over 200 files and more than 1.6M phone numbers in the sample.)

Next, copy [cat.py](cat.py); cat.py is an example program that reads and prints the contents of any file passed as its argument.
This will give you a starting point for writing your own program.

Your job is to write a program to find all the phone numbers in a file and print them in a consistent format (what format you use for the output is up to you). You might find [this reference](https://regexone.com/references/python) page helpful for information on using regular expressions in python. You might also use [https://regexr.com/](https://regexr.com/) to test out your regular expression on some sample text.

## Using grep and sed

You may have noticed that we have lots of files to search and our program can only read one file at a time. While we could update our python program to traverse the directory and search multiple files, these kinds of search and replace actions are so common that there are dedicated command line tools to do it. We’ll use `grep` to find all the phone numbers in all the files and then use `sed` to rewrite them into our desired output format.


### Grep

You may remember from [learn enough command line to be dangerous](https://www.learnenough.com/command-line-tutorial?single_page=1) that `grep` is a program used for searching files to fine lines that contain specific text. In fact, `grep` accepts regular expressions to specify what lines to return.

In order to search all the files in a directory you’ll need the `-r` option. To return just the part of the text that matched rather than the whole line use the` -o` option. Depending on how you built your pattern, you may also need to use the `-E` option, which enables full regex mode. (`grep` originally shipped with a stripped down version of regular expressions, which is still the default decades later. Backwards compatibility is a pain.) Your final command will look something like this:

```
$ grep -r -o -E "Your pattern here" directory_to_search/
```

Note: You might need to use `-P` instead of `-E` in some versions of grep

### Sed

While `grep` can only be used to find a pattern files, `sed` (the “**s**tream **ed**itor”) can both find and replace using a pattern. (Actually, `sed` can do a lot more than that, but find and replace is all most people ever learn. The man page for `sed` is super dense, for a deeper dive into what it can do I recommend: [https://www.grymoire.com/Unix/Sed.html](https://www.grymoire.com/Unix/Sed.html))

The basic structure of your sed command will be:

```
$ sed 's/pattern/replacement/'
```

In order to format your output, you’ll need to create groups in your pattern and refer to them in your replacement. You can drop the contents of the first group into your replacement with \1 the second group with \2 and so on. Eg. if we had a list of names written as “ firstname lastname” and wanted to rewrite them to be “lastname, firstname”  the sed command might be:

`$ sed 's/\([A-Z][a-z]*\) \([A-Z][a-z]*\)/\2, \1/'`

(More elaboration here: [https://www.grymoire.com/Unix/Sed.html#uh-4](https://www.grymoire.com/Unix/Sed.html#uh-4))

### Putting it together

To find and format the files in one command, we just need to pipe the output of grep into sed:

```
$ grep -r -o -E "Your pattern here" directory_to_search/ | sed 's/pattern/replacement/'
```

## Bonus: More fun with regexes

*   Regular expressions are implemented using state machines this short tutorial will walk you through how: [http://www.postcrashgames.com/finitris/](http://www.postcrashgames.com/finitris/)
*   Did you know that you can play crosswords with regular expressions? [https://regexcrossword.com/](https://regexcrossword.com/)
