from tkinter import *
from tkinter import filedialog
from PIL import Image
import os

STANDARD_SIZE = (500, 500)

def squareImage(img, fillColor=(0, 0, 0, 0)):
    x, y = img.size
    size = max(x, y)
    if x != y:
        newImage = Image.new('RGBA', (size, size), fillColor)
        newImage.paste(img, (int((size - x) / 2), int((size - y) / 2)))
        return newImage
    else:
        return img


def selecionaImagem():
    filename = filedialog.askopenfilename(filetypes = [("Imagens", ".png .jpg .jpeg .jfif .tiff")])
    dirImg.set(filename)
    if len(filename) > 40:
        labelImgText.set(filename[:17] + "..." + filename[(len(filename) - 21):])
    else:
        labelImgText.set(filename)


def selecionaSalvarComo():
    dirName = filedialog.asksaveasfilename(defaultextension = ".png", filetypes = [("PNG", ".png")])
    
    if ".jpg" or ".jpeg" or ".jfif" or ".tiff" in dirName:
        dirName = dirName.replace(".jpg", ".png")
        dirName = dirName.replace(".jpeg", ".png")
        dirName = dirName.replace(".jfif", ".png")
        dirName = dirName.replace(".tiff", ".png")

    dirImgSave.set(dirName)
    if len(dirName) > 40:
        labelImgTextSave.set(dirName[:17] + "..." + dirName[(len(dirName) - 21):])
    else:
        labelImgTextSave.set(dirName)


def selecionaRoot():
    folder = filedialog.askdirectory()
    dirFolder.set(folder)
    if len(folder) > 40:
        labelDirFolder.set(folder[:17] + "..." + folder[(len(folder) - 21):])
    else:
        labelDirFolder.set(folder)


def selecionaFinalFolder():
    folder = filedialog.askdirectory()
    dirFinalFolder.set(folder)
    if len(folder) > 40:
        labelDirFinalFolder.set(folder[:17] + "..." + folder[(len(folder) - 21):])
    else:
        labelDirFinalFolder.set(folder)


def squareOneImage():
    if dirImg.get() != "":

        finalName = dirImgSave.get() if dirImgSave.get() != "" else dirImg.get()

        if ".jpg" or ".jpeg" or ".jfif" or ".tiff" in finalName:
            finalName = finalName.replace(".jpg", ".png")
            finalName = finalName.replace(".jpeg", ".png")
            finalName = finalName.replace(".jfif", ".png")
            finalName = finalName.replace(".tiff", ".png")

        loadText.set("Processando...")
        app.configure(cursor = "watch")

        image = Image.open(dirImg.get())
        newImage = squareImage(image)

        if optmize_one and newImage.size[0] > 500:
            newImage = newImage.resize(STANDARD_SIZE, Image.ANTIALIAS)

        newImage.save(finalName, optmize = True, quality = 100)

        app.configure(cursor = "arrow")
        loadText.set("Enquadramento finalizado!")
        imgProcess.configure(fg = "#0F0")
    else:
        loadText.set("Selecione uma imagem.")
        imgProcess.configure(fg = "#F00")


def squareFolder():
    if dirFolder.get() != "":
        
        finalFolder = dirFinalFolder.get() if dirFinalFolder.get() != "" else dirFolder.get()

        loadTextFolder.set("Processando...")
        app.configure(cursor = "watch")

        files = os.listdir(dirFolder.get())

        for filename in files:
            if ".jpg" or ".jpeg" or ".jfif" or ".tiff" in filename:
                image = Image.open(dirFolder.get() + "/" + filename)
                newImage = squareImage(image)

                finalFilename = filename
                finalFilename = finalFilename.replace(".jpg", ".png")
                finalFilename = finalFilename.replace(".jpeg", ".png")
                finalFilename = finalFilename.replace(".jfif", ".png")
                finalFilename = finalFilename.replace(".tiff", ".png")

                if optmize_folder and newImage.size[0] > 500:
                    newImage = newImage.resize(STANDARD_SIZE, Image.ANTIALIAS)

                newImage.save(finalFolder + "/" + finalFilename, optmize = True, quality = 100)

        app.configure(cursor = "arrow")
        loadTextFolder.set("Enquadramento finalizado!")
        imgProcessFolder.configure(fg = "#0F0")
    else:
        loadTextFolder.set("Selecione a pasta de origem.")
        imgProcessFolder.configure(fg = "#F00")


