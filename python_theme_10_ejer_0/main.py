import tkinter

window = tkinter.Tk()

label1 = tkinter.Label(window, text="label1", bg="yellow", fg= "blue")
label1.pack(ipadx=40, ipady=60, )
label2 = tkinter.Label(window, text="label1", bg="blue", fg= "white")
label2.pack(ipadx=40, ipady=60, fill= "x")
label3 = tkinter.Label(window, text="label1", bg="orange", fg= "blue")
label3.pack(ipadx=40, ipady=60, fill= "x")

label_saludo = tkinter.Label(window, text="hola buenas noches\n", bg="red", fg= "white")
label_saludo.pack(fill="both", expand=True)

window.mainloop()