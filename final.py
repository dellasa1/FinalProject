#abilities to get the current time of score
from datetime import datetime
#helps to get a random #
import random

def main():
    #gets choice from user and performs program accordingly
    playGame()

#def getPlayerHigh():

#The player plays the game (heads/tails) and recieves an output of
#their name, their score, and the date
def playGame():
    score = 0
    playing = True
    name = input('Enter player name (or nickname):')
    while playing:
        flip = input("Enter 'heads' or 'tails': ")
        coin = random.randint(1, 2)
        #print(coin)
        if flip == 'heads':
            if coin == 1:
                print("That's correct!")
                score+=1
            if coin == 2:
                print("That's incorrect!")
                playing = False
        if flip == 'tails':
            if coin == 1:
                print("That's incorrect!")
                playing = False
            if coin == 2:
                print("That's correct!")
                score+=1
        else:
            print('Try Again')
    now = datetime.now()
    print()
    print('Name: ', name, '\nScore: ',
          score, '\nDate: ', now.strftime("%m/%d/%Y %H:%M"))

#set up for future pieces of program
#def showLeader():

#def playerHigh():

#def playerSpec():
    
main()