#Cria APP
app = Tk()
#Configurações do APP
bodyPadding = 8
standardBackground = "#F3F3F3"

app.title("Square Image")
# app.iconbitmap("./favicon.ico")
app.configure(background = standardBackground, padx = bodyPadding, pady = bodyPadding)
app.minsize(500, 0)
app.maxsize(500, 600)
app.resizable(False, False)

#Conteúdo do APP

#Padrões
margin = 16
paddingX = 16
paddingY = 8

#Logo
appLogo = Label(app, text = "Square Image", font = 24)
appLogo.pack(fill = X, expand = True, side = "top")

#Layout para processamento de imagem única
formContainer = LabelFrame(app, text = "Enquadrar imagem única")
formContainer.pack(fill = X, expand = True, side = "top")
formContainer.configure(pady = 10)

labelFrame1 = Frame(formContainer)
labelFrame1.pack(fill = X, expand = True, side = "top")
labelFrame1.configure(padx = paddingX)

label1 = Label(labelFrame1, text = "Imagem:")
label1.pack(side = "left")

containerFrame1 = Frame(formContainer)
containerFrame1.pack(fill = X, expand = True, side = "top")
containerFrame1.configure(padx = paddingX, pady = paddingY)

chooseImgBtn = Button(containerFrame1, text = "Selecionar imagem", command = selecionaImagem, width = 20)
chooseImgBtn.pack(side = "right")

dirImg = StringVar()
labelImgText = StringVar()

sourceImg = Label(containerFrame1, textvariable = labelImgText, width = 100, relief = "sunken")
sourceImg.pack(expand = True, side = "left")

labelFrame2 = Frame(formContainer)
labelFrame2.pack(fill = X, expand = True, side = "top")
labelFrame2.configure(padx = paddingX)

label2 = Label(labelFrame2, text = "Nome/local do arquivo:")
label2.pack(side = "left")

containerFrame2 = Frame(formContainer)
containerFrame2.pack(fill = X, expand = True, side = "top")
containerFrame2.configure(padx = paddingX, pady = paddingY)

chooseImgSave = Button(containerFrame2, text = "Salvar como", command = selecionaSalvarComo, width = 20)
chooseImgSave.pack(side = "right")

dirImgSave = StringVar()
labelImgTextSave = StringVar()

imgSave = Label(containerFrame2, textvariable = labelImgTextSave, width = 100, relief = "sunken")
imgSave.pack(expand = True, side = "left")

observation = Frame(formContainer)
observation.pack(fill = X, expand = True, side = "top")
observation.configure(padx = paddingX)

labelObservation = Label(observation, text = "Obs.: Deixar o segundo campo em branco mantém o nome do arquivo.", fg = "#666")
labelObservation.pack(side = "left")

optmizeFrame = Frame(formContainer)
optmizeFrame.pack(fill = X, expand = True, side = "top")
optmizeFrame.configure(padx = paddingX)

optmize_one = IntVar()
checkOptmizeOne = Checkbutton(optmizeFrame, text = "Otimizar imagem para WooCommerce", variable = optmize_one)
checkOptmizeOne.pack(side = "left")

containerFrame3 = Frame(formContainer)
containerFrame3.pack(fill = X, expand = True, side = "top")
containerFrame3.configure(padx = paddingX, pady = paddingY)

loadText = StringVar()

