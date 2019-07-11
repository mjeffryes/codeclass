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