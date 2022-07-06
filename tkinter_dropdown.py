from tkinter import *

root = Tk()
root.geometry('600x600')
root.configure(bg='pink')
root.title('World of Stories...!')

my_menu = Menu(root)
root.config(menu=my_menu)

menu0 = Menu(my_menu)

my_menu.add_cascade(label='File', menu=menu0)
menu0.add_command(label='New')
menu0.add_command(label='Open')
menu0.add_command(label='Save')
menu0.add_command(label='Save as')
menu0.add_separator()
menu0.add_command(label='Print')
menu0.add_separator()
menu0.add_command(label='Exit')

menu1 = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=menu1)
menu1.add_command(label='Undo')
menu1.add_command(label='Cut')
menu1.add_command(label='Copy')
menu1.add_command(label='Paste')
menu1.add_command(label='Delete')

menu2 = Menu(my_menu)
my_menu.add_cascade(label='Format', menu=menu2)
menu2.add_command(label='Center')
menu2.add_command(label='Left')
menu2.add_command(label='Right')
menu2.add_command(label='Justify')


menu3 = Menu(my_menu)
my_menu.add_cascade(label='View', menu=menu3)
menu3.add_command(label='Zoom In')
menu3.add_command(label='Zoom Out')

menu4 = Menu(my_menu)
my_menu.add_cascade(label='Help', menu=menu4)
menu4.add_command(label='View Help')
menu4.add_command(label='Send Feedback')

root.mainloop()
