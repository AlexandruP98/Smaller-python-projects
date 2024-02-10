#this is a program that will give the user a break when he needs it, it will prompt him for the minutes, convert his answer into minutes, and play a small alarm when the time expires, if the user needs another break
#he can prompt the program "yes" or "y" to be asked again

import time
import winsound


while True:
    while True:
        try:
            seconds = int(input('How many minutes would you like a timer for? '))
            break
        except ValueError:
            print('Please type a number')
    minutes = seconds * 60
    time.sleep(minutes)
    winsound.PlaySound('sound',winsound.SND_FILENAME)
    print('End of the time')

    prompt = input('Go again? Type yes or y: ')

    if prompt == 'yes' or prompt == 'y':
        continue
    else:
        break
