# knock_knock.py

def knock_knock():
  whos_there = input('Knock. Knock. ')
  if whos_there != "Who's there?":
    print ("""You're supposed to say "Who's there?" Try Again. """)
    knock_knock()

knock_knock()
banana_who = input('Banana. ')
knock_knock()
banana_who = input('Banana. ')
knock_knock()
banana_who = input('Banana. ')
knock_knock()
orange_who = input('Orange. ')
print('Orange you glad I didn’t say banana? ')