imgProcess = Label(containerFrame3, textvariable = loadText)
imgProcess.pack(expand = True, side = "left")

execOneImg = Button(containerFrame3, text = "Executar", command = squareOneImage, width = 15)
execOneImg.pack(side = "right")

#Layout para processamento em massa
formContainerFolder = LabelFrame(app, text = "Enquadrar pasta")
formContainerFolder.pack(fill = X, expand = True, side = "top")
formContainerFolder.configure(pady = 10)

labelFrameFolder1 = Frame(formContainerFolder)
labelFrameFolder1.pack(fill = X, expand = True, side = "top")
labelFrameFolder1.configure(padx = paddingX)

labelFolder1 = Label(labelFrameFolder1, text = "Pasta de origem:")
labelFolder1.pack(side = "left")

containerFrameFolder1 = Frame(formContainerFolder)
containerFrameFolder1.pack(fill = X, expand = True, side = "top")
containerFrameFolder1.configure(padx = paddingX, pady = paddingY)

chooseDirBtn = Button(containerFrameFolder1, text = "Selecionar pasta", command = selecionaRoot, width = 20)
chooseDirBtn.pack(side = "right")

dirFolder = StringVar()
labelDirFolder = StringVar()

sourceFolder = Label(containerFrameFolder1, textvariable = labelDirFolder, width = 100, relief = "sunken")
sourceFolder.pack(expand = True, side = "left")

labelFrameFolder2 = Frame(formContainerFolder)
labelFrameFolder2.pack(fill = X, expand = True, side = "top")
labelFrameFolder2.configure(padx = paddingX)

labelFolder2 = Label(labelFrameFolder2, text = "Pasta final:")
labelFolder2.pack(side = "left")

containerFrameFolder2 = Frame(formContainerFolder)
containerFrameFolder2.pack(fill = X, expand = True, side = "top")
containerFrameFolder2.configure(padx = paddingX, pady = paddingY)

chooseFinalDirBtn = Button(containerFrameFolder2, text = "Selecionar pasta", command = selecionaFinalFolder, width = 20)
chooseFinalDirBtn.pack(side = "right")

dirFinalFolder = StringVar()
labelDirFinalFolder = StringVar()

destinationFolder = Label(containerFrameFolder2, textvariable = labelDirFinalFolder, width = 100, relief = "sunken")
destinationFolder.pack(expand = True, side = "left")

observationFolder = Frame(formContainerFolder)
observationFolder.pack(fill = X, expand = True, side = "top")
observationFolder.configure(padx = paddingX)

labelObservationFolder = Label(observationFolder, text = "Obs.: Deixar o segundo campo em branco mantém a pasta.", fg = "#666")
labelObservationFolder.pack(side = "left")

optmizeFrameFolder = Frame(formContainerFolder)
optmizeFrameFolder.pack(fill = X, expand = True, side = "top")
optmizeFrameFolder.configure(padx = paddingX)

optmize_folder = IntVar()
checkOptmizeFolder = Checkbutton(optmizeFrameFolder, text = "Otimizar imagem para WooCommerce", variable = optmize_folder)
checkOptmizeFolder.pack(side = "left")

containerFrameFolder3 = Frame(formContainerFolder)
containerFrameFolder3.pack(fill = X, expand = True, side = "top")
containerFrameFolder3.configure(padx = paddingX, pady = paddingY)

loadTextFolder = StringVar()

imgProcessFolder = Label(containerFrameFolder3, textvariable = loadTextFolder)
imgProcessFolder.pack(expand = True, side = "left")

execFolder = Button(containerFrameFolder3, text = "Executar", command = squareFolder, width = 15)
execFolder.pack(side = "right")

mensagem = Label(app, text = "Todas as imagens serão salvas em .png.", fg = "#4b6dde")
mensagem.pack(fill = X, expand = True, side = "top")
mensagem.configure(pady = 10)


#Fim conteúdo do APP

#Roda APP
app.mainloop()