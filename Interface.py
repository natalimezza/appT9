from tkinter import*

raiz=Tk()
raiz.title("AppT9")
mFrame = Frame()
mFrame.pack()
mFrame.config(width=400, height=350)

mLabel = Label(mFrame, text= "Ingresar un texto: ")
mLabel.grid(row=1, column=0)

cTxt = Text(mFrame, width=16, height=7)
cTxt.grid(row=1, column=1)

scrollVert = Scrollbar(mFrame, command=cTxt.yview)
scrollVert.grid(row=1, column=2, sticky="nsew")

cTxt.config(yscrollcommand=scrollVert.set)

 


raiz.mainloop()
