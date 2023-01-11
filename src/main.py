import os
import eel
import tkinter
from tkinter import filedialog
from PIL import Image

dirname = os.path.dirname(__file__)

eel.init(os.path.join(dirname, "view/"))

@eel.expose
def oi():
    tk = tkinter.Tk()
    tk.withdraw()
    tk.overrideredirect(True)
    tk.wm_attributes('-topmost', 1)
    filename = filedialog.askopenfilename(filetypes = [("Imagens", ".png .jpg .jpeg .jfif .tiff")], multiple=True)
    print(filename)
    img = Image.open(r"C:/Users/Jhonata S/Documents/backup/bckp/bckp/5968913008_9f7e66e1a9_o.jpg")
    img = img.save(os.path.join(dirname,"view/_temp/img.png"))
    eel.getResult(filename)

    return

eel.start("main.html")