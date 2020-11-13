from microbit import *
import random
scissor = Image("99009:"
              "99090:"
              "00900:"
              "99090:"
              "99009")
paper = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999")
rock = Image("00000:"
              "09990:"
              "09990:"
              "09990:"
              "00000")
game = [rock, paper, scissor]
while True:
    if accelerometer.was_gesture('shake'):
        display.show(random.choice(game))
        sleep(2000)
        display.clear()