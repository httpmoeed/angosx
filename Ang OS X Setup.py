from tkinter import *
import tkinter.ttk as tk
import time
from tkinter import messagebox, filedialog, Frame, Label


def read_from_file():
    # this will only be used when Ang OS X needs to read this for login stuff
    with open('!DONOTCHANGE Ang OS X Configuration.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            key, label = line.split('/')
            userDetails[key] = label


def write_to_file(key, label):
    # writes the user details and the value of it to the file
    with open('!DONOTCHANGE Ang OS X Configuration.txt', 'a') as file:
        file.write('\n' + key + '/' + label)


def shutdown():
    messagebox.showinfo("Ang OS X", "Ang OS X is shutting down...")
    exit()


changeCounter = 0
page = 0
color = "darkgray"
secondaryColor = "#e3e3e3"
root = Tk()
root.state('zoomed')
root.title('Ang OS X')
root.iconbitmap('./assets/ang.ico')
bg = PhotoImage(file="./assets/10-6-6kgif.gif")
image = tk.Label(root, image=bg)
image.place(x=0, y=0)
angIcon = PhotoImage(file="./assets/ang-1.png")
angIcon = angIcon.subsample(5, 5)
angIconLabel = Label(root, image=angIcon)
angIconLabel.place(x=610, y=190)
startupFrame = Frame(root, bg=secondaryColor, width=1200, height=900)
startupFrame.place(relx=0.5, rely=0.45, anchor="center")
userDetails = {'username': '', 'password': '', 'profilePicture': '', 'setupTrue': ''}
title = Label(startupFrame, text="Ang OS X", bg=secondaryColor, font=("Helvetica", 20))
title.pack()
progress = tk.Progressbar(startupFrame, orient=HORIZONTAL,
                          length=300, mode='determinate')
messages = ["Welcome to Ang OS X.", "Initialising ang.exe", "Checking math tests", "Waiting for ",
            "Are you seriously reading this?"]

read_from_file()

if userDetails['setupTrue'] == 1:
    exec(open("ang os x (no setup).py").read())
    exit()


def select_profile_picture():
    filename = filedialog.askopenfilename(initialdir="%USERPROFILE%", title="Select Profile Picture",
                                          filetypes=(("GIF image", "*.gif"),))
    write_to_file('profilePicture', filename)


def shutdown():
    messagebox.showinfo("Ang OS X", "Ang OS X is shutting down...")
    exit()


def bar():
    for i in range(100):
        if changeCounter % 20 == 0:
            information.config(text=messages[int((i / 20))])
        progress['value'] = i
        root.update_idletasks()
        time.sleep(0.05)
        if i == 99:
            global setupFrame1, page
            page += 1
            startupFrame.destroy()
            angIconLabel.destroy()
            setupFrame1 = Frame(root, bg=color)
            setupFrame1.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
            shutdownButton = Button(root, text="Shutdown Ang OS X", command=shutdown)
            shutdownButton.pack()

            welcomeLabel = Label(setupFrame1, text="Welcome to Ang OS X Setup", bg=color, font=("Helvetica", 30))
            welcomeLabel.pack()

            welcomeLabel2 = Label(setupFrame1,
                                  text="The setup assistant will guide you with setting up Ang OS X. Please click "
                                       "'Next' "
                                       "to continue Setup.", bg=color,
                                  font=("Helvetica", 10))
            welcomeLabel2.pack()
            nextButton = Button(setupFrame1, text="Next", command=nextPage)
            nextButton.pack()
            backButton = Button(setupFrame1, text="Previous")
            backButton.pack()


progress.pack()
information = Label(startupFrame, text="", bg=secondaryColor)
information.pack()
Button(startupFrame, text='Start Ang OS X', command=bar).pack()


def nextPage():
    global page, setupFrame2
    if page == 1:
        global username, password
        page += 1
        setupFrame1.destroy()
        setupFrame2 = Frame(root, bg=color)
        setupFrame2.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
        userAccount = Label(setupFrame2, text="Create your user account", bg=color, font=("Helvetica", 30))
        userAccount.pack()
        setupLabel = Button(setupFrame2, text="Set profile picture", command=select_profile_picture)
        setupLabel.pack()
        username_entry = Label(setupFrame2, text="Username", bg=color, font=("Helvetica", 10))
        username_entry.pack()
        username = Entry(setupFrame2)
        username.pack()
        password_entry = Label(setupFrame2, text="Password", bg=color, font=("Helvetica", 10))
        password_entry.pack()
        password = Entry(setupFrame2, show="•")
        password.pack()
        nextButton = Button(setupFrame2, text="Next", command=nextPage)
        nextButton.pack()
        backButton = Button(setupFrame2, text="Previous")
        backButton.pack()
    elif page == 2:
        page += 1
        username.get()
        password.get()
        write_to_file('username', str(username))
        write_to_file('password', str(password))
        setupFrame2.destroy()
        frame3 = Frame(root, bg=color)
        frame3.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
        finalisation = Label(frame3, text="Setup finished", bg=color, font=("Helvetica", 30))
        finalisation.pack()
        restartProgram = Label(frame3,
                               text="Ang OS X has finished setting up your computer. To continue, Ang OS X will "
                                    "restart and save your information. To start using Ang OS X, run 'Ang OS X.py'",
                               bg=color,
                               font=("Helvetica", 10))
        restartProgram.pack()
        continueButton = Button(frame3, text="Continue", command=nextPage)
        continueButton.pack()
        write_to_file("setupTrue", "1")
    elif page == 3:
        # exec(open("ang os x (no setup).py").read())
        # exit()
        pass


root.mainloop()
