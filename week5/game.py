from vpython import *
from robot import *
import random
import math
import ipywidgets as widgets

# variable declarations
global userbot
global running
running = True
GROUND_RADIUS = 50
ZOMBIES = 20

# declare our buttons
fastButton = widgets.Button(description = 'F', width = '60px', height = '60px')
slowButton = widgets.Button(description = 'S', width = '60px', height = '60px')
leftButton = widgets.Button(description = 'L', width = '60px', height = '60px')
rightButton = widgets.Button(description = 'R', width = '60px', height = '60px')
fillerButton0 = widgets.Button(description = '', width = '60px', height = '60px')
resetButton = widgets.Button(description = 'Reset', width = '120px', height = '60px')
quitButton = widgets.Button(description = 'Quit', width = '120px', height = '60px')
fillerButton1 = widgets.Button(description = '', width = '120px', height = '60px')
scene.caption = "To use the directional pad, click on a marked direction. F = Faster, S = Slower, L = turn Left and R = turn Right."

# These functions set up our buttons to read in inputs
def fastButton_handler(s):
    global userbot
    userbot.speed += 0.1
fastButton.on_click(fastButton_handler)

def slowButton_handler(s):
    global userbot
    userbot.speed -= 0.1
slowButton.on_click(slowButton_handler)

def leftButton_handler(s):
    global userbot
    userbot.turn(5)
leftButton.on_click(leftButton_handler)

def rightButton_handler(s):
    global userbot
    userbot.turn(-5)
rightButton.on_click(rightButton_handler)

def quitButton_handler(s):
    global running
    running = False
    print("Exiting the main loop. Ending this vPython session...")
quitButton.on_click(quitButton_handler)

def display(container):
  pass

# now arrange and display our GUI
container0 = widgets.HBox(children = [fillerButton0, fastButton, fillerButton0, quitButton])
container1 = widgets.HBox(children = [leftButton, fillerButton0, rightButton, fillerButton1])
container2 = widgets.HBox(children = [fillerButton0, slowButton, fillerButton0, fillerButton1])
display(container0)
display(container1)
display(container2)

def main():
    global userbot
    global running
    ground = cylinder(pos = vector(0, -1, 0),
                      axis = vector(0, 1, 0),
                      radius = GROUND_RADIUS)
    userbot = PlayerBot()
    zombies = makeZombies()
    while running:
        rate(30)
        userbot.update()
        if mag(userbot.position) >= GROUND_RADIUS:
            userbot.turn(180)
        for z in zombies:
            z.update()
            if mag(z.position) >= GROUND_RADIUS:
                z.turn(random.uniform(150, 210))

def makeZombies():
    zombies = []
    for z in range(ZOMBIES):
        theta = random.uniform(0, 360)
        r = random.uniform(0, GROUND_RADIUS)
        x = r * cos(math.radians(theta))
        z = r * sin(math.radians(theta))
        zombies.append(ZombieBot(position = vector(x, 0, z)))
    return zombies
main()
