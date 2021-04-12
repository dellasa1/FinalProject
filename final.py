#This class helps to store the list in the binary file with objects
class Leaders:
    def __init__(self, name, score, date):
        self.name = name
        self.score = score
        self.date = date                   

from datetime import datetime
import random
import pickle

play = 1
leader = 2
playerHigh = 3
playerSpec = 4
EXIT = 5
DEL = 6

#files to store information in
topFile = 'leaderboard3.dat'
playerFile = 'playerStat.dat'

def main():
    #retrieve lists from binary files
    leadList = getLeader()
    #playHigh = getPlayerHigh()
    
    choice = 0
    while choice != EXIT:
        choice = getChoice()
        if choice == play:
            leadList = playGame(leadList)#, playHigh
        if choice == leader:
            showLeader(leadList)
        if choice == playerHigh:
            playerHigh()
        if choice == playerSpec:
            playerSpec()
        if choice == DEL:
            delete(leadList)
    saveLeaders(leadList)
    #saveplayHigh(playHigh)

def getLeader():
    try:
        infile = open(topFile, 'rb')
        leadList = pickle.load(infile)
        print(leadList)
        infile.close()
    except:
        leadList = []
    return leadList

#def getPlayerHigh():
    #try:
        #infile = open(playerFile, 'rb')
        #playHigh = pickle.load(infile)
        #infile.close()
    #except:
        #playHigh = []
    #return playHigh

#Gets user choice for what to make the program do
def getChoice():
    print()
    print('1. Play the game')
    print('2. View the leaderboard')
    print('3. View all players high scores')
    print("4. Retrieve a specific player's high score")
    print('5. Exit the program')
    #Temporary deletion of dictionary from file
    print('6. delete dictionary from file')
    print()
    
    choice = int(input('Enter the number for an option above: '))
    while choice < play or choice > DEL:
        choice = int(input('Enter a valid option: '))
    return choice

#Play the game
def playGame(leadList):
    score = 0
    numObjects = 0
    playing = True
    name = input('Enter player name (or nickname):')
    while playing:
        flip = input("Enter 'heads' or 'tails': ")
        coin = random.randint(1, 2)
        print(coin)
        if flip == 'heads':
            if coin == 1:
                print("That's correct!")
                score+=1
            elif coin == 2:
                print("That's incorrect!")
                playing = False
        elif flip == 'tails':
            if coin == 1:
                print("That's incorrect!")
                playing = False
            elif coin == 2:
                print("That's correct!")
                score+=1
        else:
            print('Try Again')
    now = datetime.now()
    print()
    date = str(now.strftime("%I:%M%p on %B %d, %Y"))
    score = str(score)

    #Prints info and adds it to the list
    print('Name: ', name, '\nScore: ',
          score, '\nDate: ', date)
    for x in leadList:
        numObjects += 1
    if numObjects < 5:
        temp = Leaders(name, score, date)
        leadList.append(temp)
        print('You are one of the first people on the leaderboard')

    #add it, order it, then remove the min v
    else:
        tempList = []
        for x in leadList:
            tempList += x.score
        
        if score >= min(tempList):
            temp = Leaders(name, score, date)
            leadList.append(temp)
            print('You made the leaderboard')
            leadList = sort(leadList)
            del leadList[5:]
        else:
            print("You didn't make the leaderboard")        

    return leadList
#Displays the leaderboard correctly from the list, specifying what place each score is
def showLeader(leadList):
    leadList = sort(leadList)
    numbers = ['1st', '2nd', '3rd', '4th', '5th']
    for x in leadList:
        print(numbers[0], ': ')
        del numbers[0]
        print(f'Name: {x.name}\nScore: {x.score}\nDate: {x.date}')
        print()

def sort(leadList):
    leadList = sorted(leadList, key=lambda x: x.score, reverse=True)
    return leadList
#stores the high score for each player
#def playerHigh():

#Gets a specific player's high score
#def playerSpec():

def saveLeaders(leadList):
    outFile = open(topFile, 'wb')
    pickle.dump(leadList, outFile)
    outFile.close()


#def saveplayHigh(playHigh):
    #outFile = open(playerFile, 'wb')
    #pickle.dump(playHigh, outFile)
    #outFile.close()
def delete(leadList):
    leadList.clear()
main()

