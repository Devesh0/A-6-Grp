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
        # Might need to edit this a little. 
        self.SettingsWindow = Tk()
        self.label = Label(self.SettingsWindow, text="There should be settings here. ")
        self.label.pack()
        self.SettingsWindow.mainloop()

    def loadGameArena(self):
        # Eventually this will have a new game/load game option prior to loading the actual game
        self.menuCanvas.pack_forget()
        theGame = theRobotGame(self.window)

class theRobotGame():

    
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x600+200+60")
        self.robotLocation = 1
        self.robotCoords = (0, 0, 20, 20)
        self.createMap(self.robotCoords)
        
        self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
        
        
    def createMap(self, crds):

        self.coords = crds
        # split each if into it's own seperate function: zone1(), zone2() etc...
        if self.robotLocation == 1:
            self.zone = Canvas(self.window, width=1000, height=600, bg='white')
            self.window.title("Zone 1")
            self.zone.pack(fill=BOTH, expand=1)
##            self.wall = self.zone.create_rectangle(25,25,950,50, fill="black")
##            self.wall2 = self.zone.create_rectangle(25,25,50,550, fill="black")
##            self.wall3 = self.zone.create_rectangle(50,550,950,525, fill="black")
##            self.wall4 = self.zone.create_rectangle(950,525,925,325, fill="black")
##            self.wall5 = self.zone.create_rectangle(950,50,925,250, fill="black")
            self.teleport1 = self.zone.create_line(500, 597, 450, 597, fill="green", width=2)
            self.teleport2 = self.zone.create_line(996, 270, 996, 310, fill ="green", width=2)
            self.zone.x_min = 0
            self.zone.y_min = 0
            self.zone.x_max = 991
            self.zone.y_max = 600
            self.robot = self.zone.create_rectangle(self.coords)
            self.initiateGameplay()

        if self.robotLocation == 2:
            self.zone.pack_forget()
            self.zone = Canvas(self.window, width=1000, height=600, bg='white')
            self.window.title("Zone 2")
            self.zone.pack(fill=BOTH, expand=1)
            self.teleport1 = self.zone.create_line(3, 270, 3, 310, fill ="green", width=2)
            self.zone.x_min = 0
            self.zone.y_min = 0
            self.zone.x_max = 991
            self.zone.y_max = 600
            self.robot = self.zone.create_rectangle(self.coords)
            self.initiateGameplay()

        if self.robotLocation == 3:
            self.zone.pack_forget()
            self.zone = Canvas(self.window, width=1000, height=600, bg='white')
            self.window.title("Zone 3")
            self.zone.pack(fill=BOTH, expand=1)
            self.teleport1 = self.zone.create_line(500, 3, 450, 3, fill="green", width=2)
            self.zone.x_min = 0
            self.zone.y_min = 0
            self.zone.x_max = 991
            self.zone.y_max = 600
            self.robot = self.zone.create_rectangle(self.coords)
            self.initiateGameplay()
        
    def initiateGameplay(self):
        # Temporary movement for testing purposes
        # Refactor this code when the time comes
        
        def rightKey(event):
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
            
            
            if self.x2 >= self.zone.x_max or self.battery == 0:
                self.zone.coords(self.robot, self.x1, self.y1, self.x2, self.y2)
            else:
                self.zone.coords(self.robot, self.x1+10, self.y1, self.x2+10, self.y2)
##                self.battery -= 0.5

            if self.robotLocation == 1:

                self.teleportTuple1 = self.zone.find_overlapping(500, 597, 450, 597)
                self.teleportTuple2 = self.zone.find_overlapping(996, 270, 996, 310)
                
                if self.robot in self.teleportTuple1:
                    self.robotLocation = 3
                    self.robotCoords = (460, 3, 480, 23)
                    self.createMap(self.robotCoords)
                elif self.robot in self.teleportTuple2:
                    self.robotLocation = 2
                    self.robotCoords = (4, 280, 24, 300)
                    self.createMap(self.robotCoords)
                else:
                    pass

            if self.robotLocation == 2:

                self.teleportTuple1 = self.zone.find_overlapping(3, 270, 3, 310)

                if self.robot in self.teleportTuple1:
                    self.robotLocation = 1
                    self.zone.pack_forget()
                    self.robotCoords = (976, 270, 996, 310)
                    self.createMap(self.robotCoords)
              
        def leftKey(event):
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
            
            
            if self.x1 <= self.zone.x_min or self.battery == 0:
                self.zone.coords(self.robot, self.x1, self.y1, self.x2, self.y2)
            else:
                self.zone.coords(self.robot, self.x1-10, self.y1, self.x2-10, self.y2)
