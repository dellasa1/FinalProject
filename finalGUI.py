from datetime import datetime
import random
import pickle
from tkinter import *
import tkinter.messagebox
global score
score = 0

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
#This gui helps to display the game in a user interface
#First initialize creates a dropdown menu
class myGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Play", command=self.game)
        fileMenu.add_command(label="Exit", command=self.master.destroy)
        menu.add_cascade(label="File", menu=fileMenu)
#helps to display score after playing the game
        self.frame = tkinter.Frame(self.master)

        self.var = tkinter.StringVar()
        self.score = tkinter.Label(self.frame, textvariable=self.var)

        self.score.pack(side='left')#close, ask hardy to look at it

        self.frame.pack()
#Gets user name and goes to game
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
#guess the coin and goes to check if it's right
    def getCoin(self):
        self.getCoinWindow = tkinter.Tk()
        
        self.coinFrame = tkinter.Frame(self.getCoinWindow)

        self.coinFlip = tkinter.Label(self.coinFrame, text="Enter 'heads' or 'tails':")
        self.coinFlipGet = tkinter.Entry(self.coinFrame, width=5)

        self.coinFlip.pack(side='left')
        self.coinFlipGet.pack(side='left')

        self.coinNext = tkinter.Frame(self.getCoinWindow)

        self.coinFlipGo = tkinter.Button(self.coinNext, text='Check', command=self.check)
        self.coinFlipGo.pack(side='left')

        self.coinFrame.pack()
        self.coinNext.pack()
#this checks to see if the guess is correct
#I'm trying to have it use a while loop but it hasn't been liking it
    def check(self):
            
        score = 0
        flip = self.coinFlipGet.get()
        
        coin = random.randint(1, 2)
        
        if flip == 'heads':
            if coin == 1:
                tkinter.messagebox.showinfo("That's correct!")
                
                score+=1
            elif coin == 2:
                tkinter.messagebox.showinfo("That's incorrect!")
                
                playing = False
                self.gameWindow.destroy()
        elif flip == 'tails':
            if coin == 1:
                tkinter.messagebox.showinfo("That's incorrect!")
                
                playing = False
                self.gameWindow.destroy()
            elif coin == 2:
                tkinter.messagebox.showinfo("That's correct!")
                
                score+=1
        else:
            tkinter.messagebox.showinfo("Try again")
#This returns the info to the original window to display
        now = datetime.now()
        print()
        date = str(now.strftime("%I:%M%p on %B %d, %Y"))
        score = str(score)
        name = self.namein.get()
        self.temp = ('Name: ', name, '\nScore: ',
          score, '\nDate: ', date)
        self.var.set(str(self.temp))
#Helps to set up dropdown menu in original window
root = Tk()
app = myGUI(root)
root.wm_title("Tkinter window")
root.mainloop()
