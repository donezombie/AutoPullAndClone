from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess

def pullFunction(folder_father, self):
  print(folder_father)
  print(os.listdir(folder_father))
  for index, folderChild in enumerate(os.listdir(folder_father)):
    if (folderChild != "checked"):
      print("*" * 10 + " " + folderChild + " " + "*" * 10)
      os.chdir(folder_father+"/"+ folderChild)
      subprocess.call("git stage .",shell=True)
      subprocess.call("git commit -m '.'",shell=True)
      subprocess.check_call("git pull",shell=True)
      # print(subprocess.check_call("git pull",shell=True))
      self.label = Label(self, text=folderChild+" Pull Done!").grid(row=index+3,column=4)
  messagebox.showinfo("Message","Pull Successfully!")
  # subprocess.call("taskkill /IM Python* /F",shell=True)
  # os.system("pause")

def cloneFunction(listGit,pathFolder,self):
  os.chdir(pathFolder)
  for git in listGit:
    subprocess.call("git clone "+ git,shell=True)
  open('checked', 'a').close()
  pull_button = Button(self, text = "Pull", command = self.pull)
  pull_button.grid(row=1,column=3)


title = "Tool Auto Git Pull"
class App(Frame):
    global title
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.init_window()
        self.textGet = StringVar()
        self.path = ''
        self.input = ''
        self.isPull = False
        self.isEmptyFolder = False
        self.dataReadFromFile = None
        self.pack()
        self.entry = Entry(master, textvariable=self.textGet).pack(side = LEFT, expand = True, fill = BOTH )
    def init_window(self):
      self.master.title(title)
      self.master.maxsize(1000,1000)
      self.pack(fill=BOTH, expand = 1)
      quitButton = Button(self, text = "Quit", command = self.exit_app)
      quitButton.grid(row=1, column=1)

      choose_folder_button = Button(self, text = "Choose Folder", command = self.choose_folder)
      choose_folder_button.grid(row=1,column=2)

      # NavBar
      # initial Menu
      menu = Menu(self.master)
      self.master.config(menu=menu)
      # add content Button
      file = Menu(menu)
      file.add_command(label = "Exit", command = self.exit_app)

      about = Menu(menu)
      about.add_command(label = "About Me", command = self.about_me)
      
      # add menu
      menu.add_cascade(label = "File", menu = file )
      menu.add_cascade(label = "Help", menu = about)
    
    def pull(self):
      if self.isPull:
        pullFunction(self.path, self)
      else:
        messagebox.showinfo("Message","Choose Folder Plz")

    def openfile(self):
      filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text Files","*.txt"),("All files","*.*")))
      f = open(filename, 'r')
      self.dataReadFromFile = f.read()

    def show_img(self):
      load = Image.open('pic.jpg')
      render = ImageTk.PhotoImage(load)

      img = Label(self, image = render)
      img.image = render
      img.place(x=0,y=0)

    def about_me(self):
      # self.input = self.textGet.get()
      # print(self.input)
      self.openfile()
      a = self.dataReadFromFile.split("\n")
      print(a)
      print("ABOUT ME")

    def choose_folder(self):
      choosePath = filedialog.askdirectory()
      try:
        dirName =  choosePath
        self.path = dirName
        if len(os.listdir(dirName)) == 0:
            messagebox.showinfo("Message","Choose Successfully!")
            self.isEmptyFolder = True
        else:    
          for folder in os.listdir(dirName):
            if folder == "checked":
              self.isPull = True
              break
            else:
              self.isPull = False
          if self.isPull == False:
            messagebox.showinfo("Message","Directory Is Not Checked!")
        self.label2 = Label(self, text="PATH: "+ self.path).grid(row=2,column=4)
      except FileNotFoundError:
        print("Not Found Folder")
      
      if self.isPull:
        pull_button = Button(self, text = "Pull", command = self.pull)
        pull_button.grid(row=1,column=3)
      elif self.isEmptyFolder:
        clone_button = Button(self, text = "Clone", command = self.clone)
        clone_button.grid(row=1,column=4)

      # print(self.input.split(','))

      # print(dirName)
      # try:
      #   try:
      #       os.makedirs(dirName)    
      #       print("Directory " , dirName ,  " Created ")
      #   except FileExistsError:
      #       print("Directory " , dirName ,  " already exists")  
      # except FileNotFoundError:
      #   print("Not Found Folder")

    def clone(self):
      self.openfile()
      listGit = self.dataReadFromFile.split("\n")
      cloneFunction(listGit, self.path, self)
      messagebox.showinfo("Message","Clone Successfully!")

    def exit_app(self):
      exit()
# create the application
root = Tk()
root.geometry("600x300")
myapp = App()


# start the program
myapp.mainloop()