import tkinter
from tkinter import *
import MyDataBase
root=Tk()

root.geometry('600x400')
root.title('Login')

user=StringVar()
password=IntVar()

def Login():
    username=user.get()
    code=password.get()

    if MyDataBase.Login(username,code):
        print('login successful')
    else:
        print('Wrong Details')

lblHeading=Label(root,text='FaceBook Login')
lblHeading.place(x=250,y=20)

val1=Label(root,text='User Name')
val1.place(x=200,y=50)

txtval1=Entry(root,textvariable=user)
txtval1.place(x=275,y=50)

val2=Label(root,text='Password')
val2.place(x=200,y=80)

txtval2=Entry(root,textvariable=password,show='*')
txtval2.place(x=275,y=80)

login=Button(root,text='Login',command=Login)
login.place(x=275,y=120)

root.mainloop()


