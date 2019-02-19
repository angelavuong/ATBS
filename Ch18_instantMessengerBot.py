# Write a program that will automatically send out a notification
# message to a select group of people on your friend list.
# Your program may have to deal with exceptional cases, such as
# friends being offline, the chat window appearing at different
# coordinates on the screen, or confirmation boxes that interrupt
# your messaging. Your program will have to take screen-shots to
# guide its GUI interaction and adopt ways of detecting when its
# virtual keystrokes aren’t being sent.

import pyautogui


x = 1069#x coordinates
y = 562#y coordinates

words = 'TEST' #insert text to transmit here
timesToTransmit = 5 #number of times to transmit

pyautogui.moveTo(x,y)

def spamThem():
    pyautogui.click()
    pyautogui.typewrite(words)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

for i in range(timesToTransmit):
    spamThem()
