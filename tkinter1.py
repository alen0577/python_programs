from tkinter import *
root = Tk()
Label(root, text="username").grid(row=0, column=0)
Label(root, text="password").grid(row=1, column=0)
Entry(root).grid(row=0,column=1)
Entry(root).grid(row=1, column=1)
Button(root, text="Login").grid(row=2,column=0)



root.mainloop()
