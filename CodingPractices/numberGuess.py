import random

gameStat = True

while gameStat:
    num = random.randint(1, 100)
    attempts = 7
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
            
        attempts -= 1
        if guess < num:
            print("Too low!, You have {} attempts left.".format(attempts))
        elif guess > num:
            print("Too high!, You have {} attempts left.".format(attempts))
        else:
            print("Congratulations! You've guessed the number.")
            break 
        if attempts == 0:
            print("Sorry, you've run out of attempts. The number was {}.".format(num))
            break

    playOrquit = input("Play again: 'p'\nTo Quit: 'q'")
    
    if playOrquit == 'p':
        gameStat = True
    elif playOrquit == 'q':
        gameStat = False
        print("Thanks for playing!")    
    else:
        print("Invalid input. Exiting the game.")
        gameStat = False