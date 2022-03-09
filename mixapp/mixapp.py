from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
import os
import sys

class Ressources(object):
    """docstring for Ressources"""
    def __init__(self):
        super(Ressources, self).__init__()
    nameapp = ""

if len(sys.argv[1]) > 0:
    if sys.argv[1] == "-createapp":
        if len(sys.argv[2]) > 0:
            # Print output
            # print(f"Nom: {sys.argv[2]}")
            Ressources.nameapp = sys.argv[2]
            output_file = open(f"{Ressources.nameapp}.py", "w")
            output_file.write(f"print(\"Welcome on {Ressources.nameapp} !\")")
            output_file.close()
        else:
            print("MixApp> Enter a correct name for your app !")
    elif sys.argv[1] == "-deleteapp":
        if len(sys.argv[2]) > 0:
            nameofapp = sys.argv[2]
            os.remove(nameofapp + ".py")
        else:
            print("MixApp> Error has been detected.")
    elif sys.argv[1] == "-editapp":
        if len(sys.argv[2]) > 0:
            if sys.argv[2] == "name":
                if len(sys.argv[3]) > 0:
                    if len(sys.argv[4]) > 0:
                        os.rename(f"{sys.argv[3]}.py", f"{sys.argv[4]}.py")
                        Ressources.nameapp = sys.argv[4]
                    else:
                        print("MixApp> Error has been detected.")
                else:
                    print("MixApp> Error has been detected.")
            elif sys.argv[2] == "gui":
                if len(sys.argv[3]) > 0:
                    def notepad():
                        def cancelfile():
                            npgui.destroy()

                        def savefile():
                            t = text.get("1.0", "end-1c")
                            file = open(f'{sys.argv[3]}.py', "w")
                            file.write(t)
                            file.close()
                            mb.showinfo("MixApp","File has been saved with success !")

                        def readfile():
                            file = open(f'{sys.argv[3]}.py', "r")
                            content_file = file.read()
                            file.close()
                            text.insert("1.0", content_file)

                        npgui = Tk()
                        npgui.title(f'MixApp - Editing {sys.argv[3]}.py')
                        npgui.geometry('380x370')
                        npgui.resizable(False, False)
                        npgui.iconbitmap("icons/editing-icon.ico")
                        text = Text(npgui, font=("Arial", 10))
                        text.pack(expand=True, anchor="center")

                        readfile()

                        menu = Menu(npgui)

                        file = Menu(menu, tearoff=0)
                        file.add_command(label="Save", command=savefile)
                        file.add_command(label="Cancel", command=cancelfile)

                        menu.add_cascade(label="File", menu=file)

                        npgui.config(menu=menu)
                        npgui.mainloop()
                    notepad()
                else:
                    print("MixApp> Error has been detected.")
            elif sys.argv[2] == "config":
                if len(sys.argv[3]) > 0:
                    configwindow = Tk()
                    configwindow.title(f'MixApp - Configurate {sys.argv[3]}.py')
                    configwindow.iconbitmap("icons/config-icon.ico")
                    configwindow.geometry('400x400')
                    configwindow.resizable(False, False)
                    configwindow.bind('<Escape>', lambda: configwindow.destroy())

                    nameapp = sys.argv[3]

                    Label(configwindow, text=f"Current Name: ", font=("Arial", 10)).place(relx=0.3, rely=0.1)
                    Label(configwindow, text=f"{sys.argv[3]}", font=("Arial", 10)).place(relx=0.53, rely=0.1)

                    configwindow.mainloop()
                else:
                    print("MixApp> Error has been detected.")
            else:
                print("MixApp> Error has been detected.")
        else:
            print("MixApp> Error has been detected.")
    else:
        print("MixApp> Error has been detected.")
else:
    print("MixApp> Error has been detected.")
