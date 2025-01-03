from tkinter import*
import  string
import random

from tkinter import messagebox

def password_generator():
    try:
        plen = int(entry.get())
        if plen < 1:
            raise ValueError("Password length must be greater than 0.")
        
    except ValueError:
        messagebox.showerror("Invalid Input ","Please enter a valid number for password length.")
        return
    
    str1 = string.ascii_lowercase
    str2 = string.ascii_uppercase
    str3 = string.digits
    str4 = string.punctuation
    
    s = []
    
    s.extend(list(str1))
    s.extend(list(str2))
    s.extend(list(str3))
    s.extend(list(str4))
    
    if plen >len(s):
        messagebox.showerror("Invalid Input","Password length exceeds aailable character pool.")
        return
    ranndom_password ="".join(random.sample (s, plen))
    
    password_textbox.delete(1.0,END)
    password_textbox.insert(END,ranndom_password)
    
    root.Tk()
    root.title("PASSWORD GENERATOR")
    root.geometry("450x350")
    root.config(bg="F5F5DC")
    
    
    font_stile = ("Arial 14 bold")
    button_font= ("Arial 12 bold")
    headline_font=("Arial 16 bold")
    
    #Headline for password length 
    headline = Label(root,text="ENTER PASSWORD LENGTH ",font=headline_font,bg="#F5F5DC",fg="black")
    headline.pack(pady=12)
    
    #Entry for password length
    entry=Entry(root,font=font_stile,bg="white",fg="bleck",borderwidth=3,relief="sunken")
    entry.pack(pady=10)
    
    password_frame= Frame(root,bg="#E8E8E8")
    password_frame.pack(pady=10)
    
    password_lable=Label(password_frame,text="YOUR PASSWORD:",font=("Arial 15 bold"),bg="E8E8E8",fg="black")
    password_lable.pack(anchor=CENTER,pady=10)
    
    password_textbox=Text(password_frame,height=1,width=25,font=("Arial 15 bold"),borderwidth=1,relief="sunken",wrap=N)
    password_textbox.pack(anchor=CENTER,pady=10)
    
    root.mainloop()
    