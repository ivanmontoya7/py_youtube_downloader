from tkinter import Tk,Label,Button,Entry,PhotoImage
from pytube import YouTube

""" si cambio la extensión a .pyw, la aplicacion se ejecuta al hacer doble click  """
foto_miniatura=''

def descargar():
    enlace=link.get()
    yt=YouTube(enlace)
    yt.streams.get_highest_resolution().download()

def previsualizar():
    enlace=link.get()
    yt=YouTube(enlace)
    print(yt.thumbnail_url)

def debug():
    print(ventana.geometry())
    print(lbl.winfo_height())

ventana=Tk()
ventana.geometry("600x448")
ventana.title("Aplicacion")
ventana.minsize(400,280)
ventana.iconbitmap(default='icono.ico')

img=PhotoImage(file='ardilla.png')
lbl_img=Label(width=3000,height=3000,image=img)
lbl_img.pack()

lbl=Label(ventana,text='Enlace: ',borderwidth=2, relief="groove",font='Helvetica 12 bold')
lbl.place(rely=0.1,relx=0.05,relwidth=0.2, relheight=0.1)

link=Entry(ventana,font='Helvetica 12 bold')
link.place(rely=0.1,relx=0.3,relwidth=0.6, height=45)

btn=Button(ventana,text='Descargar',command=descargar,font='Helvetica 12 bold')
btn.place(relx=0.2,rely=0.5,relwidth=0.2, relheight=0.1)

btn2=Button(ventana,text='Previsualizar (no funciona)',command=previsualizar,font='Helvetica 12 bold')
btn2.place(relx=0.6,rely=0.5,relwidth=0.2, relheight=0.1)

btn2=Button(ventana,text='Salir',command=ventana.quit,font='Helvetica 12 bold')
btn2.place(relx=0.4,rely=0.8,relwidth=0.2, relheight=0.1)

btn_dev=Button(ventana,text='debug',command=debug,font='Helvetica 12 bold')
btn_dev.place(relx=0.8,rely=0.8,relwidth=0.2, relheight=0.1)


ventana.mainloop()