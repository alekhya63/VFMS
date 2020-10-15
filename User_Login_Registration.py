#!/usr/bin/python3
import subprocess
from tkinter import messagebox
from tkinter import *
import os
import re
import ctypes
#import Browser


def delete2():
    successscreen.destroy()

def error():
    messagebox.showinfo("Error","All Fields Required")

def delete3():
    sucessscreen2.destroy()
    
def sucess_login():
    messagebox.showinfo("Success","Login Successful")
    
def password_not_recognised():
    messagebox.showerror("Error","Incorrect Password")

def password_check():
    messagebox.showinfo("Error","Password can't be less than 8 characters")
    
def user_not_found():
    messagebox.showerror("Error","Access Denied")

def success_register():
    messagebox.showinfo("Success","Registration Successful")

def name_check():
    messagebox.showinfo("Error","Invalid Name")
    
##def signup_user():  
##    username_info = Username.get()
##    password_info = Password.get()
##    signupfile=open(username_info+".txt","w")
##    signupfile.write(username_info+'\n')
##    signupfile.write(password_info)
##    signupfile.close()
##    signupscreen.destroy()
##    #UserName_Entry.delete(0,END)
##    #Password_Entry.delete(0,END)

    
### Signup Page
def signup():
    global University_ID
    global FirstName
    global Email_ID
    global LastName
    global Password    
    global Username
    #global Password_Entry
    global signupscreen
    global Role
    signupscreen = Toplevel(screen)
    signupscreen.title ("Signup")
    signupscreen.geometry("300x700+350+150")

    University_ID = StringVar()
    Email_ID =StringVar()
    FirstName =StringVar()
    LastName =StringVar()
    Username =StringVar()
    Password =StringVar()
    Role = StringVar()
    #PasswordRe =StringVar()

    file = open ("test.txt","w+")
 

    Label (signupscreen,text = "** ENTER the required fields").pack()
    Label (signupscreen,text = "").pack()
        
    Label (signupscreen,text = "** University_ID").pack()
    University_ID = Entry (signupscreen,textvariable = University_ID)
    University_ID.pack()
    Label (signupscreen,text = "").pack()
    
    Label (signupscreen,text = "** Email_ID").pack()
    Email_ID = Entry (signupscreen,textvariable = Email_ID)
    Email_ID.pack()
    Label (signupscreen,text = "").pack()
    
    Label (signupscreen,text = "** FirstName").pack()    
    FirstName = Entry (signupscreen,textvariable = FirstName)
    FirstName.pack()
    Label (signupscreen,text = "").pack()
    
    Label (signupscreen,text = "** LastName").pack()
    LastName = Entry (signupscreen,textvariable = LastName)
    LastName.pack()
    Label (signupscreen,text = "").pack()

    Label (signupscreen,text = "** Username").pack()
    Username = Entry (signupscreen,textvariable = Username)
    Username.pack()
    file.write("\n" + str(Username))
    file.close()
    Label (signupscreen,text = "").pack()
    
    Label (signupscreen,text = "** Password").pack()
    Password_ = Entry (signupscreen, show="*", textvariable = Password).pack()
    Label (signupscreen,text = "").pack()
    
    Label (signupscreen,text = "").pack()
    Radiobutton (signupscreen,text ="Professor",value ="Professor",variable=Role).pack()
    
    Radiobutton (signupscreen,text ="Student",value ="Student",variable=Role).pack()
    Button (signupscreen,text ="Submit" , height ="1", width ="10", command = signup_user).pack()
    Label (signupscreen,text = "").pack()
    Button (signupscreen,text ="Cancel" , height ="1", width ="10", command = exit).pack()


def signup_user():
    username_info = Username.get()
    password_info = Password.get()
    university_info = University_ID.get()
    email_info = Email_ID.get()
    fname_info = FirstName.get()
    lname_info = LastName.get()
    usernameFile = username_info+'.txt'
    list_of_files = os.listdir()
    role = Role.get()
    
    if username_info == "":
        error()

    elif password_info == "":
        error()

    elif university_info == "":
        error()

    elif email_info == "":
        error()

    elif fname_info == "":
        error()

    elif lname_info == "":
        error()

    elif len(password_info) < 8:
        password_check()

    elif len(fname_info) < 2:
        name_check()

    else:
        for line in open("ACL.txt","r").readlines():
            signup_info = line.split()
            if usernameFile in list_of_files:
                messagebox.showinfo("Error","Already registered ACL User")
                
            elif username_info == signup_info[0] or username_info == signup_info[1]:
                signupfile=open(username_info+".txt","w")
                signupfile.write(username_info+'\n')
                signupfile.write(password_info+'\n')
                signupfile.write(role)
                signupfile.close()
                signupscreen.destroy()
                success_register()
                print (role)
                break
            else:
                messagebox.showinfo("Error","Invalid User From ACL")
   
### Login screen page
                

def login():
    global Username
    global Password
    loginscreen = Toplevel(screen)
    loginscreen.title ("Login")
    loginscreen.geometry("400x350")

    Username =StringVar()
    Password =StringVar()
    Label (loginscreen,text = "** ENTER a valid UserId & Password to Access VFMS").pack()
    Label (loginscreen,text = "").pack()
    Label (loginscreen,text = "").pack()
    
    Label (loginscreen,text = "** Username").pack()
    Entry (loginscreen,textvariable = Username).pack()
    Label (loginscreen,text = "").pack()
    
    Label (loginscreen,text = "** Password").pack()    
    Entry (loginscreen,show="*", textvariable = Password).pack()
    Label (loginscreen,text = "").pack()
    Label (loginscreen,text = "").pack()
    Button (loginscreen,text ="Login" , height ="2", width ="30", command = login_verify).pack()
    Label (loginscreen,text = "").pack()
    Button (loginscreen,text ="Cancel" , height ="2", width ="30", command = exit).pack()

### Login Verification
def login_verify():
    username1 = Username.get()
    password1 = Password.get()
    #username_entry1.delete(0, END)
    #password_entry1.delete(0,END)
    username1File = username1+'.txt'
    list_of_files = os.listdir()
    #print(list_of_files)
    if username1 == "":
        error()

    elif password1 == "":
        error()

    elif username1File in list_of_files:
        file1 = open(username1File, "r")
        verify = file1.read().splitlines()
        if password1 in verify:

            ### SCREEN 5 FILE BROWSER
                output = sucess_login()
                #messagebox.showinfo("Success","Login Successful")
                if "Student" in verify:
                 with open("Browser.py") as f:
                    code = compile(f.read(), "Browser.py", "exec")
                    exec(code)
                    
                else:
                   with open("Admin.py") as f:
                       code = compile(f.read(), "Admin.py", "exec")
                       exec(code)
                      
    
            #sucess_login()
            #login_verify()
            #Browser.login_verify()
        else:
            output = password_not_recognised()
           #password_not_recognised()
           
    else:
        output = user_not_found()

               #user_not_found()
               

#### FIRST SCREEN access to login and register
def main_screen():
    global screen
    screen =Tk()
    screen.geometry("800x250")
    screen.title ("                                            Vigilantes File Management System")
    Label (text = "Welcome to Vigilantes File Management System (VFMS)", bg ='Light grey', font = ("Ariel",13)).pack()
    Label (text = "").pack()
    Button (text ="Login" , height ="2", width ="30", command = login).pack()
    Label (text = "").pack()
    Label (text = "OR").pack()
    Label (text = "").pack()
    Label (text = "Click to register with VFMS").pack()
    Button (text ="Signup" , height ="2", width ="30", command = signup).pack()
    screen.mainloop()

main_screen()