##                self.battery -= 0.5

            if self.robotLocation == 1:

                self.teleportTuple1 = self.zone.find_overlapping(500, 597, 450, 597)
                self.teleportTuple2 = self.zone.find_overlapping(996, 270, 996, 310)
                
                if self.robot in self.teleportTuple1:
                    self.robotLocation = 3
                    self.robotCoords = (460, 3, 480, 23)
                    self.createMap(self.robotCoords)
                elif self.robot in self.teleportTuple2:
                    self.robotLocation = 2
                    self.robotCoords = (4, 280, 24, 300)
                    self.createMap(self.robotCoords)
                else:
                    pass

            if self.robotLocation == 2:

                self.teleportTuple1 = self.zone.find_overlapping(3, 270, 3, 310)

                if self.robot in self.teleportTuple1:
                    self.robotLocation = 1
                    self.zone.pack_forget()
                    self.robotCoords = (976, 270, 996, 290)
                    self.createMap(self.robotCoords)
                    
        def upKey(event):
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
            

            if self.y1 <= self.zone.y_min or self.battery == 0:
                self.zone.coords(self.robot, self.x1, self.y1, self.x2, self.y2)
            else:
                self.zone.coords(self.robot, self.x1, self.y1-10, self.x2, self.y2-10)
##                self.battery -= 0.5

            if self.robotLocation == 1:

                self.teleportTuple1 = self.zone.find_overlapping(500, 597, 450, 597)
                self.teleportTuple2 = self.zone.find_overlapping(996, 270, 996, 310)
                
                if self.robot in self.teleportTuple1:
                    self.robotLocation = 3
                    self.robotCoords = (460, 3, 480, 23)
                    self.createMap(self.robotCoords)
                elif self.robot in self.teleportTuple2:
                    self.robotLocation = 2
                    self.robotCoords = (4, 280, 24, 300)
                    self.createMap(self.robotCoords)
                else:
                    pass

            if self.robotLocation == 2:

                self.teleportTuple1 = self.zone.find_overlapping(3, 270, 3, 310)

                if self.robot in self.teleportTuple1:
                    self.robotLocation = 1
                    self.zone.pack_forget()
                    self.robotCoords = (976, 270, 996, 310)
                    self.createMap(self.robotCoords)
            
        def downKey(event):
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
            
            
            if self.y2 >= self.zone.y_max or self.battery == 0:
                self.zone.coords(self.robot, self.x1, self.y1, self.x2, self.y2)

            else:
                self.zone.coords(self.robot, self.x1, self.y1+10, self.x2, self.y2+10)
##                self.battery -= 0.5

            if self.robotLocation == 1:

                self.teleportTuple1 = self.zone.find_overlapping(500, 597, 450, 597)
                self.teleportTuple2 = self.zone.find_overlapping(996, 270, 996, 310)
                
                if self.robot in self.teleportTuple1:
                    self.robotLocation = 3
                    self.robotCoords = (460, 3, 480, 23)
                    self.createMap(self.robotCoords)
                elif self.robot in self.teleportTuple2:
                    self.robotLocation = 2
                    self.robotCoords = (4, 280, 24, 300)
                    self.createMap(self.robotCoords)
                else:
                    pass

            if self.robotLocation == 2:

                self.teleportTuple1 = self.zone.find_overlapping(3, 270, 3, 310)

                if self.robot in self.teleportTuple1:
                    self.robotLocation = 1
                    self.zone.pack_forget()
                    self.robotCoords = (976, 270, 996, 310)
                    self.createMap(self.robotCoords)

        self.battery = 100.0
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
