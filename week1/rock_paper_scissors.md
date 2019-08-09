**(from the CS5 problem: [https://www.cs.hmc.edu/twiki/bin/view/CS5Fall07/RPSWeek0Gold](https://www.cs.hmc.edu/twiki/bin/view/CS5Fall07/RPSWeek0Gold))**

# A rock, paper, scissors program -- that _never_ loses...

This second problem asks you to practice

*   creating new python files (in this case, by copying old ones)
*   writing a bit of your own code (by altering another program, if you wish)
*   textual input and output in Python

The idea is this: alter the sample program below so that it invites the user to play a game of "rock-paper-scissors." What's more, the program should make sure that it _always_ wins the game (taunting the graders who will be running your program is optional).

## Creating a new python program

Copy the text below into your editor and save it as `rock_paper_scissors.py`:

```
    # Here is a short python program... try it out!
    import time          # includes a module named time
    import random        # a random module

    name = input('Hi... what is your name? ')
    print('')

    if name == 'Matt' or name == 'Matthew':
        print('I\'m "offline." Try later.')

    elif name == 'Zach':
        print('Zach Quinto!?!')
        time.sleep(.5)
        print('No?')
        time.sleep(.5)
        print('Meh.')

    else:
        print('Welcome,', name)
        my_choice = random.choice(['rock', 'paper', 'scissors'])
        print('By the way, I choose', my_choice)
        print('')
```

Open the terminal and run this new program with python3. Play around with it to see what it does. When you’re ready to make your game go on to the next section.

**How the program should work**

*   The program should ask the user to choose rock, paper, or scissors. Then, it should repeat back to the user their choice, it should "reveal" its own choice, and then report the results. The program should always win -- of course, it will be cheating because it will know and use the opponent's input, but we will leave a true implementation of the game to next week. Briefly, in the game of [rock-paper-scissors](http://www.worldrps.com/), rock defeats scissors, scissors defeat paper, and paper defeats rock.
*   You may assume that the user will input one of rock, paper, or scissors. (But feel free to catch errors and report them, if you like!)
*   Too much time on your hands? Extend the game into [RPS-25](http://www.umop.com/rps25.htm), a strict superset of RPS.
*   You may write the dialog however you like, but here's an example dialog if you'd like one to follow. This is two distinct runs of the program:

        ```
        >>>
        Choose rock, paper, or scissors: scissors

        You chose scissors - I chose rock
        I win!
        >>>
        Choose rock, paper, or scissors: paper

        You chose paper - I chose scissors
        I win!
        >>>
        ```

*   Note that taunting and/or praising the user with your dialog is encouraged -- though less and less so as the class wears on and they become increasingly sleep-deprived.
