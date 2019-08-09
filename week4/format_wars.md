


# FormatWars

This exercise will help you practise reading and writing files, especially in the JSON and CSV formats.


## Before you start

Download the [starwars dataset](swapi.zip) (curated from [https://swapi.co](https://swapi.co/).
Unzip the files and take a quick look at their contents.  You’ll notice that they are formatted as JSON.

When one file refers to the contents of another file (eg. listing the home planet of a character in the people.json), it just uses a number. That number is an index of the item in the other file, but watch out, these indexes start with 1 rather than with 0.


## Problem 1: The opening crawl

Every star wars movie begins with a paragraph or two of text that slowly marches up the screen. Lets see if we can make a short python program to simulate that.

First, let’s start by letting the user select which movie’s crawl to show. Create a new python file “crawl.py” and use argparse read the user’s selection and print it back to them. (It’s up to you to decide if you want the user to enter the title, episode number or something else to select a film.)

Next, read the films.json file and find the movie the user selected (be sure to show a helpful error message if you can’t find what they asked for). Print the “opening_crawl” text to the screen.

A [true Star Wars crawl ](https://www.youtube.com/watch?v=KDFqhXHD3yk)should march steadily up the center of the screen. Lets center our text, and print each line in a loop with a delay to give a little more authentic experience. (Bonus points for including the title and the ascii art “STAR WARS” at the top, but don’t spend too much time on it this is only problem 1!)


## Problem 2: Character stats

Next, let’s do a little analysis of our data. Create a new python program that creates a csv file with the index, name, height, mass and eye color for each character. What percentage of Star Wars characters have blue eyes? Add an option to this program to print the csv sorted by height or weight.

Let’s find out who is the tallest and the shortest character in each movie. Create another small python script to do this. For practice, read the list of characters per movie out of the films.json and the height of each character out of the csv file you just created. (You could take the csv file as an input parameter, and use the sort order of that file to determine whether you return the tallest or the shortest…) Print this result as a csv as well with columns for the movie title, character name and character height.


## Problem 3: General tools

If you think about it, every CSV file can be written as JSON. Each row becomes an object where the keys are the column names and the whole file is just an array of these objects. Write a script that takes a csv file as input and returns a JSON array as its output. (Bonus problem: We could make a converter from JSON array to CSV as well, but there are some edge cases to think about. How would you handle them? What options should your program offer?)
