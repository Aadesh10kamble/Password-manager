from password_generator import passwordgenerator
from tkinter import messagebox
from tkinter import *
import json

def saver () :

    passw_ = password_entry.get ()
    email_ = email_entry.get ()
    web_ = website_entry.get ()

    try :
        with open ("password_manager.json","r") as File : 
            new_entry = json.load (File)
    except FileNotFoundError :
        with open ("password_manager.json","w") as File :
            new_entry = {}
    except json.decoder.JSONDecodeError :
        new_entry = {}
        
    new_entry[web_] = {
            "email" : email_,
            "password" : passw_
            }
    
    if (len (passw_) == 0) or (len (email_) == 0) or (len (web_) == 0) :
        messagebox.askretrycancel (title = "Empty Password") 
    else :
        is_ok = messagebox.askokcancel (title = web_,message = f"Email :{email_}\n" 
                                                    f"Password{passw_}" "\nWant to save this data?")
        if is_ok == True :
            with open ("password_manager.json","w") as File :
                json.dump (new_entry,File,indent = 4)
                website_entry.delete (0,END)
                password_entry.delete (0,END)

def password_gen () :
    password_entry.insert (0 , passwordgenerator ())

def searcher () :
    
    web_ = website_entry.get ()
    try :
        with open ("password_manager.json","r") as File : 
                data = json.load (File)
    except :
        messagebox.askokcancel (title = "Error",message = "Data not found .")
    else :
        if web_ in data.keys () :
            messagebox.askokcancel (title = "Login Credentials",message = f'Email   :   {data[web_]["email"]}'
                                                                        f'\nPassword   :   {data[web_]["password"]}')
        else :
            messagebox.askokcancel (title = "Search",message = f"No credentials for :  {web_}")    


screen = Tk ()
screen.minsize (430 , 350)
screen.title ("Password Manager")

blank = Label (text = "" )
blank.grid (row = 0 , column = 0)

canvas = Canvas ( width = 200 ,  height = 190)
img = PhotoImage (file = "logo.png")
canvas.create_image (90,95,image = img) 
canvas.grid (row = 0 , column = 1,columnspan = 2)

website = Label (text = "Website : ")
website.config (padx = 10,pady = 10)
website.grid (row = 1 , column = 0)

website_entry = Entry (width = 30)
website_entry.grid (row = 1,column = 1)

email = Label (text = "Email : ")
email.config (padx = 10)
email.grid (row = 2,column = 0)

email_entry = Entry (width = 50)
email_entry.insert (0,"aadesh10kamble@gmail.com")
email_entry.grid (row = 2 ,column = 1,columnspan = 6)

password = Label (text = 'Password : ')
password.config (padx = 10)
password.grid (row = 3 ,column = 0)

password_entry = Entry (width = 30)
password_entry.grid (row = 3 ,column = 1)

generate_button = Button (text = "Generate Password",width = 14,command = password_gen)
generate_button.grid (row = 3 ,column = 2,pady = 10)

add_button = Button (text = 'Add',width = 43,command = saver)
add_button.grid (row = 5 ,column = 1,columnspan = 2)

search_button = Button (text = "Search",width = 14,command = searcher)
search_button.grid (row = 1 , column = 2)

screen.mainloop ()
