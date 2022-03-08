from tkinter import *
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
            elif sys.argv[2] == "editor":
                if len(sys.argv[3]) > 0:
                    def notepad():
                        def savefile():
                            t = text.get("1.0", "end-1c")
                            npgui.destroy()
                            file = open(f'{sys.argv[3]}.py', "w")
                            file.write(t)
                            file.close()
                        def readfile():
                            file = open(f'{sys.argv[3]}.py', "r")
                            content_file = file.read()
                            file.close()
                            text.insert("1.0", content_file)

                        npgui = Tk()
                        npgui.title(f'Editing {sys.argv[3]}.py')
                        npgui.geometry('850x500')
                        npgui.resizable(False, False)
                        text = Text(npgui)
                        text.pack()
                        button = Button(npgui, text="Save", command=savefile)
                        button.pack()

                        readfile()

                        npgui.mainloop()
                    notepad()
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
