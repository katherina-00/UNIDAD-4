from claseVista import PacienteView, NewPaciente, verImc
from ClaseManejador import manejador

class ControladorPacientes(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.Paciente = list(repo.obtenerListaPacientes())

    # comandos de que se ejecutan a través de la vista
    def crearPaciente(self):
        nuevoPaciente = NewPaciente(self.vista).show()
        if nuevoPaciente:
            Paciente = self.repo.agregarPaciente(nuevoPaciente)
            self.Paciente.append(Paciente)
            self.vista.agregarPaciente(Paciente)

    def seleccionarPaciente(self, index):
        self.seleccion = index
        Paciente = self.Paciente[index]
        self.vista.verPacienteEnForm(Paciente)

    def modificarPaciente(self):
        if self.seleccion==-1:
            return
        rowid = self.Paciente[self.seleccion].rowid
        detallesPaciente = self.vista.obtenerDetalles()
        detallesPaciente.rowid = rowid
        Paciente = self.repo.modificarPaciente(detallesPaciente)
        self.Paciente[self.seleccion] = Paciente
        self.vista.modificarPaciente(Paciente, self.seleccion)
        self.seleccion = -1
    
    def verImc(self):
        if self.seleccion==-1:
            return
        Paciente = self.Paciente[self.seleccion]
        self.vista.verImc(Paciente)
        self.seleccion = -1


    def borrarPaciente(self):
        if self.seleccion==-1:
            return
        Paciente = self.Paciente[self.seleccion]
        self.repo.borrarPaciente(Paciente)
        self.Paciente.pop(self.seleccion)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion = -1

    def start(self):
        for c in self.Paciente:
            self.vista.agregarPaciente(c)
        self.vista.mainloop()
        
    def salirGrabarDatos(self):
        self.repo.grabarDatos()