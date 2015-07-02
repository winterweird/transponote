# Play around with mouseover colors!
# necessary files in master/images

from Tkinter import *
import os
from PIL import ImageTk, Image

def updateHexColor(rgbtuple, slider, h):
    sval = slider.get()
    c = [0, 0, 0]
    
    for i in range(len(c)):
        if rgbtuple[i].get(): c[i] = 255 if sval >=0 else 255+sval
        else: c[i] = sval if sval >= 0 else 0
    
    rval, gval, bval = c
    hval = "#" + ''.join([('' if v>15 else '0') + hex(v)[2:] for v in (rval, gval, bval)])
    h.set(hval)
    

try:
    PATH = os.path.join(os.path.dirname(__file__))
except:
    PATH = os.path.join(os.getcwd())

root = Tk()
root.geometry("750x300+150+150")

widgets = []

whitespace1 = ImageTk.PhotoImage(Image.open(os.path.join(PATH, "images", "px1whitespace.png")))
whitespace6 = ImageTk.PhotoImage(Image.open(os.path.join(PATH, "images", "px6whitespace.png")))
line6 = ImageTk.PhotoImage(Image.open(os.path.join(PATH, "images", "px6line.png")))
shk = ImageTk.PhotoImage(Image.open(os.path.join(PATH, "images", "sheet_keys.png")))

keys = Label(root, image=shk, bd=0)
keys.grid(row=0, column=0, rowspan=71)

for x in range(71):
    if x%2:
        w = Label(root, image=whitespace1, bd=0)
        w.grid(row=x, column=1)
        continue
    else:
        if 11 < x <61 and not (28 < x < 44) and not x%4:
            w = Label(root, image=line6, activebackground="#000000", bd=0)
        else:
            w = Label(root, image=whitespace6, activebackground="#000000", bd=0)
        if not (33 < x <39):
            w.bind("<Enter>", lambda e: e.widget.config(state=ACTIVE))
            w.bind("<Leave>", lambda e: e.widget.config(state=NORMAL))
    
    w.grid(row=x, column=1)
    widgets.append(w)

r, g, b = IntVar(), IntVar(), IntVar()
red = Checkbutton(root, text="Red", variable=r)
green = Checkbutton(root, text="Green", variable=g)
blue = Checkbutton(root, text="Blue", variable=b)

for i, button in enumerate((red, green, blue)):
    button.grid(column=2, row=i*8, rowspan=8, sticky=W, ipadx=20)

shade = Scale(root, from_=-255, to=255)
shade.grid(row=5, column=2, rowspan=70)

h = StringVar(value="#000000")
hexval = Label(root, textvariable=h, fg="#000000")
hexval.grid(column=2, row=72)

r.trace("w", lambda *args: updateHexColor((r,g,b), shade, h))
g.trace("w", lambda *args: updateHexColor((r,g,b), shade, h))
b.trace("w", lambda *args: updateHexColor((r,g,b), shade, h))
shade.bind("<ButtonRelease-1>", lambda e: updateHexColor((r,g,b), shade, h))
h.trace("w", lambda *args: [(w.config(activebackground=hexval.cget("text")), hexval.config(fg=h.get())) for w in widgets])

root.mainloop()
