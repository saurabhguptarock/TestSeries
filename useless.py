# from question import question

# print(question())
from tkinter import *

root2 = Tk()
root2.geometry('1920x1080')
root2.title('Question')

top = Frame(root2, width=1920, height=1080, bg='powder blue', relief=SUNKEN)
top.pack(side=TOP)

lblinfo = Label(top, font=('arial', 15, 'bold'),
                text="QUESTIONS ARE BELOW", fg='Steel Blue', bd=10, anchor='w')
lblinfo.grid(row=0, column=0)

text = Text(top, 'as')


root2.mainloop()
