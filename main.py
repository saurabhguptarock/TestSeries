from tkinter import *
from nltk.tokenize import word_tokenize

root = Tk()
root.geometry('400x200')
root.title('Test Series')

login_text = StringVar()
password_text = StringVar()
answer = StringVar()


top = Frame(root, width=400, height=200, bg='powder blue', relief=SUNKEN)
top.pack(side=TOP)

lblinfo = Label(top, font=('arial', 15, 'bold'),
                text="ENTER LOGIN DETAILS", fg='Steel Blue', bd=10, anchor='w')
lblinfo.grid(row=0, column=0)


def message():
    global root1
    root1 = Tk()
    root1.geometry('200x120')
    root1.title('Error')
    frame = Frame(root1, width=200, height=120, bg='powder blue', relief=SUNKEN)
    frame.pack(side=TOP)
    login_id = Label(frame, font=('arial', 15, 'bold'),
                     text="Wrong login ID", fg='Steel Blue',
                     bd=10, anchor='w')
    login_id.grid(row=0, column=0)
    Signup = Button(frame, padx=30, pady=8, bd=2, fg='black',
                    font=('arial', 20, 'bold'),
                    text='Signup', bg='powder blue', command=lambda: sign_up())
    Signup.grid(row=1, column=0)


def question():
    root2 = Tk()
    root2.geometry('1920x1080')
    root2.title('Question')

    top = Frame(root2, width=1920, height=1080, bg='powder blue', relief=SUNKEN)
    top.pack(side=TOP)

    lblinfo = Label(top, font=('arial', 15, 'bold'),
                    text="QUESTIONS ARE BELOW", fg='Steel Blue', bd=10, anchor='w')
    lblinfo.grid(row=0, column=0)

    # for question in question_asked():
    #     print(question)

    login = Entry(top, font=('arial', 50, 'bold'), textvariable=answer,
                  bd=10, insertwidth=4, bg='powder blue', justify='left')
    login.grid(row=1, column=0)


def exit():
    try:
        root.destroy()
        root1.destroy()
    except NameError:
        pass


def login_details():
    with open('Users.txt', 'a') as all_users:
        print(login_text.get(), end=' ', file=all_users)
    with open('Passwords.txt', 'a') as all_passwords:
        print(password_text.get(), end=' ', file=all_passwords)


def sign_up():
    root1.destroy()
    login_details()


def login_check():
    try:
        done = False
        with open('Users.txt') as u:
            users = u.read()
        for users in word_tokenize(users):
            if login_text.get() == users:
                with open('Passwords.txt') as p:
                    passwords = p.read()
                for passwords in word_tokenize(passwords):
                    if password_text.get() == passwords:
                        print('you are now loged in')
                        root.destroy()
                        question()
                        done = True
                    else:
                        print('wrong password')
                        done = True
            else:
                print('wrong login id')
        if done is not True:
            message()
    except FileNotFoundError:
        pass


login = Entry(top, font=('arial', 10, 'bold'), textvariable=login_text,
              bd=10, insertwidth=4, bg='powder blue', justify='left')
login.grid(row=1, column=0)

password = Entry(top, font=('arial', 10, 'bold'), textvariable=password_text,
                 bd=10, insertwidth=4, bg='powder blue', justify='left')
password.grid(row=2, column=0)


login = Button(top, padx=30, pady=8, bd=2, fg='black', font=('arial', 20, 'bold'),
               text='Login', bg='powder blue', command=lambda: login_check()).grid(row=1, column=1)
Exit = Button(top, padx=43, pady=8, bd=2, fg='black', font=('arial', 20, 'bold'),
              text='Exit', bg='powder blue', command=lambda: exit()).grid(row=2, column=1)

root.mainloop()
