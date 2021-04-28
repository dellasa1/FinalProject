from datetime import datetime
import random
import pickle
from tkinter import *
import tkinter.messagebox
#global final
#final = 0

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

class myGUI(Frame):
    def __init__(self, master=None):
        #global self.final
        self.final = tkinter.IntVar()
        self.date = tkinter.StringVar()
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Play", command=self.game)
        fileMenu.add_command(label="Exit", command=self.master.destroy)
        menu.add_cascade(label="File", menu=fileMenu)

        self.frame = tkinter.Frame(self.master)

        self.var = tkinter.StringVar()
        self.score = tkinter.Label(self.frame, textvariable=self.var)

        self.score.pack(side='left')#close, ask hardy to look at it
        
        #self.name1 = tkinter.Label(self.frame, text="Enter name before playing")
        #self.name1in = tkinter.Entry(self.frame, width=10)
        
        #self.name1.pack(side='left')
        #self.name1in.pack(side='left')

        self.frame.pack()

    def game(self):#, final
        #self.final = final
        self.gameWindow = tkinter.Tk()

        self.frame1 = tkinter.Frame(self.gameWindow)
        self.frame3 = tkinter.Frame(self.gameWindow)

        self.getName = tkinter.Label(self.frame1, text='Enter player name (or nickname):')
        self.namein = tkinter.Entry(self.frame1, width=12)


        self.getName.pack(side='left')
        self.namein.pack(side='left')

        #self.coinFlip = tkinter.Label(self.frame3, text="Enter 'heads' or 'tails':")
        #self.coinFlipGet = tkinter.Entry(self.frame3, width=5)

        #self.coinFlip.pack(side='left')
        #self.coinFlipGet.pack(side='left')

        #self.flip = tkinter.Label(self.frame3, text="Enter 'heads' or 'tails': ")
        #self.flipIn = tkinter.Entry(self.frame3, width=5)
        self.flipGo = tkinter.Button(self.frame3, text="Guess coin", command=self.getCoin)

        #self.flip.pack(side='left')
        #self.flipIn.pack(side='left')
        self.flipGo.pack(side='left')
        
        self.frame1.pack()
        self.frame3.pack()
    def getCoin(self):
        self.getCoinWindow = tkinter.Tk()

        #self.getCoinFrame = tkinter.Frame(self.getCoinWindow)

        #score = 0
        #numObjects = 0
        #playing = True
        #self.getName2 = tkinter.Label(self.getCoinFrame, text="Enter player name (or nickname):")
        #self.name = tkinter.Entry(self.getCoinFrame, width=12)

        #self.getName2.pack(side='left')
        #self.name.pack(side='left')

        #self.getCoinFrame.pack()
        #while playing:
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
    def check(self):
        self.temp = ''
        #final = 0
        playing = True
        #while playing:

        flip = self.coinFlipGet.get()
        coin = random.randint(1, 2)
        if flip == 'heads':
            if coin == 1:
                tkinter.messagebox.showinfo("That's correct!")
                #correct = "That's correct!"
                #self.final+=1
                self.final.set(self.final.get() + 1)
                #self.getCoin()
            elif coin == 2:
                tkinter.messagebox.showinfo("That's incorrect!")
                #correct = "That's incorrect!"
                playing = False
                self.getCoinWindow.destroy()
        elif flip == 'tails':
            if coin == 1:
                tkinter.messagebox.showinfo("That's incorrect!")
                #correct = "That's incorrect!"
                playing = False
                self.getCoinWindow.destroy()
            elif coin == 2:
                tkinter.messagebox.showinfo("That's correct!")
                #correct = "That's correct!"
                #self.final+=1
                self.final.set(self.final.get() + 1)
                #self.getCoin()
        elif flip != 'heads' or flip != 'tails':
            tkinter.messagebox.showinfo("Try again")
            #correct = "Try again"
        if playing == False:

            now = datetime.now()
            print()
            self.date.set(now.strftime("%I:%M%p on %B %d, %Y"))
            date = str(self.date.get())
            tempFinal = str(self.final.get())
            name = self.namein.get()
            self.temp = 'Name: ' + name + '\nScore: ' + tempFinal + '\nDate: ' + date
            self.var.set(self.temp)
            self.gameWindow.destroy()
            #score = 0
        else:
            self.finalWindow = tkinter.Tk()
            self.finalFrame = tkinter.Frame(self.finalWindow)
            self.finalButton = tkinter.Button(self.finalFrame, text='Guess again', command=lambda: [self.getCoin, self.finalWindow.destroy()])
            self.finalButton.pack(side='left')
            self.finalFrame.pack()
            

root = Tk()
app = myGUI(root)
root.wm_title("Tkinter window")
root.mainloop()
