import os
from tkinter import *
import PIL
from PIL import ImageGrab,ImageDraw
import przetwarzanie


class main:
    def __init__(self, master):
        self.master = master
        self.res = ""
        self.pre = [None, None]
        self.bs = 9
        self.c = Canvas(self.master,bd=3,relief="ridge", width=270, height=270, bg='Gainsboro')
        self.rectangle()
        self.c.pack(side=LEFT)
        self.image1 = PIL.Image.new("RGB", (9, 9), "White")
        f1 = Frame(self.master, padx=20, pady=20)
        self.pr = Label(f1,text="Prediction:",fg="black",font=("",20,"bold"))
        self.pr.pack(pady=20)
        
        
        
        Button(f1,font=("",10),fg="white",bg="black", text="Wyczysc", command=self.clear).pack(side=BOTTOM)
        Button(f1,font=("",10),fg="white",bg="black", text="Rozpoznaj", command=self.getResult).pack(side=BOTTOM)
        f1.pack(side=RIGHT,fill=Y)
        self.c.bind("<Button-1>", self.putPoint)

    def getResult(self):
        self.image1.save("znak.png")
        self.res = str(przetwarzanie.predict("znak.png"))
        self.pr['text'] = "Prediction: " + self.res

    def clear(self):
        self.c.delete('all')
        self.image1 = PIL.Image.new("RGB", (9, 9), "White")
        self.pr['text'] = "Prediction: "
        self.rectangle()

    def putPoint(self, e):
        current = e.widget.find_withtag('current')
        self.c.itemconfigure(current,fill="Black",outline = "Black")
        self.image1.putpixel((int(e.x/30), int(e.y/30)),(0,0,0))

    def rectangle(self):
        for y in range(2,270,30):
            for x in range(2,270,30):
                self.c.create_rectangle(x,y,x+30,y+30,fill="White", width=1,outline="Gainsboro")
                
            


if __name__ == "__main__":
    root = Tk()
    main(root)
    root.title('Rozpoznawanie liczb')
    root.resizable(0, 0)
    root.mainloop()
