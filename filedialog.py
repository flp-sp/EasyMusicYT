from tkinter import filedialog
from tkinter import *
import os

def getFilePath():
    root = Tk()
    root.withdraw()

    home_dir = os.path.expanduser('~')

    arquivo = filedialog.askopenfile(initialdir=home_dir, 
                                    title="Escolha o seu arquivo de texto", 
                                    filetypes=(("Texto", "*.txt"),))

    return arquivo.name