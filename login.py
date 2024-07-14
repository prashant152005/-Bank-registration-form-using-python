from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import re

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="student"
)
def open_register():
    t.destroy()
    import register
def validate_login():
    username = userentry.get()
    password = passentry.get()
    if not username or not password:
        messagebox.showerror('Error', 'Both fields are required!')
        return
    try:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM shiven WHERE `Phone No.`=%s or Email=%s AND Password=%s", (username, username, password))
        user = cursor.fetchone()
        if user:
            messagebox.showinfo('Success', 'Login successful!')
        else:
            messagebox.showerror('Error', 'Invalid credentials!')
    except Exception as e:
        messagebox.showerror('Error', f'Error: {e}')


t = Tk()
t.geometry('900x600+50+50')
t.title('Login page')
bgLImage=PhotoImage(file='loginbg.png')
bgLLabel=Label(t,image=bgLImage,bd=5)
bgLLabel.place(x=0,y=0)

frame1=Frame(t,width=568,height=320, bg='white')
frame1.place(x=160,y=140)

userimage=PhotoImage(file='user.png')
userimageLabel=Label(frame1, image=userimage, bg='white')
userimageLabel.place(x=10, y=50)


userlabel=Label(frame1, text='Email Or Phone No', bg='white', font=("arial", 15,'bold'))
userlabel.place(x=220, y=32)
userentry=Entry(frame1, font=('arial',15), bg='lightgray')
userentry.place(x=220,y=70)

passwordlabel=Label(frame1,text='Password', font=('arial',15,'bold'),bg='white')
passwordlabel.place(x=220,y=120)
passentry=Entry(frame1,font=('arial',15,),bg='lightgray')
passentry.place(x=220,y=160)


regButton=Button(frame1, text='Register New Account?',font=('arial',10),bd=0, bg='white', cursor='hand2',command=open_register )
regButton.place(x=220,y=200)

forgetButton=Button(frame1, text='Forget Password?',font=('arial',10),bd=0, bg='white', cursor='hand2',activebackground='white',fg='red')
forgetButton.place(x=410, y=200)

loginButton = Button(frame1, text="login", bd=5, bg='lightblue', cursor='hand2', command=validate_login)
loginButton.place(x=350,y=250)

t.mainloop()