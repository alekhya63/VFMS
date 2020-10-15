from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename
import subprocess
import grp
import os
import fnmatch



global adminpath
global adminPermissions
global Path_admin
global permission
global Path_Src
global Path_Tgt
global Path_open
global ad_filesize
global adminscreen
global adminpath
global srcpath
global tgtpath
global openpath
global save_File
global open_File
global open_File_B
open_File_B = askopenfilename
 
##Function to open the file names
def browsefiles_ad():
        #swtchuser = os.system('sudo user1 user123')
        #uname = getpass.getuser()
        #uname = os.setuid(swtchuser)
        #browsers =  browsefiles_ad()
        filename = open_File_B(initialdir = "/", title ="Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
        openpath.insert(0,filename)
        open_File()
        #label_file_explorer.configure(text="File Opened: "+filename)
        #print(uname)
   


def DeleteFile_A():
   try:
       os.remove(openpath.get())
       messagebox.showinfo("Success","Successfully Deleted the File")
   except:
       messagebox.showerror("error","No such file exists")
    
## Owner changes the permissions

def change():
    #permission_ad = StringVar()    
    #group =  grp.getgrnam('studentgroup')
    #print(group[2])]

    #os.system("sudo chown :studentgroup "+Path.get())#(Path.get(), -1, group[2])
      
    #os.system("sudo chmod "+permission.get()+" " + Path.get())

    #os.system("sudo ch :studentgroup "+Path.get())
    #con = permission.get()
    #process = subprocess.call(['sudo chmod ', con,' '+Path.get()])
    #os.chmod(Path.get(),int(con, base=8))
    #print(user)
    try:
       print(adminpath.get())
       print("sudo chown :studentgroup "+adminpath.get())
       print("sudo chmod "+adminPermissions.get()+" " + adminpath.get())
       output1 = subprocess.check_output("sudo chown :studentgroup "+adminpath.get(),shell=True)
       print (output1)
       output2 = subprocess.check_output("sudo chmod "+adminPermissions.get()+" " + adminpath.get(),shell=True)
       print (output2)
    except:
       messagebox.showerror("Error","Invalid Path Or Permission")

def save_File():
   try:      
        output = text_a.get("1.0",END)
        length= len(output.encode('utf-8'))
        if length <= 1024:
          fs = open(openpath.get(), "w")  
          text1 = fs.write(text_a.get("1.0",END))
          messagebox.showinfo("Success","File Successfully Saved")
        else:
             messagebox.showerror("error","File Size Exceeds")
   except :
       messagebox.showerror("error","Invalid file/Access Denied")
       
def open_File():
    global text_a
    try:
        path, dirs, files = next(os.walk(os.path.dirname(openpath.get())))
        print (os.path.dirname(openpath.get()))
        numberoffiles=len(files)
        print(os.path.exists(openpath.get()))
        print(os.path.exists(openpath.get())is True)
        print((os.path.exists(openpath.get())is True) or numberoffiles<7)
        if (os.path.exists(openpath.get())is True) or numberoffiles<7:
           
                mode = "r"   
                if (os.path.exists(openpath.get()) is False):
                                        mode ="w+"
                print(openpath.get())
                fo = open(openpath.get(), mode)
                text1 = fo.read()
                root = Toplevel(adminscreen)
                root.title('Text')
                text_a = Text(root, height=26, width=50)
                 
                text_a.tag_configure('bold_italics', 
                               font=('Verdana', 12, 'bold', 'italic'))

                text_a.tag_configure('big', 
                               font=('Verdana', 24, 'bold'))
                text_a.tag_configure('color', 
                               foreground='blue', 
                               font=('Tempus Sans ITC', 14))
                                   
                text_a.tag_configure('groove', 
                               relief=GROOVE, 
                               borderwidth=2)
                text_a.insert(INSERT, text1)
                               
                text_a.tag_bind('bite', 
                          '<1>', 
                          lambda e, t=text_a: t.insert(END, "Text"))

                text_a.pack(side=LEFT)
                
                button = Button(root,text="save", command = save_File)
                button.pack(side=BOTTOM)
        else: messagebox.showerror("error","File limit Exceeded; Can not create New Files, Please Delete Existing")
    except Exception as e:
        messagebox.showerror("error","Invalid file/Access Denied")
        print(str(e))
       


def move_file():
    try:     
            filesize = os.path.getsize(srcpath.get())
            #numberoffiles = len([f for f in os.listdir(srcpath.get()) if os.path.isfile(os.path.join(srcpath.get(),f))])
            #numberoffiles= len(fnmatch.filter(os.listdir(tgtpath.get()),'*.*'))
            path, dirs, files = next(os.walk(tgtpath.get()))
            numberoffiles=len(files)
            if filesize <=1024:

                    if numberoffiles <7 :
                    
                            try:
                               print (numberoffiles)
                               outputm1 = subprocess.check_output("cp "+srcpath.get() +" "+tgtpath.get() ,shell=True)
                               #print (outputm1)
                               messagebox.showinfo("Success","File Copy Successful")
                               
                            except:
                               messagebox.showerror("Error","Invalid File Or Directory")
                               print (numberoffiles)
                    else: messagebox.showerror("Error","Number of files in the target folder exceeds the limit")
            else: messagebox.showerror("Error","File Size Exceeds")
    except:
            messagebox.showerror("Error","Invalid File Or Directory")
    
##Define global variables

def Admin():
    #global Username

    global permission_AD
    #loginscreen = Toplevel(screen)

##Professor access window
adminscreen = Tk()

adminscreen.title('VFMS file management system')

adminscreen.geometry("900x600")

adminscreen.config(background ="light grey")


#Username_admin =StringVar()
Path_admin =StringVar()
permission =StringVar()
Path_Src =StringVar()
Path_Tgt =StringVar()
Path_open =StringVar()

Label (adminscreen,text = "File Access Change").pack()
Label (adminscreen,text = "").pack()
Label (adminscreen,text = "").pack()
Button (adminscreen,text ="Broswe File Structure" , height ="2", width ="30", command = browsefiles_ad).pack()
Label (adminscreen,text = "").pack()

##    Label (loginscreen,text = "** Username").pack()
##    Entry (loginscreen,textvariable = Username).pack()
##    Label (loginscreen,text = "").pack()

Label (adminscreen,text = "**Enter Folder/FilePath").pack()
adminpath=Entry (adminscreen, textvariable = Path_admin)
adminpath.pack()
Label (adminscreen,text = "**Enter Permissions").pack()
adminPermissions = Entry (adminscreen, textvariable = permission)
adminPermissions.pack()
Button (adminscreen,text ="Change Permission" , height ="2", width ="30", command = change).pack()
Label (adminscreen,text = "").pack()

Label (adminscreen,text = "**Enter Src File Path").pack()
srcpath=Entry (adminscreen, textvariable = Path_Src)
srcpath.pack()

Label (adminscreen,text = "**Enter Tgt Folder Path").pack()
tgtpath=Entry (adminscreen, textvariable = Path_Tgt)
tgtpath.pack()

Button (adminscreen,text ="Move/Copy" , height ="2", width ="30", command = move_file).pack()
Label (adminscreen,text = "").pack()
Label (adminscreen,text = "**Enter Src File Path").pack()
openpath=Entry (adminscreen, textvariable = Path_open)
openpath.pack()

Button (adminscreen,text ="Create New File or Edit" , height ="2", width ="30", command = open_File).pack()
Label (adminscreen,text = "").pack()
Button (adminscreen,text ="Delete" , height ="2", width ="30", command = DeleteFile_A).pack()
Label (adminscreen,text = "").pack()
Button (adminscreen,text ="Cancel" , height ="2", width ="30", command =exit).pack()
adminscreen.mainloop()


