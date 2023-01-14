import os
import re
import eel
import tkinter
from PIL import Image
from tkinter import filedialog

DIRNAME = os.path.dirname(__file__)

def isImage(file):
    regex = '.jpg$|.png$|.jpeg$|.tiff$|.jfif$'
    return True if re.search(regex, file) else False
    

def move2temp(files):
    images = []

    for file in files:
        image = Image.open(file)
        regex = '([\d\w\s\.\-\+\*\[\]\}\}\(\)\&\^\%\$\#\@\!\?\,\>\<]+)$'
        filename = re.findall(regex, file)[0]
        dir = "view/_temp/" + filename
        image = image.save(os.path.join(DIRNAME, dir))
        images.append(filename)

    return images


def clearTemp():
    dir = "view/_temp/"
    tempFiles = os.listdir(os.path.join(DIRNAME, dir))
    regex = '.jpg$|.png$|.jpeg$|.tiff$|.jfif$'
    for filename in tempFiles:
        if re.search(regex, filename):
            os.remove(os.path.join(DIRNAME, dir+filename))


def finalize(a, b):
    clearTemp()
    exit()


eel.init(os.path.join(DIRNAME, "view/"))

@eel.expose
def getImages(mode):

    if mode not in ["select", "folder"]:
        return {'error': {'type': 1, 'message': "Undefined select mode. Expected 'select' or 'folder'."}}

    tk = tkinter.Tk()
    tk.withdraw()
    tk.overrideredirect(True)
    tk.wm_attributes('-topmost', 1)

    files = []

    if mode == "select":
        files = filedialog.askopenfilename(filetypes = [("Imagens", ".png .jpg .jpeg .jfif .tiff")], multiple=True)
    elif mode == "folder":
        folder = filedialog.askdirectory()
        files = [folder + "/" + filename for filename in os.listdir(folder)] if folder else []

    if len(files) <= 0:
        return {'error': {'type': 2, 'message': 'No image selected.'}}

    files = [file for file in filter(isImage, files)]

    images = move2temp(files)
    
    return {'images': {'source': images, 'root': files}}
    

eel.start("main.html", size=(800, 600), close_callback=finalize)
