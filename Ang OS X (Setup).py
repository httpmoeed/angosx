import tkinter as tk
from tkinter import messagebox, CENTER, filedialog
import os
from time import sleep


def printInput():
    inp = username_entry.get(1.0, "end-1c")
    print(inp)


global username, password, username_entry
username = None
password = None
userdetails = {}
color = "darkgrey"
setupWindow = tk.Tk()
setupWindow.title("Ang OS X Setup")
setupWindow.state('zoomed')
setupWindow.resizable(False, False)
setupWindow.iconbitmap('./assets/ang.ico')
bg = tk.PhotoImage(file="./assets/10-6-6kgif.gif")
image = tk.Label(setupWindow, image=bg)
image.place(x=0, y=0)
frame = tk.Frame(setupWindow, bg=color)
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
global page
page = 1


def nextPage():
    if page == 1:
        global username
        global password
        frame.destroy()
        welcomeLabel.destroy()
        welcomeLabel2.destroy()
        frame2 = tk.Frame(setupWindow, bg=color)
        frame2.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
        userAccount = tk.Label(frame2, text="Create your user account", bg=color, font=("Helvetica", 30))
        userAccount.pack()
        setupLabel = tk.Button(frame2, text="Set profile picture", command=select_profile_picture)
        setupLabel.pack()
        username_entry = tk.Label(frame2, text="Username", bg=color, font=("Helvetica", 10))
        username_entry.pack()
        username = tk.Entry(frame2)
        username.pack()
        password_entry = tk.Label(frame2, text="Password", bg=color, font=("Helvetica", 10))
        password_entry.pack()
        password = tk.Entry(frame2, show="•")
        password.pack()
        nextButton = tk.Button(frame2, text="Next", command=nextPage)
        nextButton.pack()
        backButton = tk.Button(frame2, text="Previous")
        backButton.pack()
    else:
        pass

def next2():
    pass


def shutdown():
    messagebox.showinfo("Ang OS X", "Ang OS X is shutting down...")
    exit()


def select_profile_picture():
    filename = filedialog.askopenfilename(initialdir="%USERPROFILE%", title="Select Profile Picture",
                                          filetypes=(("GIF image", "*.gif"),))


frame = tk.Frame(setupWindow, bg=color)
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
shutdown = tk.Button(setupWindow, text="Shutdown Ang OS X", command=shutdown)
shutdown.pack()

welcomeLabel = tk.Label(frame, text="Welcome to Ang OS X Setup", bg=color, font=("Helvetica", 30))
welcomeLabel.pack()

welcomeLabel2 = tk.Label(frame,
                         text="The setup assistant will guide you with setting up Ang OS X.\nPlease click 'Next' "
                              "to continue Setup.", bg=color,
                         font=("Helvetica", 10))
welcomeLabel2.pack()
nextButton = tk.Button(frame, text="Next", command=nextPage)
nextButton.pack()
backButton = tk.Button(frame, text="Previous")
backButton.pack()

setupWindow.mainloop()