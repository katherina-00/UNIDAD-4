from tkinter import *
from tkinter import ttk
from tkinter import messagebox





class Aplicacion():
    __ventana=None
    __dolares=None
    __pesos=None
    __cotizacion=None
    def __init__(self,cotizacion):
        self.__cotizacion=cotizacion
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title('Conversor de moneda')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__dolares = StringVar()
        self.__pesos = StringVar()
        self.__dolares.trace('w', self.calcular)
        self.dolaresEntry = ttk.Entry(mainframe, width=7, textvariable=self.__dolares)
        self.dolaresEntry.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.__pesos).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="dolares").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="pesos").grid(column=3, row=2, sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.dolaresEntry.focus()
        self.__ventana.mainloop()

    def calcular(self, *args):
        if self.dolaresEntry.get()!='':
            try:
                valor=float(self.dolaresEntry.get())

                self.__pesos.set(self.__cotizacion*valor)    

            except ValueError:
                messagebox.showerror(title='Error de tipo',
                                     message='Debe ingresar un valor numérico')
                self.__dolares.set('')
                self.dolaresEntry.focus()
        else:
            self.__pesos.set('')
    