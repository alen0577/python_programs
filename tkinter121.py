from tkinter import *
root = Tk()
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg='#D8CBC9')
root.title("Find Sum")


def find_sum():
    sum1 = int(e1.get()) + int(e2.get())
    result.set(str(sum1))


result = StringVar()

label1 = Label(root, text="Number 1", width=10, fg='#0507B1', font=15)
label2 = Label(root, text="Number 2", width=10, fg='#0507B1', font=15)
label3 = Label(root, text="Result", width=10, fg='#0507B1', font=15, justify=LEFT)

e1 = Entry(root, justify=RIGHT, bg='#9ADE6A', font=20)
e2 = Entry(root, justify=RIGHT, bg='#9ADE6A', font=20)
e3 = Entry(root, justify=RIGHT, textvariable=result, bg='#9ADE6A', font=20)

b1 = Button(root, text="Find Sum", command=find_sum, bg='orange', font=15)

label1.grid(row=0, column=0)
e1.grid(row=0, column=1)
label2.grid(row=1, column=0)
e2.grid(row=1, column=1)
label3.grid(row=2, column=0)

e3.grid(row=2, column=1)
b1.grid(row=3, column=1)

root.mainloop()
