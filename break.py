import time
import winsound


while True:
    seconds = int(input('How many minutes would you like a break for? '))
    minutes = seconds * 60
    time.sleep(minutes)
    winsound.PlaySound('sound',winsound.SND_FILENAME)
    print('End of the time')

    prompt = input('Go again? Type yes or y: ')

    if prompt == 'yes' or prompt == 'y':
        continue
    else:
        break
