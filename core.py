from tkinter import filedialog
from tkinter import *
import os
import ffmpeg

def getFilePath():
    root = Tk()
    root.withdraw()

    home_dir = os.path.expanduser('~')

    arquivo = filedialog.askopenfile(initialdir=home_dir, 
                                    title="Escolha o seu arquivo de texto", 
                                    filetypes=(("Texto", "*.txt"),))

    return arquivo.name

def convert():
    for musica in os.listdir(path='./musics'):
        musica = musica.replace(".m4a", "")
        ffmpeg.input(f'./musics/{musica}.m4a').output(f'./musics/{musica}.mp3').run()

        os.remove(f'./musics/{musica}.m4a')