# Knock Knock

In the tradition of writing programs designed to taunt their users, let’s write a program that tells [a classic knock knock joke](http://jokes.cc.com/funny-food/panmgr/knock--knock----banana). To start you can copy this short program. Read the program first, see if you understand what it does, then run it to check if you were right.


```
    # knock_knock.py

    whos_there = input('Knock. Knock. ')
    banana_who = input('Banana. ')
    whos_there = input('Knock. Knock. ')
    banana_who = input('Banana. ')
    whos_there = input('Knock. Knock. ')
    banana_who = input('Banana. ')
    whos_there = input('Knock. Knock. ')
    orange_who = input('Orange. ')
    print('Orange you glad I didn't say banana? ')
```



## Being pedantic

You might have noticed that the program above will let the user type anything in response to the prompts from the computer. Edit the program to check if they said the right thing and chew them out if not.


## Don’t repeat yourself

It’s a bit annoying to have to type out the same lines over and over in out program. (we want to harass our users not ourselves) Create a function (or two, or more!) that does some of the repetitive work (Eg. You could have a function that says “Knock. Knock.” and checks the user’s response.)


## Being more pedantic.

Instead of just telling the user they typed the wrong response, we could make them type it over again too. Eg. you might print something like this:


```
    Knock. Knock. f
    You're supposed to say "Who's there?" Try Again.
    Knock. Knock. Who's there?
    Banana.
```


Hint: Try calling the function again.


## Don’t repeat yourself (more)

Our joke repeats the same 2 prompts (“Knock. Knock.” and “Banana”) three times, can you think of how you could avoid calling those functions three times? Hint: This is going to use recursion.


## Being even more pedantic.

I mean really if the user messes up your joke, you’re going to have to start all over right? Can you modify your program to start at the beginning of the joke any time the user messes up?
