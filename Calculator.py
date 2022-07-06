from tkinter import *

root = Tk()
root.geometry("312x324")
root.resizable(False, False)
root.title("My_Calculator")

expression = ""


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def btn_clear():
    global expression
    expression = ""
    input_text.set("")


def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)


input_text = StringVar()
input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="#540D02",
                    highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font="arial,18,bold",textvariable=input_text, width=50, bg="#99E4F9", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btn_frame = Frame(root, width=312, height=272.5, bg="grey")
btn_frame.pack()

clear = Button(btn_frame, text='C', fg='black', width=32, height=3, bd=0, bg='#eee', cursor="hand2",
               command=lambda: btn_clear())
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btn_frame, text='/', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                command=lambda: btn_click("/"))
divide.grid(row=0, column=3, padx=1, pady=1)

seven = Button(btn_frame, text=7, fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
               command=lambda: btn_click(7))
eight = Button(btn_frame, text=8, fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
               command=lambda: btn_click(8))
nine = Button(btn_frame, text=9, fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
              command=lambda: btn_click(9))
multiply = Button(btn_frame, text='x', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                  command=lambda: btn_click('*'))

four = Button(btn_frame, text=4, fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
              command=lambda: btn_click(4))
five = Button(btn_frame, text=5, fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
              command=lambda: btn_click(5))
six = Button(btn_frame, text=6, fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
             command=lambda: btn_click(6))
minus = Button(btn_frame, text='-', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
               command=lambda: btn_click('-'))

one = Button(btn_frame, text=1, fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
             command=lambda: btn_click(1))
two = Button(btn_frame, text=2, fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
             command=lambda: btn_click(2))
three = Button(btn_frame, text=3, fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
               command=lambda: btn_click(3))
plus = Button(btn_frame, text='+', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
              command=lambda: btn_click('+'))

zero = Button(btn_frame, text=0, fg='black', width=20, height=3, bd=0, bg='#eee', cursor='hand2',
              command=lambda: btn_click(0))
pont = Button(btn_frame, text=".", fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
              command=lambda: btn_click('.'))
equals = Button(btn_frame, text='=', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                command=lambda: btn_equal())
seven.grid(row=1, column=0, padx=1, pady=1)
eight.grid(row=1, column=1, padx=1, pady=1)
nine.grid(row=1, column=2, padx=1, pady=1)
multiply.grid(row=1, column=3, padx=1, pady=1)
four.grid(row=2, column=0, padx=1, pady=1)
five.grid(row=2, column=1, padx=1, pady=1)
six.grid(row=2, column=2, padx=1, pady=1)
minus.grid(row=2, column=3, padx=1, pady=1)
one.grid(row=3, column=0, padx=1, pady=1)
two.grid(row=3, column=1, padx=1, pady=1)
three.grid(row=3, column=2, padx=1, pady=1)
plus.grid(row=3, column=3, padx=1, pady=1)
zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
pont.grid(row=4, column=2, padx=1, pady=1)
equals.grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
