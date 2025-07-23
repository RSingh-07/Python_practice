from tkinter import *

clicked_once = False

def on_click():
    global clicked_once
    if not clicked_once:
        label.config(text="You clicked the button!")
        clicked_once = True
    else:
        label.config(text="You already clicked!")

root = Tk()
root.title("My First App")
root.geometry("300x200")
root.config(bg="green")


label = Label(root, text="Hello, Tkinter!", bg="pink")
label.pack(pady=10)

button = Button(root, text="Click Me", command = on_click, relief=GROOVE, bd=4, cursor="heart")
button.pack(pady = 10)


root.mainloop()