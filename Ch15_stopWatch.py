import time
import pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
raw_input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1
res = []
# Start tracking the lap times.
try:
    while True:
        raw_input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        output = ('Lap #' + str(lapNum) + ':').ljust(7) + (('  %s ') % (totalTime)).rjust(5) + (('(  %s)') % (lapTime)).rjust(2)
        print output
        res.append(output)
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
       # Handle the Ctrl-C exception to keep its error message from displaying.
        # Clipboard Output
        clipOutput = ''
        for lap in res:
            clipOutput += lap + "\n"
        pyperclip.copy(clipOutput)
        print('\nDone.')
