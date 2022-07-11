import tkinter as tk
from tkinter import messagebox, CENTER, filedialog, Entry
import os
from time import sleep
import webbrowser

global username, password, username_entry
username = None
password = None
profilePicture = []
userDetails = {}
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

def read_from_file():
    #this will only be used when Ang OS X needs to read this for login stuff
    with open('!DONOTCHANGE Ang OS X Configuration', 'r') as f:
        selectedprofilepicture = f.read()
        profilePicture = selectedprofilepicture.split(',')
        print(profilePicture)

def write_to_file():
    with open('!DONOTCHANGE Ang OS X Configuration', 'w') as f:
        for item in profilePicture:
            f.write(item + ',')

def setup_finished():
    sleep(1)
    root = tk.Tk()
    root.title("Ang OS X")
    root.state('zoomed')
    root.iconbitmap('./assets/ang.ico')
    bg = tk.PhotoImage(file="./assets/10-6-6kgif.gif")
    image = tk.Label(root, image=bg)
    image.place(x=0, y=0)

    def teachingNotes():
        messagebox.showerror("Teaching Notes", "Teaching Notes are not available as yet.")

    def systemPreferences():
        messagebox.showerror("System Preferences", "System Preferences are not available as yet.")

    def systemUpdate():
        webbrowser.open_new_tab("https://www.github.com/httpmoeed/angosx")

    def shutdown():
        messagebox.showinfo("Ang OS X", "Ang OS X is shutting down...")
        exit()

    teachingNotes = tk.Button(root, text="Teaching Notes", command=teachingNotes)
    teachingNotes.pack()
    systemPreferences = tk.Button(root, text="System Preferences", command=systemPreferences)
    systemPreferences.pack()
    systemUpdate = tk.Button(root, text="System Update", command=systemUpdate)
    systemUpdate.pack()
    shutdown = tk.Button(root, text="Shutdown Ang OS X", command=shutdown)
    shutdown.pack()

    root.mainloop()

def nextPage():
    global page, username, passsword, username_entry, frame2, userAccount, setupLabel, username_entry, password_entry
    if page == 1:
        global username
        global password
        page += 1
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
    elif page == 2:
        page += 1
        username.get()
        password.get()
        finished_username = username.get()
        finished_password = password.get()
        print(finished_username)
        print(finished_password)
        frame2.destroy()
        frame3 = tk.Frame(setupWindow, bg=color)
        frame3.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
        finalisation = tk.Label(frame3, text="Setup finished", bg=color, font=("Helvetica", 30))
        finalisation.pack()
        restartProgram = tk.Label(frame3, text="Ang OS X has finished setting up your computer. To continue, Ang OS X will restart.", bg=color,
                                font=("Helvetica", 10))
        restartProgram.pack()
        continueButton = tk.Button(frame3, text="Continue", command=nextPage)
        continueButton.pack()
    elif page == 3:
        setupWindow.destroy()
        setup_finished()


def shutdown():
    messagebox.showinfo("Ang OS X", "Ang OS X is shutting down...")
    exit()


def select_profile_picture():
    filename = filedialog.askopenfilename(initialdir="%USERPROFILE%", title="Select Profile Picture",
                                          filetypes=(("GIF image", "*.gif"),))
    profilePicture.append(filename)
    write_to_file()


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
