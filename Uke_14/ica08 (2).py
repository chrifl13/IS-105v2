from turtle import *
from Tkinter import *
color('red')

class PressingButtons:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.quitButton = Button(frame, text="Start", bg="red", command=frame.quit)
        self.quitButton.pack(side=LEFT)
        
root = Tk()
b = PressingButtons(root)
root.mainloop()


#photo = PhotoImage(file="man.jpg")
#label = Label(root, image=photo)
#label.pack()
#root.mainloop()

while True:  
    speed(1)
    shape("turtle")
    write("Chicken, Fox, Grain")
    forward(150)
    write("chicken")
    forward(150)
    write("Chicken")
    right(10)
    backward(150)
    write("Alone")
    backward(150)
    write("Fox, Grain")
    left(10)
    forward(150)
    write("Grain")
    forward(150)
    write("Grain, Chicken")
    right(10)
    backward(150)
    write("Chicken")    
    backward(150)
    write("Chicken, Fox")
    left(10)
    forward(150)
    write("Fox")
    forward(150)
    write("Fox, Grain")  
    right(10)
    backward(150)
    write("Alone")
    backward(150)
    write("Chicken")
    left(10)
    forward(150)
    write("Chicken")
    forward(150)
    write("Chicken, Fox, Grain")
    break
while False:
    break
done()


