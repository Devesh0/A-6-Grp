import sys
from tkinter import *

class robotGameBaseClass():

    def __init__ (self, window):
        # Initializes the first window
        # Might need to refactor. There's a lot of code here.
        self.window = window
        self.menuCanvas = Canvas(self.window, width=300, height=300, bg='white')
        self.menuCanvas.pack(fill=BOTH, expand=1)

        self.buttonFrame = Frame(self.menuCanvas)
        self.buttonFrame.pack(side="top", pady=25)

        self.startButton = Button(self.menuCanvas, text="Play game", command = lambda: self.loadGameArena())
        self.startButton.pack()

        self.settingsButton = Button(self.menuCanvas, text="Settings", command = lambda: self.settings())
        self.settingsButton.pack()

        self.exitButton = Button(self.menuCanvas, text="Exit", command = lambda: self.window.destroy())
        self.exitButton.pack()
        

    def loadGameArena(self):
        # Eventually this will have a new game/load game option prior to loading the actual game
        self.menuCanvas.pack_forget()
        self.window.attributes("-fullscreen", True) # Automatically goes full-screen. 
        self.menuCanvas = Canvas(self.window, width=10000, height=10000, bg='white')
        self.menuCanvas.pack()
        self.window.bind("<Escape>", self.minimizeScreen)
        self.wall = self.menuCanvas.create_rectangle(25,25,950,50, fill="black")
        self.wall2 = self.menuCanvas.create_rectangle(25,25,50,550, fill="black")
        self.wall3 = self.menuCanvas.create_rectangle(50,550,950,525, fill="black")
        self.wall4 = self.menuCanvas.create_rectangle(950,525,925,325, fill="black")
        self.wall5 = self.menuCanvas.create_rectangle(950,50,925,250, fill="black")
        

##        self.robot = self.menuCanvas.create_rectangle(25, 25, 25+25, 25+25) # Placeholder rectangle
##
##        self.x1,y1,x2,y2 = canvas.coords(self.robot)
##
##        xspeed = 10.0
##        yspeed = 5.0
##
##        self.menuCanvas.bind("<Right>", rightKey)
##
##        def rightKey(event, self.robot, ):
##            canvas.coords(self.robot

        # Focus on getting a moving robot
        

    
        
        
    def minimizeScreen(self, event):
        self.window.attributes("-fullscreen", False) #Need to program this so it goes back to a decent resolution
        self.window.geometry("1000x600+200+60")
    def settings(self):
        self.SettingsWindow = Tk()
        self.label = Label(self.SettingsWindow, text="There should be settings here. ")
        self.label.pack()
        self.SettingsWindow.mainloop()
    
def main():
    window = Tk()
    window.geometry("400x200+450+300") # Window needs to be centered on each PC screen
    game = robotGameBaseClass(window)
    window.mainloop()

if __name__=='__main__':
    sys.exit(main())
