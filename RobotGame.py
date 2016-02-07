import sys

from tkinter import *

class userInterface():

    def __init__ (self, window):
        # Initializes the first window
         
        self.window = window
        self.menuCanvas = Canvas(self.window, width=300, height=300, bg='white')
        self.menuCanvas.pack(fill=BOTH, expand=1)

        self.buttonFrame = Frame(self.menuCanvas)
        self.buttonFrame.pack(side="top", pady=25)

        self.startButton = Button(self.menuCanvas, text="Play game", command = lambda: self.loadGameArena())
        self.startButton.pack()

        self.settingsButton = Button(self.menuCanvas, text="Settings")
        self.settingsButton.pack()

        self.exitButton = Button(self.menuCanvas, text="Exit", command = lambda: self.window.destroy())
        self.exitButton.pack()

    def settings(self):
        pass

    def loadGameArena(self):
        # Eventually this will have a new game/load game option prior to loading the actual game
        self.menuCanvas.pack_forget()
        theGame = theRobotGame(self.window)

class theRobotGame():

    
    
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x600+200+60")
        self.createMap()
        self.robot = self.zone.create_rectangle(10, 10, 20+20, 20+20)
        self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
        self.robotLocation = 1
        
    def createMap(self):
        self.zone = Canvas(self.window, width=1000, height=600, bg='white')
        self.zone.pack(fill=BOTH, expand=1)
        
        #teleport1 = self.zone.create_line
        self.zone.x_min = 0
        self.zone.y_min = 0
        self.zone.x_max = 991
        self.zone.y_max = 600
        self.keyboardMovement()

    def keyboardMovement(self):
        # Temporary movement for testing purposes
        def rightKey(event):
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)

            if self.x2 >= self.zone.x_max:
                self.zone.coords(self.robot, self.x1, self.y1, self.x2, self.y2)
            else:
                self.zone.coords(self.robot, self.x1+10, self.y1, self.x2+10, self.y2)
            
            
        def leftKey(event):
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)

            if self.x1 <= self.zone.x_min:
                self.zone.coords(self.robot, self.x1, self.y1, self.x2, self.y2)
            else:
                self.zone.coords(self.robot, self.x1-10, self.y1, self.x2-10, self.y2)
            
        def upKey(event):
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)

            if self.y1 <= self.zone.y_min:
                self.zone.coords(self.robot, self.x1, self.y1, self.x2, self.y2)
            else:
                self.zone.coords(self.robot, self.x1, self.y1-10, self.x2, self.y2-10)
            
        def downKey(event):
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)

            if self.y2 >= self.zone.y_max:
                self.zone.coords(self.robot, self.x1, self.y1, self.x2, self.y2)
            else:
                self.zone.coords(self.robot, self.x1, self.y1+10, self.x2, self.y2+10)


        self.zone.focus_set()
        self.zone.bind("<Right>", rightKey)
        self.zone.bind("<Left>", leftKey)
        self.zone.bind("<Up>", upKey)
        self.zone.bind("<Down>", downKey)
        

def main():
    window = Tk()
    window.geometry("400x200+450+300") # Window needs to be centered on each PC screen 
    game = userInterface(window)
    window.mainloop()

if __name__=='__main__':
    sys.exit(main())
