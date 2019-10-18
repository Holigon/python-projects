import time

# - Functions - #
 
def dogSit():
    
    # Data    
    treatsEaten = 0
    treatsToSit = 50

    # While Command | Will keep running until treatsEaten >= treatsToSit      
    while treatsEaten < treatsToSit:
        
        # To insure the initial message won't keep on displaying
        if treatsEaten == 0: 
            print('\nArthur has not eaten enough treats to sit yet.') 

        # User input of how many treats will be given the Arthur the dog
        # Using "try and catch" method to ensure input will be positive interger
        while True:
            try:
                giveTreatAmount = int(input('How many treats do you want to give to Arthur?: '))
            except ValueError:      # Ensure integer
                print("\nYou have to use numbers to say how many treats Arthur will get! Try again.\n")
                continue
            
            if giveTreatAmount < 0: #Ensure positve
                print("\nYou can't take treats from Arthur! You monster! Please don't use negative numbers.\n")
                continue
            else:
                break # Input was parsed
        treatsEaten += giveTreatAmount
    
        # If you give Arthur too many treats (>100) the game will print a Game over screen
        # Using "raise SystemExit" the program will end after the Game over screen
        if treatsEaten > 100:
            print("\nOh no! You have given too many treats to Arthur, and now he is sick!")
            print("Now he will never learn to sit :-( ")
            gameOver =  r'''

            G A M E  O V E R

              /^-----^\\
              V  o o  V
               |  Y  |
                \ Q /
                / - \\
                |    \\
                |     \     )
                || (___\====

                        '''
            print(gameOver)
            time.sleep(0.8)
            replayLose()
        
        # Using the break function the program will go to the Victory Condition if treatsEaten >= treatsToSit
        # This is done to skip the treatData_1 message, as not to show two similar messages
        elif (treatsEaten >= treatsToSit):
            break

        # Using .format to insert variables into middle of string
        treatData_1 = "\nArthur has now eaten {} treats, and he needs {} treats to learn to sit\n"
        print(treatData_1.format(treatsEaten,treatsToSit - treatsEaten))
    

    # Victory Condition | Arthur the dog has gotten enough treats to finally want to learn to sit!
    treatData_2 = "\nArthur has now eaten {} treats, and has learned to sit! Congratulations!"
    print(treatData_2.format(treatsEaten))
    dogPic = r'''

             V I C T O R Y !

            |\_/|                  
            | @ @   Woof! 
            |   <>              _  
            |  _/\------____ ((| |))
            |               `--' |   
        ____|_       ___|   |___.' 
        /_/_____/____/_______|
              
            '''
    
    print(dogPic)
    time.sleep(0.8)

def replayWin():
    
    # Message
    print("\n\nCongratulations, you have won the game! Do you wan't to play again?")
    
    # Y/N Input
    while True:
        replayInput = str(input("Type 'Y' for Yes | Type 'N' for No (Y/N): ")).upper()
        if replayInput not in ('Y','N'):
            print("Please choose a valid choice\n")
        else:
            break

    if replayInput == "Y":
        print("\nRestarting game")
        time.sleep(0.8)
        print(".")
        time.sleep(0.8)
        print(".")
        time.sleep(0.8)
        print(".")
        time.sleep(0.8)
        startProgram()
    
    elif replayInput == "N":
        print("Quitting game")
        time.sleep(0.8)
        print(".")
        time.sleep(0.8)
        print(".")
        time.sleep(0.8)
        print(".")
        time.sleep(0.2)
        print("\nGoodbye")
        time.sleep(0.6)
        raise SystemExit
    
    else:
        print("Error. This should not ever happen. Good job")
        time.sleep(0.5)
        raise SystemExit    

def replayLose():
    
    # Message
    print("\nOh no, you lost the game! Do you wan't to try again?")
    
    # Y/N Input
    while True:
        replayInput_2 = str(input("Type 'Y' for Yes | Type 'N' for No (Y/N): ")).upper()
        if replayInput_2 not in ('Y','N'):
            print("Please choose a valid choice\n")
        else:
            break

    if replayInput_2 == "Y":
        print("\nRestarting game")
        time.sleep(0.8)
        print(".")
        time.sleep(0.8)
        print(".")
        time.sleep(0.8)
        print(".")
        time.sleep(0.8)
        startProgram()
    
    elif replayInput_2 == "N":
        print("Quitting game")
        time.sleep(0.8)
        print(".")
        time.sleep(0.8)
        print(".")
        time.sleep(0.8)
        print(".")
        time.sleep(0.2)
        print("\nGoodbye")
        time.sleep(0.6)
        raise SystemExit
    
    else:
        print("Error. This should not ever happen. Good job")
        time.sleep(0.5)
        raise SystemExit    

def introStory():
    story = r'''

                    A R T H U R  T H E  D O G

                          / \__
                         (    @\___
                         /         O
                        /   (_____/  < HELP ME LEARN TO SIT
                       /_____/   U

   Arthur is your new dog, and you want to teach him to sit on command.
      He is a stubborn dog, and refuses to follow your instructions.
        Give him the treats he needs to finally listen to you!
              Be careful not to overfeed him though.

    '''
    print(story)

def startProgram():
    introStory()
    dogSit()
    replayWin()

# - Execution of Program - #

startProgram()
