class Leaders:
    def __init__(self, name, score, date):
        self.__name = name
        self.__score = score
        self.__date = date
#This stuff was used when using a dictionary, I'll keep it just in case it's useful
    #def setName(self, name):
    #    self.__name = name
    #def setScore(self, score):
    #    self.__score = score
    #def setDate(self, date):
    #    self.__date = date
    #def getName(self):
    #    return self.__name
    #def getScore(self):
    #    return self.__score
    #def getDate(self):
    #    return self.__date
    def __str__(self):
        return f'{self.__name} -- {self.__score} -- {self.__date}'
        #'Name: ' + self.__name + \
            #'\nScore: ' + self.__score + \
            #'\nDate: ' + self.__date
                   

#class PlayerScore:
    #def __init__(self, password, strength):
    #    self.__password = password
    #    self.__strength = strength
    #def setPass(self, password):
    #    self.__password = password
    #def setStr(self, strength):
    #    self.__strength = strength
    #def getPass(self):
    #    return self.__password
    #def getStr(self):
    #    return self.__strength
    #def __str__(self):
    #    return 'Password: ' + self.__password + \
    #           '\nPassword Strength: ' + self.__strength

from datetime import datetime
import random
import pickle

play = 1
leader = 2
playerHigh = 3
playerSpec = 4
EXIT = 5
DEL = 6

topFile = 'leaderboard.dat'

def main():
    leadList = getLeader()
    
    choice = 0
    while choice != EXIT:
        choice = getChoice()
        if choice == play:
            playGame(leadList)
        if choice == leader:
            showLeader(leadList)
        if choice == playerHigh:
            playerHigh()
        if choice == playerSpec:
            playerSpec()
        if choice == DEL:
            delete(leadList)
    saveLeaders(leadList)

def getLeader():
    try:
        infile = open(topFile, 'rb')
        leadList = pickle.load(infile)
        infile.close()
    except:
        leadList = []
    return leadList

#def getPlayerHigh():

    
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
    leadClass = Leaders(name, score, date)#might not be needed
    for x in leadList:#
        numObjects += 1#
    if numObjects < 5:#
        leadList[name] = leadClass#--------- where leadClass.score >= min(list)
        print('You are one of the first people on the leaderboard')

    #add it, remove the min, then order it v
    else:
        if score > leadList[name].score:
            leadList[name] = leadClass 
        #leadClass = Leaders(name, score, date)
        
   # if leadList[score] >= min
        


#Displays the leaderboard
#Might do it different so it can be sorted and displayed, or sort it somewhere else
def showLeader(leadList):
    #sort(leadList)
    for x in leadList:
        print()
        print(leadList.get(x, 'Invalid'))
        print()

#function for sorting list
#def sort(leadList):
    #leadList = sorted(leadList, key=lambda x: x.score, reverse=True)
    #return leadList

#stores the high score for each player
#def playerHigh():

#Gets a specific player's high score
#def playerSpec():

def saveLeaders(leadList):
    outFile = open(topFile, 'wb')
    pickle.dump(leadList, outFile)
    outFile.close()

#temporary (for convenience)
def delete(leadList):
    leadList.clear()
main()
