import tkinter as tk
from tkinter import messagebox
import webbrowser

root = tk.Tk()
root.title("Ang OS X")
root.state('zoomed')
root.iconbitmap('./assets/ang.ico')
bg = tk.PhotoImage(file="../pythonProject/assets/10-6-6kgif.gif")
image = tk.Label(root, image=bg)
image.place(x=0, y=0)


def teachingNotes():
    messagebox.showerror("Teaching Notes", "Teaching Notes are not available as yet.")


def systemPreferences():
    messagebox.showerror("System Preferences", "System Preferences are not available as yet.")


def systemUpdate():
    webbrowser.open_new_tab("https://www.github.com/httpmoeed/angosx")


def shutdown2():
    messagebox.showinfo("Ang OS X", "Ang OS X is shutting down...")
    exit()


teachingNotes = tk.Button(root, text="Teaching Notes", command=teachingNotes)
teachingNotes.pack()
systemPreferences = tk.Button(root, text="System Preferences", command=systemPreferences)
systemPreferences.pack()
systemUpdate = tk.Button(root, text="System Update", command=systemUpdate)
systemUpdate.pack()
shutdownButton2 = tk.Button(root, text="Shutdown Ang OS X", command=shutdown2)
shutdownButton2.pack()

root.mainloop()
