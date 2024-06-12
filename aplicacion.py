from tkinter import Tk,Label,Button

""" si cambio la extensión a .pyw, la aplicacion se ejecuta al hacer doble click  """

def mensaje():
    print("Mensaje del boton")

ventana=Tk()
""" poner icono """
""" ventana.iconbitmap('icono.ico') """
ventana.geometry("400x280")
ventana.title("Aplicacion")
ventana.minsize(400,280)

lbl=Label(ventana,text='Este es un [Label] tkinter')
lbl.pack()

btn=Button(ventana,text='Presiona este [Button] para mensaje',command=mensaje)
btn.config(fg="red",bg="blue") 
btn.pack()
""" Tambien se puede btn=Button(fg="red",bg="blue",ventana,text='Presiona este [Button] para mensaje',command=mensaje)
btn["fg"]="red" 
btn["bg"]="blue"""


btn2=Button(ventana,text='Salir',command=ventana.quit)
btn2.place(relx=0.5,rely=0.5,width=100,height=30)
"""se puede hacer con porcentajes, relx=0.1,rely=0.1,relwidth=0.1,relheight=0.1 son porcentajes respecto al padre, la ventana"""


ventana.mainloop()