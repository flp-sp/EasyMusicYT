import yt_dlp
import os

from core import *

arquivo = getFilePath()

with open(arquivo, "r", encoding="utf-8") as f:
    text = f.read()
url_list = text.splitlines()

ydl_opts = {
    "format" : "bestaudio[ext=m4a]",
    "outtmpl" : "musics/%(title)s.%(ext)s",
}

os.makedirs("./musics", exist_ok=True)

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for url in url_list:
        url = url.split("&")[0]
        if "music" in url:
            url = url.replace("music", "www")
        ydl.download([url])

convert()