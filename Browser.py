from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import getpass
import os
##import User_Login

##def loginfunc():
##    #loginfunc()
##    c= User_Login.login_verify()
##    ##print(c)
##    

global Path
global Path_def
global window
global saveFile_B
global openFile_B
global openFile
openFile = askopenfilename


def saveFile_B():
   try:      
        output = text.get("1.0",END)
        length= len(output.encode('utf-8'))
        
        if length <= 1024:
           #path, dirs, files = next(os.walk(os.path.dirname(Path_def.get())))
           #print (os.path.dirname(Path_def.get()))
           #numberoffiles=len(files)
           #if numberoffiles<7:
             f = open(Path_def.get(), "w")  
             text1 = f.write(text.get("1.0",END))
             messagebox.showinfo("Success","File Successfully Saved")
           #else: messagebox.showerror("error","Number of Files Exceeds the Limit")
        else:
             messagebox.showerror("error","File Size Exceeds")
   except Exception as e2:
       messagebox.showerror("error","Invalid file/Access Denied")
       print(str(e2))

def DeleteFile_B():
   try:
       os.remove(Path_def.get())
       messagebox.showinfo("Success","Successfully Deleted the File")
   except:
       messagebox.showerror("error","No such file exists")
   
def openFile_B():
    global text
    try:
        path, dirs, files = next(os.walk(os.path.dirname(Path_def.get())))
        print (os.path.dirname(Path_def.get()))
        numberoffiles=len(files)
        print(os.path.exists(Path_def.get()))
        print(os.path.exists(Path_def.get())is True)
        print((os.path.exists(Path_def.get())is True) or numberoffiles<7)
        if (os.path.exists(Path_def.get())is True) or numberoffiles<7:
           
           mode = "r"   
           if (os.path.exists(Path_def.get()) is False):
                                        mode ="w+"
           f = open(Path_def.get(), mode)
           text1 = f.read()
           root = Toplevel(window)
           root.title('Text')
           text = Text(root, height=26, width=50)
            
           text.tag_configure('bold_italics', 
                          font=('Verdana', 12, 'bold', 'italic'))

           text.tag_configure('big', 
                          font=('Verdana', 24, 'bold'))
           text.tag_configure('color', 
                          foreground='blue', 
                          font=('Tempus Sans ITC', 14))
                              
           text.tag_configure('groove', 
                          relief=GROOVE, 
                          borderwidth=2)
           text.insert(INSERT, text1)
                          
           text.tag_bind('bite', 
                     '<1>', 
                     lambda e, t=text: t.insert(END, "Text"))

           text.pack(side=LEFT)
           
           button = Button(root,text="save", command = saveFile_B)
           button.pack(side=BOTTOM)
        else:messagebox.showerror("error","File limit Exceeded; Can not create New Files, Please Delete Existing")
    except Exception as e3:
        messagebox.showerror("error","Invalid file/Access Denied")
        print(str(e3))
       

def browsefiles():
        #swtchuser = os.system('sudo user1 user123')
        #uname = getpass.getuser()
        #uname = os.setuid(swtchuser)
        
        filename = openFile(initialdir = "/", title ="Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
        Path_def.insert(0,filename)
        openFile_B()
        #label_file_explorer.configure(text="File Opened: "+filename+"-"+uname)
        #print(uname)
    

    
##if loginfunc() == "success":

window = Tk()

window.title('File Explorer')

window.geometry("900x500")

window.config(background ="light grey")

label_file_explorer = Label(window,
                            text = "VFMS file management system",
                            width = 100, height = 4,
                            fg = "black")

button_explore = Button(window,
                        text = "Browse Files",command = browsefiles)
button_exit = Button(window,
                     text = "Exit", command = exit)
Path = StringVar()
Label (window,text = "").grid(column =1, row =2)

Label (window,text = "**Enter Folder/FilePath").grid(column =1, row =3)
Label (window,text = "").grid(column =1, row =4)
    
Path_def=Entry (window, textvariable = Path)
Path_def.grid(column =1, row =5)

Label (window,text = "").grid(column =1, row =6)
Label (window,text = "").grid(column =1, row =7)
Button (window,text ="Create New File or Edit" , height ="2", width ="30", command = openFile_B).grid(column =1, row =8)
Label (window,text = "").grid(column =1, row =9)

Label (window,text = "").grid(column =1, row =10)
Label (window,text = "").grid(column =1, row =11)
Button (window,text ="Delete" , height ="2", width ="30", command = DeleteFile_B).grid(column =1, row =12)

label_file_explorer.grid(column =1, row =1)

button_explore.grid(column =1, row =14)

button_exit.grid(column =1, row =15)



window.mainloop ()
##else:
##    elsewindow = Tk()
##
##    elsewindow.title('VFMS file management system')
##    messagebox.showinfo("Access Denied","Un Authorized Access")
##    elsewindow.mainloop ()
##                                                        
                                                        
                                                        
                                                                                                                           
