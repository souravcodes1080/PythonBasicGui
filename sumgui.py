from calendar import c
from tkinter import*
from tkinter import font
from tkinter.font import BOLD
from turtle import color
root= Tk()

def add():
    num1=(int)(num1Entry.get())
    num2=(int)(num2Entry.get())
    sum=num1+num2
    print(sum)
    Label(root, text="Result:",font="arial",foreground="red").grid(row=6,column=1)
    result=Label(root,text=sum,font="arial",foreground="red")
    result.grid(row=6,column=2)



blankSpace=Label(root,text="        ")
blankSpace.grid(row=6,column=3)
# blankSpace=Label(root,text="                ")
# blankSpace.grid(row=1,column=0)

num1Label=Label(root, text="Num1: ",font="arial",foreground="red")
num1Label.grid(row=2, column=1)
num2Label=Label(root, text="Num2: ",font="arial",foreground="red")
num2Label.grid(row=3, column=1)


num1Entry=Entry(root,width=5,background="yellow",font="arial",foreground="blue")
num1Entry.grid(row=2,column=2)
num2Entry=Entry(root,width=5,background="yellow",font="arial",foreground="blue")
num2Entry.grid(row=3,column=2)



button=Button(root,text="Add",font="arial",background="red",foreground="white",command=add)
button.grid(row=5,column=2)



root.mainloop()
