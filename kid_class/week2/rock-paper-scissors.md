## A Rock, Paper, Scissors Program
(Borrowed from [CSforAll - RockPaperScissors](https://www.cs.hmc.edu/twiki/bin/view/CSforAll/RockPaperScissors))

This problem asks you to practice:
- Creating new Python files (in this case, by copying old ones or starting with the code below)
- Writing a bit of your own code (by altering our starter program, if you wish)
- Text-based input and output in Python
### Start With a New File
Start by typing in the following code, which gets you on the way:
```python
import random          # imports the library named random

""" this plays a game of rock-paper-scissors
	(or a variant of that game)
	arguments: no arguments    (prompted text doesn't count as an argument)
	results: no results        (printing doesn't count as a result)
"""
user = input("Choose your weapon: ")
comp = random.choice(['rock','paper','scissors'])
print()

print('The user (you)   chose', user)
print('The computer (I) chose', comp)
print()

if user == 'rock':
	print('Ha! I really chose paper--I WIN!')

print("Better luck next time...")
```
### What's Next? What's Required?
- From the terminal—and from within the correct directory!—run the file with `python FILE_NAME`
- The basic requirements are these: use the starter code (below) to create a program that:
- Invites the user to play a game of "rock-paper-scissors."
- Lets the user choose from at least three options
	- They don't have to be rock, paper, and scissors—feel free to vary the actors!
	- _**But your program does have to work differently for each of three distinct inputs**_ (well, _at least_ three inputs)
- Your program is welcome to play an honest game of RPS
	- But you're also welcome to create a player that always wins (or, if you prefer, that always loses)
- Your program should echo the choice the user made
	- You may assume the user will type her/his choice correctly, for your game's choices...
- Your program should reveal the choice that it makes (whether fair or not)
- Your program should print out who won that round (or whether it was a tie, or some other outcome)
### More Details
- In brief, the program should ask the user to choose rock, paper, or scissors (or your own variants!). Then it should repeat that choice back to the user, reveal its own choice, and finally report the results. The program can play fairly, can always win, or can always lose—it's up to you. If RPS is unfamiliar, in the game of [rock-paper-scissors](http://www.worldrps.com/), rock defeats scissors, scissors defeat paper, and paper defeats rock.
- You may assume that the user will input one of rock, paper, or scissors. Case matters! We'll stick with lower case...
- You may write the dialog however you like—below is an example dialog if you'd like one to follow. We are _**positive**_ that you can improve on this interaction, however! Here are two distinct runs of the program:
```
Choose your weapon: rock
The user (you)   chose rock
The computer (I) chose scissors

Ha! I really chose paper--I WIN!
Better luck next time...
```
```
Choose your weapon: paper
the user (you)   chose paper
the computer (I) chose dynamite

Dynamite!? I REALLY WIN!
You can't play again.
```
### Other Possibilities
- Too much time on your hands? Add "lizard" and "spock" as noted at http://www.samkass.com/theories/RPSSL.html.  
 - Want your program to continue playing many times? Use a `while True:` loop.  We'll provide two examples instead of detailed explanations:
```python
	while True:
		print("Still running...")
		response = input("Play again? ")
		if response == 'n':
			break

	# Annother possibility:
	running = True
	while running:
		response = input("Play again? ")
		if response == 'n':
			running = False```
```
