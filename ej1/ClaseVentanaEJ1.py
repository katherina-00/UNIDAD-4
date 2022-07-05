from tkinter import *
from tkinter import ttk, messagebox
from tkinter import font
from turtle import bgcolor
from webbrowser import BackgroundBrowser

class Aplicacion():
    __ventana = None
    __altura = None
    __peso = None
    __masaMuscular = None
    __compCorporal = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('650x300')
        self.__ventana.title('Calculadora de IMC')
        self.__ventana.config(bg= 'white')
        ttk.Label(self.__ventana, text= "Calculadora de IMC").grid(row= 1, sticky=N)
        mainframe = ttk.Frame(self.__ventana, padding="20 20 50 50")
        mainframe.grid(column = 0, row = 2, sticky = (N, W, E, S))
        mainframe.columnconfigure(1, weight=2)
        mainframe.rowconfigure(1, weight=2)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        s = ttk.Style()
        s.configure('TFrame', background = 'white')
        s.configure('TButton', background = 'green', font ='white', bg='green')
        s.configure('TLabel', background = 'white', font ='white')
        self.__altura = DoubleVar()
        self.__peso = DoubleVar()
        self.__masaMuscular = DoubleVar()
        self.__compCorporal = StringVar()
        self.alturaEntry = ttk.Entry(mainframe, width = 30, textvariable = self.__altura)
        self.alturaEntry.grid(column = 2, row = 2, sticky = (W, E))
        self.pesoEntry = ttk.Entry(mainframe, width = 30, textvariable = self.__peso)
        self.pesoEntry.grid(column = 2, row = 3, sticky = (W, E))
        
        ttk.Label(mainframe, text="Altura:").grid(column = 1, row = 2, sticky = W)
        ttk.Label(mainframe, text="Peso:").grid(column=1, row = 3, sticky = W)
        ttk.Label(mainframe, text= "Tu Indice de Masa Corporal (IMC) es ").grid(column = 1, row = 6, sticky = S)
        ttk.Label(mainframe, textvariable = self.__masaMuscular).grid(column = 2, row = 6, sticky = W)
        ttk.Label(mainframe, textvariable = self.__compCorporal).grid(column = 2, row = 7, sticky = W)
        ttk.Label(mainframe, text= "Kg/m2").grid(column = 3, row = 5, sticky = S)
        ttk.Label(mainframe, text="cm").grid(column = 2, row = 2, sticky = E)
        ttk.Label(mainframe, text="kg").grid(column = 2, row = 3, sticky = E)
        ttk.Button(mainframe, text="Calcular", command= self.calcular).grid(column = 2, row = 5, sticky = W)
        ttk.Button(mainframe, text='Limpiar', command = self.__ventana.destroy).grid(column = 3, row = 5, sticky = W)
        self.alturaEntry.focus()
        self.__ventana.mainloop()

    def calcular(self):
        if self.alturaEntry.get() != '':
            try:
                valor=float(self.alturaEntry.get())
                valor2=float(self.pesoEntry.get())
                valor = (valor/100)**2
                self.__masaMuscular.set( valor2 / valor)
                self.comPOCorporal()
            except ValueError:
                messagebox.showerror(title='Error de tipo',
                                     message='Debe ingresar un valor numérico')
                self.__altura.set('')
                self.__peso.set('')
                self.alturaEntry.focus()
        
    def comPOCorporal(self):
        m = (self.__masaMuscular.get())
        if m < 18.5:
            self.__compCorporal.set('Peso inferior al normal')
        elif m >= 18.5 and m <= 24.9:
            self.__compCorporal.set('Peso Normal')
        elif m >= 25 and m <= 29.9:
            self.__compCorporal.set('Peso superior al normal')
        elif m >= 30:
            self.__compCorporal.set('Obesidad')

def testAPP():
    mi_app = Aplicacion()

if __name__ == '__main__':
    testAPP()
