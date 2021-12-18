#Import modules
import time
import random

#Welcome Screen
print('''
        WELCOME TO ROCK PAPER SCISSORS
----------------------------------------------

        Please select an option:
    1. Play
    2. How to Play
    3. Credits
    4. High Scores
    5. Exit


''')

main_choice = input('Please enter the number that matches your choice:\n')
#Make sure that user enters a number
while True:
    try:
        int(main_choice)
        break
    except:
        main_choice = input('Please enter a NUMBER:\n')


#Play
if main_choice == 1:

#How to Play
elif main_choice == 2:


#Credits
elif main_choice == 3:

#High Scores
elif main_choice == 4:
        
#Exit
elif main_choice == 5:
    print('Goodbye, you are just mad that you lost all of your matches...')

    
