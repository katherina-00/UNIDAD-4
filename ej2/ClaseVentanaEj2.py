from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion():
    __ventana = None
    __precio = None
    __iva = None
    __precioIva = None
    __valor = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('600x300')
        self.__ventana.title('Cálculo de IVA')
        mainframe = ttk.Frame(self.__ventana, padding="20 20 50 50")
        mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
        mainframe.columnconfigure(1, weight=2)
        mainframe.rowconfigure(1, weight=2)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        s = ttk.Style()
        s.configure('TFrame', background = 'white')
        s.configure('TButton', background = '', fg='white')
        s.configure('TLabel', background = 'white')
        self.__precio = DoubleVar()
        self.__iva = DoubleVar()
        self.__precioIva = DoubleVar()
        self.__valor = BooleanVar()
        self.precioEntry = ttk.Entry(mainframe, width = 30, textvariable = self.__precio)
        self.precioEntry.grid(column = 2, row = 1, sticky = (W, E))
        ttk.Label(mainframe, text="Precio sin IVA").grid(column=1, row = 1, sticky = W)
        ttk.Label(mainframe, text="IVA").grid(column=1, row = 3, sticky = W)
        ttk.Label(mainframe, text= "Precio con IVA").grid(column = 1, row = 4, sticky = W)
        ttk.Label(mainframe, textvariable = self.__precioIva).grid(column = 2, row = 4, sticky = W)
        ttk.Label(mainframe, textvariable = self.__iva).grid(column = 2, row = 3, sticky = W)
        ttk.Button(mainframe, text="Calcular", command= self.calcular).grid(column = 2, row = 5, sticky = W)
        ttk.Button(mainframe, text='Salir', command = self.__ventana.destroy).grid(column = 3, row = 5, sticky = W)
        ma = ttk.Frame(mainframe)
        ma.grid(row=2, column=1)
        ttk.Radiobutton(ma, text='IVA 21%', value=0, variable = self.__valor , command=self.calculoIva)\
            .grid(row =2, column=0, columnspan=1, sticky='w')
        ttk.Radiobutton(ma, text='IVA 10.5%', value=1, variable = self.__valor, command=self.calculoIva)\
            .grid(row =3, column=0, columnspan=1,sticky='w')
        self.precioEntry.focus()
        self.__ventana.mainloop()

    def calcular(self):
        if self.precioEntry.get() != '':
            try:
                valor=float(self.precioEntry.get())
                self.calculoIva
                self.__precioIva.set(valor + self.__iva.get())
            except ValueError:
                messagebox.showerror(title='Error de tipo',
                                     message='Debe ingresar un valor numérico')
                self.__precio.set('')
                self.precioEntry.focus()

    def calculoIva(self):
        if self.__valor.get()==0:
            self.__iva.set((self.__precio.get() * 21) / 100)
        else:
            if self.__valor.get()==1:
                self.__iva.set((self.__precio.get() * 10.5) / 100)

def test():
    app = Aplicacion()

if __name__ == '__main__':
    test()
    