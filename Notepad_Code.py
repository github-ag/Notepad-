import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk
import os

class Notepad:
    master = Tk()

    file = None

    NotepadWidth = 500
    NotepadHeight = 500
    TextArea = Text(master,bg = '#e3fdfd')
    NotepadScrollbar = Scrollbar(TextArea)
    MyLabel = Label(master,text = "Made with ❤️ by ABHISHEK",bg = "#71c9ce",fg = 'red')

    NotepadMenu = Menu(master)

    Submenus = {
        "File" : Menu(NotepadMenu,tearoff = 0),
        "Edit" : Menu(NotepadMenu,tearoff = 0),
        "Help" : Menu(NotepadMenu,tearoff = 0)
        }

    


    def __init__(self,**kwargs):

        # Setting the window dimensions
        try:
            self.NotepadHeight = kwargs['height']
        except:
            pass

        try:
            self.NotepadWidth =  kwargs['width']
        except:
            pass

        self.set_dimensions(self.master,height = self.NotepadHeight,width = self.NotepadWidth)

        # Adding the Title
        self.master.title("Lets Go")

        #Adding the icon
        try:
            self.master.iconbitmap("AG.ico")
        except:
            pass


        # Adding My Label.
        self.MyLabel.pack(fill = X)

        # Adding Text Area
        self.TextArea.pack(fill=BOTH,expand = 1)


##########  Adding menus to the Notepad    ##################
        
        self.AddMainMenu()

        for name,menu in self.Submenus.items():
            self.NotepadMenu.add_cascade(label = name , menu = menu)

        File_commands = {
        "New" : self.NewFile ,
        "Open" : self.OpenFile ,
        "Save" : self.SaveFile ,
        "Quit" : self.QuitFile
        }
        
        Edit_commands = {
        "Cut" : self.Cut , 
        "Copy" : self.Cut , 
        "Paste" : self.Paste ,  
        }

        Help_commands = {
        "About Us" : self.ShowAbout
        }

        
        self.AddCommandsToSubmenu(self.Submenus["File"],File_commands)
        self.AddCommandsToSubmenu(self.Submenus["Edit"],Edit_commands)
        self.AddCommandsToSubmenu(self.Submenus["Help"],Help_commands)
       


        ###########################   RUN BUTTON   ######################################
        #run_button = Button(self.master,bg = 'red',text = "RUN",command = self.RunFile)
        #run_button.place(x = 400,y = 0)


        # To make the textarea auto resizable
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        #######################################   SCROLLBAR   ####################################################

        self.NotepadScrollbar.pack(side=RIGHT, fill=Y)

        # To adjust Scrollbar according to content automatically
        self.NotepadScrollbar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=self.NotepadScrollbar.set)


        
        #####################################       RUNNING THE MASTER WINDOW   #################################
        
        
        
        
        self.master.mainloop()


############################################################  CONSTRUCTOR OVER  #########################################################################################333


    ##################################  CONSTRUCTOR FUNCTIONS  ##########################################################
    def set_dimensions(self,master,**kwargs):
        try:
            self.NotepadWidth = kwargs['width']
        except:
            pass

        try:
            self.NotepadHeight = kwargs['height']
        except:
            pass

        ScreenWidth = self.master.winfo_screenwidth()
        ScreenHeight = self.master.winfo_screenheight()

        left = (ScreenWidth/2) - (self.NotepadWidth/2)
        top = (ScreenHeight/2) - (self.NotepadHeight/2)

        master.geometry('%dx%d+%d+%d' %(self.NotepadWidth,self.NotepadHeight,left,top))


     #############################    ADDING MENU FUNCTIONS   ###############################

    # Adding Main menu to the menu bar 
    def AddMainMenu(self):
        self.master.config(menu = self.NotepadMenu)

    # Adding submenus
    def AddSubMenu(self,name,menu):
        self.NotepadMenu.add_cascade(label = name,menu = menu)

    # Adding commands to the submenu
    def AddCommandsToSubmenu(self,menu,commands_dict):
        for name,func in commands_dict.items():
            menu.add_command(label = name , command = func)


    ################################   FILE FUNCTIONS   ##########################################################
    def NewFile(self):
        self.file = None
        self.master.title("Lets Go")
        self.TextArea.delete(1.0,END)

    def OpenFile(self):
        self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])

        if self.file =="" :
            self.file = None

        else:
            self.master.title(os.path.basename(self.file) + " - Notepad")
            self.TextArea.delete(1.0,END)
            file = open(self.file,'r')
            data = file.read()
            self.TextArea.insert(1.0,data)
            file.close()

    def SaveFile(self):

        #If we want to save the new file
        if self.file==None:
            self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
            if self.file =="":
                self.file = None
            else:
                file = open(self.file,'w')
                file.write(self.TextArea.get(1.0,END))
                file.close()

                # change the window title
                self.master.title(os.path.basename(self.file) + " - Notepad")

        #If we want to save in existing file
        else:
            file = open(self.file,'w')
            file.write(self.TextArea.get(1.0,END))
            file.close()


    def QuitFile(self):

            popup_master = Toplevel()
            self.set_dimensions(popup_master,width = 160, height = 100)
            popup_master.title("Want To Save")
            labelBonus = Label(popup_master,text = "Want To Save?")
            OptionMenu = Label(popup_master)
            labelBonus.grid(row = 0, column = 0)
            OptionMenu.grid(row=1,column = 0)

            def yes_function():
                self.SaveFile()
                popup_master.destroy()


            def no_function():
                popup_master.destroy()
                self.master.destroy()

            yes_button = ttk.Button(OptionMenu,text = 'Yes',command = yes_function )
            no_button = ttk.Button(OptionMenu,text = 'No', command = no_function)
            yes_button.pack(fill = X,side = LEFT)
            no_button.pack(fill = X,side = LEFT)
            popup_master.mainloop()





##############################################  RUN BUTTON  #########################################################
    def RunFile(self):
        exec(self.TextArea.get(1.0, END))



 ############################################   EDIT FUNCTIONS  #############################################

    def Cut(self):
        self.TextArea.event_generate("<<Cut>>")

    def Copy(self):
        self.TextArea.event_generate("<<Copy>>")

    def Paste(self):
        self.TextArea.event_generate("<<Paste>>")

    #######################################  HELP FUNCTIONS  ###################################################

    def ShowAbout(self):
        showinfo("Notepad", "Made with ❤️ by  Abhishek ")





    ### Running the master window
    def Run(self):
        self.master.mainloop()


obj = Notepad()
