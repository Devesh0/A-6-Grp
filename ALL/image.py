import sys
from tkinter import *

def main():
    
    canvas = Canvas(width=1250,height=700,bg='black')
    canvas.pack(expand = YES,fill = BOTH)
    gif1=PhotoImage(file='images.gif')
    canvas.create_image(50,10,image=gif1,anchor = NW)
    canvas.create_text(400,10,text='VIRTUAL ROBOT BARGAIN HUNT',font='Helvetica 32 bold italic underline',fill='red',anchor=NW)
    start=canvas.create_text(1000,200,text='START',font='Times 26 bold underline',fill='blue',anchor=W)
    options=canvas.create_text(1000,250,text='OPTIONS',font='Times 26 bold underline',fill='blue',anchor=W)
    ext=canvas.create_text(1000,300,text='EXIT',font='Times 26 bold underline',fill='blue',anchor=W)
    
    mainloop()

if __name__=='__main__':
    sys.exit(main())
