import tkinter as tk
from tkinter import messagebox
from claseProvincia import provincia

class ProvinciaList(tk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    
    def insertar(self, prov, index=tk.END):
        text = "{}".format(prov.getNombre())
        self.lb.insert(index, text)


    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

class ProvinciaForm(tk.LabelFrame):
    fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de departamentos/partidos", "Temperatura","Sensacion termica","Humedad")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoProvinciaEnFormulario(self, prov, datos):
        
        values = (prov.getNombre(), prov.getCapital(),
                  prov.getCantHabitantes(), prov.getCantDepPar(), datos['temp'],datos['feels_like'],datos['humidity'])
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)


    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
            
class NewProvinciaForm(tk.LabelFrame):
    fields = ('Nombre', 'Capital', 'Cantidad de habitantes', 'Cantidad de departamentos/partidos')

    def __init__(self, master, **kwargs):
        super().__init__(master,text='Provincia', padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(column=0, row=position, pady=5)
        entry.grid(column=1, row=position, pady=5)
        return entry

    def crearProvincia(self):
        values = [e.get() for e in self.entries]
        prov = None
        try:
            prov = provincia(*values)
        except ValueError as e:
            messagebox.showerror('Error de validacion', str(e), parent=self)
        return prov

    def confirmar(self):
        self.provincia = self.crearProvincia()
        if self.provincia:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia


class NewProv(tk.Toplevel):

    def __init__(self,master, **kwargs):
        super().__init__(master,**kwargs)
        self.title('Nueva Provicia')
        self.provincia = None
        self.form = NewProvinciaForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self):
        self.provincia = self.form.crearProvincia()
        if self.provincia:
            self.destroy()
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia


class ProvinciaView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias")
        self.list = ProvinciaList(self, height=15)
        self.form = ProvinciaForm(self)
        self.btn_new = tk.Button(self, text="Agregar Provincia")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
        
    def setControlador(self, ctrl):

        self.btn_new.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)
        
    def agregarProvincia(self, prov):
        self.list.insertar(prov)
    
    def obtenerDetalles(self):
        return self.form.crearProvincia()

    def verProvinciaEnForm(self, prov,datos):
        self.form.mostrarEstadoProvinciaEnFormulario(prov,datos)


