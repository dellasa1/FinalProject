from datetime import datetime
import random
import pickle
import tkinter

#class GUI:
    #def __init__(self):
        #self.mainWindow = 

#defines objects in the leaderboard list
class Leaders:
    def __init__(self, name, score, date):
        self.name = name
        self.score = score
        self.date = date                   
#Defines objects in the player high score dictionary
class PlayerScore:
    def __init__(self, name, score, date):
        self.name = name
        self.score = score
        self.date = date
    def setName(self, name):
        self.name = name
    def setScore(self, score):
        self.score = score
    def setDate(self, date):
        self.date = date
    def getName(self):
        return self.name
    def getScore(self):
        return self.score
    def getDate(self):
        return self.date
    def __str__(self):
        return 'Name: ' + self.name + \
            '\nScore: ' + self.score + \
                '\nDate: ' + self.date

play = 1
leader = 2
player = 3
playerSpec = 4
EXIT = 5
#files to store information in
topFile = 'leaderboard4.dat'
playerFile = 'playerStat4.dat'

def main():
    #gets lists from binary files
    leadList = getLeader()
    playHigh = getPlayerHigh()
    
    choice = 0
    while choice != EXIT:
        choice = getChoice()
        if choice == play:
            leadList, playHigh = playGame(leadList, playHigh)#
        if choice == leader:
            showLeader(leadList)
        if choice == player:
            playerHigh(playHigh)
        if choice == playerSpec:
            getSpec(playHigh)
    saveLeaders(leadList)
    saveplayHigh(playHigh)

def getLeader():
    try:
        infile = open(topFile, 'rb')
        leadList = pickle.load(infile)
        infile.close()
    except:
        leadList = []
    return leadList

def getPlayerHigh():
    try:
        infile = open(playerFile, 'rb')
        playHigh = pickle.load(infile)
        print(playHigh)
        infile.close()
    except:
        playHigh = {}
    return playHigh
    
#Gives user a choice for what to make the program do
def getChoice():
    print()
    print('1. Play the game')
    print('2. View the leaderboard')
    print('3. View all players high scores')
    print("4. Retrieve a specific player's high score")
    print('5. Exit the program')
    print()
    
    choice = int(input('Enter the number for an option above: '))
    while choice < play or choice > EXIT:
        choice = int(input('Enter a valid option: '))
    return choice
        
#plays the game
def playGame(leadList, playHigh):
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
#adds info and updates high score for each player
    playClass = PlayerScore(name, score, date)
    if name not in playHigh:
        playHigh[name] = playClass
        print('You have a high score')
    else:
        if score > playHigh[name].score:
            #del playHigh[name]
            playHigh[name] = playClass
            print('You have a NEW high score')

    #Prints info and adds it to the list
    print('Name: ', name, '\nScore: ',
          score, '\nDate: ', date)
    for x in leadList:#
        numObjects += 1#
    if numObjects < 5:#
        temp = Leaders(name, score, date)
        leadList.append(temp)
        print('You are one of the first people on the leaderboard')

    #add it, order it, then remove min
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

    return leadList, playHigh
#Displays the leaderboard
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
#Displays high score for each player
def playerHigh(playHigh):
    for x in playHigh:
        print()
        print(playHigh.get(x, 'Invalid'))
        print()

#Gets a specific player's high score
def getSpec(playHigh):
    specPlay = input('Enter a player name to see their highest score: ')
    print(playHigh.get(specPlay, "That name hasn't been used"))
def saveLeaders(leadList):
    outFile = open(topFile, 'wb')
    pickle.dump(leadList, outFile)
    outFile.close()
#stores the list and dictionary in separate files
def saveplayHigh(playHigh):
    outFile = open(playerFile, 'wb')
    pickle.dump(playHigh, outFile)
    outFile.close()
main()
