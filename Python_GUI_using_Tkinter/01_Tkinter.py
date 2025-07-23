from tkinter import * #Import tkinter

root = Tk() # Create main window


# Creating a label widget (w=Label(master, option=value))
mylabel = Label(root, text="Hello World!")
# Shoving it onto the screen
mylabel.pack()


root.mainloop() 
# The mainloop() method is used to run application once it is ready. It is an infinite loop that keeps the application running, waits for events to occur (such as button clicks) and processes these events as long as the window is not closed.