from inspect import FrameInfo
from tkinter import *
from tkinter import ttk
from tkinter import Label, PhotoImage, messagebox
import pymysql
import re

# Database Connectivity
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="student"
)

def register():
    if firstnameEntry.get() == '' or passwordentry.get() == '' or Cpasswordentry.get() == '' or emailEntry.get() == '' or phoneEntry.get() == ''or addEntry.get() == ''or aadharEntry.get() == '' or entrytpin.get() == '' or pinEntry.get() == '' or check.get() == 0:
        messagebox.showerror('Error', 'All Fields are Required')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Agree to Our Terms & Conditions')
    elif not re.match(r"[^@]+@[^@]+.[^@]+", emailEntry.get()):
        messagebox.showerror("Error", "Invalid email address.")

    elif not re.match(r"[0-9]{10}", phoneEntry.get()):
        messagebox.showerror("Error", "Invalid phone number.")

    elif not re.match(r"[0-9]{6}", pinEntry.get()):
        messagebox.showerror("Error", "Invalid Pin Code number.")

    elif not re.match(r"[0-9]{12}", aadharEntry.get()):
        messagebox.showerror("Error", "Invalid Aadhar number.")

    elif not check.get():
        messagebox.showerror("Error", "Please Agree to the Terms and Conditions.")
    else:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO shiven values('"+firstnameEntry.get()+"', '"+phoneEntry.get()+"','"+entrytpin.get()+"','"+pinEntry.get()+"', '"+emailEntry.get()+"','"+addEntry.get()+"','"+aadharEntry.get()+"','"+passwordentry.get()+"')" )
        mydb.commit()
        messagebox.showinfo('Success', 'Account Registered Successfully!')

root = Tk()
root.geometry('1350x710+10+10')
root.title('Banking app')

bgImage = PhotoImage(file='bg5.png')
bgLabel = Label(root, image=bgImage, bd=0)
bgLabel.place(x=0, y=0)

gImage = PhotoImage(file='bg1.png')
gLabel = Label(root, image=gImage, height=180, width=190)
gLabel.place(x=5, y=5)

titleLabel1 = Label(text='Mumbai Bank', font=('arial', 25, 'bold'), bd=0)
titleLabel1.place(x=120, y=280)
titleLabel2 = Label(text="- The most Secure and Trusted Bank", font=('arial', 14, 'bold'), bd=0)
titleLabel2.place(x=120, y=350)

registerFrame = Frame(root, width=700, height=750)
registerFrame.place(x=630, y=30)

titleLabel = Label(registerFrame, text='Savings Account Online-registration', font=('arial', 20, 'bold'))
titleLabel.place(x=18, y=20)

firstnameLabel = Label(registerFrame, text="Full Name", width=10, font=("arial", 15))
firstnameLabel.place(x=20, y=100)
firstnameEntry = Entry(registerFrame, font=('arial', 18), bg='lightgray', width=50, bd=5)
firstnameEntry.place(x=20, y=125)

phoneLabel = Label(registerFrame, text="Phone Number", width=12, font=("arial", 15))
phoneLabel.place(x=20, y=180)
phoneEntry = Entry(registerFrame, font=('arial', 18), bg='lightgray', width=16, bd=5)
phoneEntry.place(x=20, y=205)

tpinLabel = Label(registerFrame, text="Create Tpin", width=10, font=("arial", 15))
tpinLabel.place(x=250, y=180)
entrytpin = Entry(registerFrame, font=('arial', 18), bg='lightgray', width=15, bd=5)
entrytpin.place(x=250, y=205)

pinLabel = Label(registerFrame, text="Pincode", width=12, font=("arial", 15))
pinLabel.place(x=470, y=180)
pinEntry = Entry(registerFrame, font=('arial', 18), bg='lightgray', width=15, bd=5)
pinEntry.place(x=470, y=205)

emailLabel = Label(registerFrame, text="Email Address", width=12, font=("arial", 15))
emailLabel.place(x=20, y=260)
emailEntry = Entry(registerFrame, font=('arial', 18), bg='lightgray', width=50, bd=5)
emailEntry.place(x=20, y=285)

addLabel = Label(registerFrame, text="Residential Address", width=17, font=("arial", 15))
addLabel.place(x=20, y=340)
addEntry = Entry(registerFrame, font=('arial', 18), bg='lightgray', width=50, bd=5)
addEntry.place(x=20, y=365)

aadharLabel = Label(registerFrame, text="Adhaar Card", width=12, font=("arial", 15))
aadharLabel.place(x=20, y=420)
aadharEntry = Entry(registerFrame, font=('arial', 18), bg='lightgray', width=50, bd=5)
aadharEntry.place(x=20, y=445)

passwordlabel = Label(registerFrame, text="Set Password",width=12, font=("arial", 15))
passwordlabel.place(x=20, y=500)
passwordentry = Entry(registerFrame, show="*", font=('arial', 18), bg='lightgray', width=24, bd=5)
passwordentry.place(x=20, y=525)

Cpasswordlabel = Label(registerFrame, text="Confirm Password",width=18, font=("arial", 15))
Cpasswordlabel.place(x=350, y=500)
Cpasswordentry = Entry(registerFrame, show="*", font=('arial', 18), bg='lightgray', width=24, bd=5)
Cpasswordentry.place(x=350, y=525)

check = IntVar()
checkButton = Checkbutton(registerFrame, text="I Agree to the Terms & Conditions", variable=check, onvalue=1, offvalue=0, font=("arial", 10, 'bold'))
checkButton.place(x=20, y=570)

registerButton = Button(registerFrame, text='Register', font=('arial', 15, 'bold'), bg='steelblue', fg='white', bd=5, relief=RIDGE, command=register)
registerButton.place(x=300, y=620)

root.mainloop()
