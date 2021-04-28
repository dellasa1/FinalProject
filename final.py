#need to get the current date
from datetime import datetime
#To flip the coin
import random
#for storing the files
import pickle
#for using the GUI
from tkinter import *
import tkinter.messagebox

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

#Main class for the GUI, uses a 'Frame' to help display a dropdown menu for the user
class myGUI(Frame):
    def __init__(self, master=None):
        self.topFile = 'leaderboard.dat'
        self.playerFile = 'playerStat.dat'
        #retrieves the leaderboard list from a file
        def getLeader():
            try:
                infile = open(self.topFile, 'rb')
                leadList = pickle.load(infile)
                infile.close()
            except:
                leadList = []
            return leadList
        #retrieves the player high dictionary from a file
        def getPlayerHigh():
            try:
                infile = open(self.playerFile, 'rb')
                playHigh = pickle.load(infile)
                infile.close()
            except:
                playHigh = {}
            return playHigh

        self.leadList = getLeader()
        self.playHigh = getPlayerHigh()
        #some variables to access in different parts of the code
        #These store the information for each time a user plays the game
        self.user =tkinter.StringVar()
        self.final = tkinter.IntVar()
        self.date = tkinter.StringVar()

        #Configures the main window
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)
        #This configure the drop-down menu to give the user options on what
        #to make the program do. Each tab calls a function lower in the program
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Play", command=self.game)
        fileMenu.add_command(label="Leaderboard", command=self.leaderboard)
        fileMenu.add_command(label="All Player highs", command=self.getplayHigh)
        fileMenu.add_command(label="Get Specific Player high", command=self.getSpecPlayer)
        fileMenu.add_command(label="Exit", command=self.exit)
        menu.add_cascade(label="File", menu=fileMenu)
        #This frame will display the information after each time the game is played
        #This will also be used to display the leaderboard list and to display the information
        #in the player highs dictionary
        self.frame = tkinter.Frame(self.master)

        self.var = tkinter.StringVar()
        self.outPut = tkinter.Label(self.frame, textvariable=self.var)

        self.outPut.pack(side='left')

        self.frame.pack()
    #When the program ends, it destroys the window after saving the information to the appropriate
    #files with the leader list and the player high dictionary
    def exit(self):
        def saveLeaders(leadList):
            outFile = open(self.topFile, 'wb')
            pickle.dump(leadList, outFile)
            outFile.close()

        def saveplayHigh(playHigh):
            outFile = open(self.playerFile, 'wb')
            pickle.dump(playHigh, outFile)
            outFile.close()

        saveLeaders(self.leadList)
        saveplayHigh(self.playHigh)
        self.master.destroy()
    #This function takes the updated leaderboard list and displays the information from it 
    #The user is able to see what the high scores are in order
    def leaderboard(self):
        def showLeader(leadList):
            leadTemp = ""
            leadList = sort(leadList)
            numbers = ['1st', '2nd', '3rd', '4th', '5th']
            for x in leadList:
                first = str(numbers[0] + ': ')
                del numbers[0]
                second = str(f'Name: {x.name}\nScore: {x.score}\nDate: {x.date}')
                
                leadTemp += ('\n' + first + second + '\n')
            self.var.set(leadTemp)

        def sort(leadList):
            leadList = sorted(leadList, key=lambda x: x.score, reverse=True)
            return leadList
        
        showLeader(self.leadList)
    #This function gets every player high from the player high dictionary
    #Whenever the game is played this will be updated to keep the high score for each user that has played the game
    def getplayHigh(self):
        def playerHigh(playHigh):
            anotherTemp = ""
            for x in playHigh:
                anotherTemp += "\n" + str(playHigh.get(x, 'Invalid')) + "\n"
                #print(playHigh.get(x, 'Invalid'))
            self.var.set(anotherTemp)
                
        playerHigh(self.playHigh)
    #This function allows the user to see the high score for a specific user
    def getSpecPlayer(self):
        self.specWindow = tkinter.Tk()
        self.specFrame = tkinter.Frame(self.specWindow)
        self.specLabel = tkinter.Label(self.specFrame, text='Enter a username to see their highest score: ')
        self.specEntry = tkinter.Entry(self.specFrame, width=12)
        self.specButton = tkinter.Button(self.specFrame, text='Go', command=lambda: [self.getSpec(), self.specWindow.destroy()])
        self.specLabel.pack(side='left')
        self.specEntry.pack(side='left')
        self.specButton.pack(side='left')
        self.specFrame.pack()
    def getSpec(self):
        playHigh = self.playHigh
        getting = str(playHigh.get(self.specEntry.get(), "That name hasn't been used"))
        self.var.set(getting)
    # This is where the game is played. The program first prompts the user to enter their name
    # Then they press a button to flip and guess the coin
    def game(self):
        self.gameWindow = tkinter.Tk()

        self.frame1 = tkinter.Frame(self.gameWindow)
        self.frame3 = tkinter.Frame(self.gameWindow)

        self.getName = tkinter.Label(self.frame1, text='Enter player name (or nickname):')
        self.namein = tkinter.Entry(self.frame1, width=12)

        self.getName.pack(side='left')
        self.namein.pack(side='left')

        self.flipGo = tkinter.Button(self.frame3, text="Guess coin", command=self.getCoin)

        self.flipGo.pack(side='left')
        
        self.frame1.pack()
        self.frame3.pack()
    # The user now guesses how the coin will flip. Then 
    # the program will go to a different function to see if the user guessed right
    def getCoin(self):
        self.getCoinWindow = tkinter.Tk()

        self.coinFrame = tkinter.Frame(self.getCoinWindow)
        self.coinNext = tkinter.Frame(self.getCoinWindow)
        self.coinLast = tkinter.Frame(self.getCoinWindow)

        self.coinFlip = tkinter.Label(self.coinFrame, text="Enter 'heads' or 'tails':")
        self.coinFlipGet = tkinter.Entry(self.coinFrame, width=5)

        self.coinFlip.pack(side='left')
        self.coinFlipGet.pack(side='left')

        self.coinFlipGo = tkinter.Button(self.coinNext, text='Check', command=self.check)

        self.coinFlipGo.pack(side='left')

        self.coinFrame.pack()
        self.coinNext.pack()
    # This function will check if the user guessed correctly
    def check(self):
        #sorts a list
        def sort(leadList):
            leadList = sorted(leadList, key=lambda x: x.score, reverse=True)
            return leadList
        self.checkWindow = tkinter.Tk()
        self.checkFrame = tkinter.Frame(self.checkWindow)
        
        playing = True
        #this is the section that retrieves the user's guess and determines if it's right or not
        flip = self.coinFlipGet.get()
        coin = random.randint(1, 2)
        if flip == 'heads':
            if coin == 1:
                self.checkLabel = tkinter.Label(self.checkFrame, text="That's correct!")
                self.final.set(self.final.get() + 1)
            elif coin == 2:
                tkinter.messagebox.showinfo("That's incorrect!")
                playing = False
                self.getCoinWindow.destroy()
        elif flip == 'tails':
            if coin == 1:
                tkinter.messagebox.showinfo("That's incorrect!")
                playing = False
                self.getCoinWindow.destroy()
            elif coin == 2:
                self.checkLabel = tkinter.Label(self.checkFrame, text="That's correct!")
                self.final.set(self.final.get() + 1)
        elif flip != 'heads' or flip != 'tails':
            self.checkLabel = tkinter.Label(self.checkFrame, text="Try Again")
        #if the user guessed wrong then the information from their game will
        #be returned to the main window to display how many guesses in a row the user got correct. This will be the user's score
        if playing == False:
            self.checkWindow.destroy()

            now = datetime.now()
            self.date.set(now.strftime("%I:%M%p on %B %d, %Y"))
            date = str(self.date.get())
            score = str(self.final.get())
            self.user.set(self.namein.get())
            name = self.user.get()
            self.temp = 'Name: ' + name + '\nScore: ' + score + '\nDate: ' + date
            self.var.set(self.temp)
            self.gameWindow.destroy()#--------------------------------------------
            #This stores the players score in the high score dictionary.
            #if they have a new High score it will store it
            playClass = PlayerScore(name, score, date)
            if name not in self.playHigh:
                self.playHigh[name] = playClass
            else:
                if score > self.playHigh[name].score:
                    self.playHigh[name] = playClass
                    tkinter.messagebox.showinfo('You have a NEW high score')
            #Now the program will determine if the user's score is high enough to make the leaderboard
            #If the user scored higher than the lowest score on the leaderboard, it will be added to the
            #list and the scoreboard will be adjusted accordingly. If there are less than 5 objects, or scores,
            #on the list, the score will automatically be added
            numObjects = 0
            for x in self.leadList:
                numObjects += 1
            if numObjects < 5:
                temp = Leaders(name, score, date)
                self.leadList.append(temp)
                tkinter.messagebox.showinfo('You made the leaderboard')

            else:
                tempList = []
                for x in self.leadList:
                    tempList += x.score
                
                if score >= min(tempList):
                    temp = Leaders(name, score, date)
                    self.leadList.append(temp)
                    tkinter.messagebox.showinfo('You made the leaderboard')
                    self.leadList = sort(self.leadList)
                    del self.leadList[5:]
                else:
                    tkinter.messagebox.showinfo("You didn't make the leaderboard")
            self.final.set(0)
            self.getCoinWindow.destroy()
        #If the user guessed right then the program will tell them so and prompt the user to flip
        # the coin again. They will return to the guessing window and can enter their guess again.
        #The user will keep guessing until they get a wrong answer, then their final score will be displayed
        else:
            self.checkButton = tkinter.Button(self.checkFrame, text="Flip Again", command=lambda:[self.getCoin, self.checkWindow.destroy()])
            self.checkLabel.pack(side='left')
            self.checkButton.pack(side='left')

            self.checkFrame.pack()
            
root = Tk()
app = myGUI(root)
root.wm_title("Tkinter window")
root.mainloop()
