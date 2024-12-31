from tkinter  import  *
myroot=Tk()

def click(event):
    global scvalue
    text = event.widget.cget("text")
    # print(text)

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
        
                value = eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    

myroot.geometry("400x700")
myroot.title("Calcy By Amar")
scvalue=StringVar()
scvalue.set("")

screen=Entry(myroot,textvar=scvalue,font="lucida 30 bold ")
screen.pack(fill=X,padx=10,pady=10)

f=Frame(myroot,bg="grey")

#buttons 1,2,3

b=Button(f,text="1",padx=15,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=10,row=1,column=0)
b.bind("<Button-1>",click)


b=Button(f,text="2",padx=15,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=10,row=1,column=1)
b.bind("<Button-1>",click)


b=Button(f,text="3",padx=15,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=10,row=1,column=2)
b.bind("<Button-1>",click)
f.pack()
#buttons 4,5,6
b=Button(f,text="4",padx=15,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=10,row=2,column=0)
b.bind("<Button-1>",click)


b=Button(f,text="5",padx=15,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=15,row=2,column=1)
b.bind("<Button-1>",click)


b=Button(f,text="6",padx=15,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=15,row=2,column=2)
b.bind("<Button-1>",click)
f.pack()
#buttons 7,8,9
b=Button(f,text="7",padx=15,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=15,row=3,column=0)
b.bind("<Button-1>",click)
b.grid(row=3,column=0)

b=Button(f,text="8",padx=15,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=15,row=3,column=1)
b.bind("<Button-1>",click)

b=Button(f,text="9",padx=15,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=15,row=3,column=2)
b.bind("<Button-1>",click)
f.pack()
#button 0 , +,-
b=Button(f,text="0",padx=25,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=15,row=4,column=0)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=25,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=15,row=4,column=1)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=25,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=15,row=4,column=2)
b.bind("<Button-1>",click) 

f.pack()
 #buttons =,C,*
b=Button(f,text="=",padx=25,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=15,row=5,column=0)
b.bind("<Button-1>",click)

b=Button(f,text="C",padx=25,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=15,row=5,column=1)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=25,pady=15,font="lucida 25 bold ")
b.grid(padx=12,pady=15,row=5,column=2)
b.bind("<Button-1>",click) 

f.pack()














myroot.mainloop()
