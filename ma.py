from PIL import Image
import sys
import tkinter as tk
from tkinter import filedialog as fd
from scroll import ScrollBar
def ascii():
    global fen
    file = fd.askopenfilename()
    try:
        image=Image.open(file)
    except e:
        tk.Label(fen,text=str(e)).pack()
        sys.exit()
    tk.Label(fen,text="Conversion en cours...").pack()
    val=image.getpixel((0,0))
    haut=image.height
    larg=image.width
    nom='ascii--'+file[len(file)-file[::-1].find('/'):file.find('.')]+'.txt'
    f=open(nom,'w')
    l=[]
    vals=' .:-=+*#%@0'
    nb=0
    for y in range(haut):
        for x in range(larg):
            val=image.getpixel((x,y))
            if type(val)==int:
                f.write(vals[int(val/255*10)])
            else:
                nb+=1
                moy=(val[0]+val[1]+val[2])/3*10/255
                f.write(vals[int(10-moy)])

            
        f.write('\n')
    f.close()
    tk.Label(fen,text="Conversion terminée !").pack()
    tk.Label(fen,text='Enregistré sous "'+nom+'"').pack()
    tk.Button(fen,text="Voir le resultat",command=lambda:show(nom)).pack()
def show(file):
    text=open(file,'r').read()
    ScrollBar(text)

fen=tk.Tk()

tk.Label(fen,text="Convertisseur ASCII",font="Consolas 25 bold").pack()
tk.Label(fen,text=" .:-=+*#%@00@%#*+=-:. ",font="Consolas 10 bold").pack()
tk.Label(fen,text="Par le seigneur µ",font="Consolas 15 bold italic").pack()
tk.Button(fen,text='Choisir une image',command=ascii,font="Consolas 10").pack()

fen.mainloop()

