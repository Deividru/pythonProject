from tkinter import *

window = Tk()
answer = IntVar()
answer2 = IntVar()

def imprimir():
    seleccion = print ("usted ha eleguido", str(answer.get()))
    b2.config(text=seleccion)

def resetear():
    answer.set(0)
    answer2.set(0)

label1 = Label(window, text="Seleccione su vehiculo y su tipo de combustible", bg="Blue", fg= "White")
label1.pack(ipadx=5, ipady=5)


w = Radiobutton(window, text = "Gasolina", variable = answer, value = 1, command= imprimir)
w.pack( anchor= W)

w = Radiobutton(window, text = "Electrico ", variable = answer, value = 2, command= imprimir)
w.pack( anchor= W)

w = Radiobutton(window, text = "Diesel ", variable = answer, value = 3, command= imprimir)
w.pack( anchor= W)

label2 = Label(window, text="seleccione un coche", bg="yellow", fg= "blue")
label2.pack(ipadx=5, ipady=5)

w2 = Radiobutton(window, text = "VW Arteon", variable = answer2, value = 1, command= imprimir)
w2.pack( anchor= W)

w2 = Radiobutton(window, text = "Opel Insignia ", variable = answer2, value = 2, command= imprimir)
w2.pack( anchor= W)

w2 = Radiobutton(window, text = "KIA Proceed ", variable = answer2, value = 3, command= imprimir)
w2.pack( anchor= W)


b2 = Button(window, text = "resetear las opciones ", command = resetear)
b2.pack()

window.mainloop()