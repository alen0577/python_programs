from tkinter import *
root = Tk()
root.geometry("600x600")
root.resizable(0, 0)
root.title('Calculator')

result = StringVar()

def Sum():
    sum = int(e1.get())+int(e2.get())
    result.set(sum)


l1 = Label(root, text='number1')
l2 = Label(root, text='number2')
l3 = Label(root, text='result')

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root, textvariable=result)

l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()

btn = Button(root, text='Find Sum', command=Sum)
btn.pack()
c = Canvas(root, width=100, height=150)
c.pack()

root.mainloop()
