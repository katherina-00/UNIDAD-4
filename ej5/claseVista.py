import tkinter as tk
from tkinter import messagebox
from ClasePacientes import paciente

class PacienteList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, Paciente, index=tk.END):
        text = "{}, {}".format(Paciente.getApellido(), Paciente.getNombre())
        self.lb.insert(index, text)

    def borrar(self, index):
        self.lb.delete(index, index)

    def modificar(self, contact, index):
        self.borrar(index)
        self.insertar(contact, index)

    def imc(self,Paciente):
        imc=verImc(self)
        imc.Imc(Paciente)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

class PacienteForm(tk.LabelFrame):
    fields = ("Apellido", "Nombre", "Teléfono", "Altura", "Peso")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Paciente", padx=10, pady=10, **kwargs)
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

    def mostrarEstadoPacienteEnFormulario(self, Paciente):
        # a partir de un contacto, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (Paciente.getApellido(), Paciente.getNombre(),
                  Paciente.getTelefono(), Paciente.getAltura(), Paciente.getPeso())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearPacienteDesdeFormulario(self):
        #obtiene los valores de los campos del formulario
        #para crear un nuevo contacto
        values = [e.get() for e in self.entries]
        Paciente = None
        try:
            Paciente = paciente(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return Paciente

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class NewPaciente(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.Paciente = None
        self.form = PacienteForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self):
        self.Paciente = self.form.crearPacienteDesdeFormulario()
        if self.Paciente:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.Paciente



class verImc(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('IMC')
        self.Paciente = None
        self.IMC = tk.Label(self,text="IMC")
        self.IMCEntry=tk.Entry(self,width=20)
        self.comp=tk.Label(self,text='Composicion corporal')
        self.compEntry=tk.Entry(self,width=20)
        self.btn_salir=tk.Button(self,text='Volver',command=self.destroy)

        self.IMC.grid(column=1,row=1,pady=10)
        self.IMCEntry.grid(column=2, row=1, pady=10)
        self.comp.grid(column=1,row=2,pady=10)
        self.compEntry.grid(column=2,row=2,pady=10)
        self.btn_salir.grid(column=2,row=3,pady=10)

    def Imc(self,paciente):
        imc=paciente.getIMC()
        final_imc= '%.2f' % (imc)
        self.IMCEntry.delete(0, tk.END)
        self.IMCEntry.insert(0,final_imc)

        comp=self.comPOCorporal(imc)
        self.compEntry.delete(0, tk.END)
        self.compEntry.insert(0,comp)

    def comPOCorporal(self,imc):
        compCorporal=None
        if imc < 18.5:
            compCorporal = ('Peso inferior al normal')
        elif imc >= 18.5 and imc <= 24.9:
            compCorporal = ('Peso Normal')
        elif imc >= 25 and imc <= 29.9:
            compCorporal = ('Peso superior al normal')
        elif imc >= 30:
            compCorporal = ('Obesidad')
        
        return compCorporal



class UpdatePacienteForm(PacienteForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn = tk.Button(self, text="Ver IMC")
        self.btn.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_save(self, callback):
        self.btn_save.config(command=callback)

    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)
    
    def bind(self, callback):
        self.btn.config(command=callback)
    
    

class PacienteView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Pacientes")
        self.list = PacienteList(self, height=15)
        self.form = UpdatePacienteForm(self)
        self.btn_new = tk.Button(self, text="Agregar paciente")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearPaciente)
        self.list.bind_doble_click(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente)
        self.form.bind_delete(ctrl.borrarPaciente)
        self.form.bind(ctrl.verImc)

    def agregarPaciente(self, Paciente):
        self.list.insertar(Paciente)

    def modificarPaciente(self, Paciente, index):
        self.list.modificar(Paciente, index)

    def borrarPaciente(self, index):
        self.form.limpiar()
        self.list.borrar(index)

    def verImc(self,Paciente):
        self.list.imc(Paciente)

    #obtiene los valores del formulario y crea un nuevo contacto
    def obtenerDetalles(self):
        return self.form.crearPacienteDesdeFormulario()

    #Ver estado de Contacto en formulario de contactos
    def verPacienteEnForm(self, Paciente):
        self.form.mostrarEstadoPacienteEnFormulario(Paciente)