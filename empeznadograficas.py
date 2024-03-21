import tkinter

ventana= tkinter.Tk() # contenedor de graficas
ventana.geometry("400x400")

etiqueta=tkinter.Label(ventana, text="hola mundo", bg="green")
etiqueta.pack(fill=tkinter.X) # colocar eñ label en pantalla

cajaNumero1 = tkinter.Entry(ventana, font="Helveltica 20")
cajaNumero1.pack()
cajaNumero2 = tkinter.Entry(ventana, font="Helveltica 20")
cajaNumero2.pack()

def numerosDealacaja():
    numero1=int(cajaNumero1.get())
    numero2=int(cajaNumero2.get())
    resulMultiplicacion= numero1*numero2
    etiquetaResult["text"]= resulMultiplicacion
    #print("el resultado de la multiplicacion es :",resulMultiplicacion)

boton =tkinter.Button(ventana,text="multiplicar", command= numerosDealacaja)
boton.pack()

etiquetaResult=tkinter.Label(ventana, text="", bg="blue", font= "Helveltica 20")
etiquetaResult.pack(fill=tkinter.X) # colocar eñ label en pantalla

ventana.mainloop()







